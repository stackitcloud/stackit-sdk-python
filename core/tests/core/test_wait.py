import time
from typing import Any, Callable, List, Tuple, Union

import pytest

from stackit.core.wait import Wait, WaitConfig


def timeout_check_function() -> Tuple[bool, Union[Exception, None], Union[int, None], Any]:
    time.sleep(9999)
    return True, None, None, None


def create_check_function(
    error_codes: Union[List[int], None], tries_to_success: int, correct_return: str
) -> Callable[[None], Tuple[bool, Union[Exception, None], Union[int, None], Any]]:
    error_code_counter = 0
    tries_to_success_counter = 0

    def check_function() -> Tuple[bool, Union[Exception, None], Union[int, None], Any]:
        nonlocal error_code_counter
        nonlocal tries_to_success_counter

        if error_codes and error_code_counter < len(error_codes):
            code = error_codes[error_code_counter]
            error_code_counter += 1
            return False, Exception("Some exception"), code, None
        elif tries_to_success_counter < tries_to_success:
            tries_to_success_counter += 1
            return False, None, 200, None
        else:
            return True, None, 200, correct_return

    return check_function


class TestWait:
    def test_timeout_throws_timeouterror(self):
        wait = Wait(timeout_check_function, WaitConfig(timeout=1))

        with pytest.raises(TimeoutError, match="Wait has timed out"):
            wait.wait()

    def test_throttle_0_throws_error(self):
        with pytest.raises(ValueError, match="throttle can't be 0"):
            _ = Wait(lambda: (True, None, None, None), WaitConfig(throttle=0))

    @pytest.mark.parametrize(
        "check_function",
        [
            create_check_function([400], 3, "Shouldn't be returned"),
        ],
    )
    def test_throws_for_no_retry_status_code(self, check_function):
        wait = Wait(check_function)
        with pytest.raises(Exception, match="Some exception"):
            wait.wait()

    @pytest.mark.parametrize(
        "correct_return,error_retry_limit,check_function",
        [
            (
                "This was a triumph.",
                0,
                create_check_function(None, 0, "This was a triumph."),
            ),
            (
                "I'm making a note here: HUGE SUCCESS.",
                3,
                create_check_function([502, 504], 3, "I'm making a note here: HUGE SUCCESS."),
            ),
        ],
    )
    def test_return_is_correct(
        self,
        correct_return: str,
        error_retry_limit: int,
        check_function: Callable[[None], Tuple[bool, Union[Exception, None], Union[int, None], Any]],
    ):
        wait = Wait(check_function, WaitConfig(error_retry_limit))
        assert wait.wait() == correct_return
