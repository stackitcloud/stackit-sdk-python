from dataclasses import dataclass, field
import signal
import time
from http import HTTPStatus
from typing import Any, Callable, List, Tuple, Union


@dataclass
class WaitConfig:
    sleep_before_wait: int = 0
    throttle: int = 5
    timeout: int = 30
    temp_error_retry_limit: int = 5
    retry_http_error_status_codes: List[int] = field(
        default_factory=lambda: [HTTPStatus.BAD_GATEWAY, HTTPStatus.GATEWAY_TIMEOUT]
    )


class Wait:

    def __init__(
        self,
        check_function: Callable[[None], Tuple[bool, Union[Exception, None], Union[int, None], Any]],
        config: Union[WaitConfig, None] = None,
    ) -> None:
        self._config = config if config else WaitConfig()
        if self._config.throttle == 0:
            raise ValueError("throttle can't be 0")
        self._check_function = check_function

    @staticmethod
    def _timeout_handler(signum, frame):
        raise TimeoutError("Wait has timed out")

    def wait(self) -> Any:
        time.sleep(self._config.sleep_before_wait)

        retry_temp_error_counter = 0

        signal.signal(signal.SIGALRM, Wait._timeout_handler)
        signal.alarm(self._config.timeout * 60)

        while True:

            done, error, code, result = self._check_function()
            if error:
                retry_temp_error_counter = self._handle_error(retry_temp_error_counter, error, code)

            if done:
                return result
            time.sleep(self._config.throttle)

    def _handle_error(self, retry_temp_error_counter: int, error, code: int):

        if code in self._config.retry_http_error_status_codes:
            retry_temp_error_counter += 1
            if retry_temp_error_counter == self._config.temp_error_retry_limit:
                raise error
            return retry_temp_error_counter
        else:
            raise error
