# coding: utf-8

"""
    STACKIT Observability API

    API endpoints for Observability on STACKIT

    The version of the OpenAPI document: 1.1.1
    Contact: stackit-argus@mail.schwarz
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501 docstring might be too long

from __future__ import annotations

import json
import pprint
from typing import Any, ClassVar, Dict, List, Optional, Set, Union

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    StrictBool,
    StrictFloat,
    StrictInt,
    StrictStr,
    field_validator,
)
from typing_extensions import Annotated, Self

from stackit.observability.models.create_scrape_config_payload_basic_auth import (
    CreateScrapeConfigPayloadBasicAuth,
)
from stackit.observability.models.create_scrape_config_payload_http_sd_configs_inner import (
    CreateScrapeConfigPayloadHttpSdConfigsInner,
)
from stackit.observability.models.create_scrape_config_payload_http_sd_configs_inner_oauth2 import (
    CreateScrapeConfigPayloadHttpSdConfigsInnerOauth2,
)
from stackit.observability.models.create_scrape_config_payload_http_sd_configs_inner_oauth2_tls_config import (
    CreateScrapeConfigPayloadHttpSdConfigsInnerOauth2TlsConfig,
)
from stackit.observability.models.create_scrape_config_payload_metrics_relabel_configs_inner import (
    CreateScrapeConfigPayloadMetricsRelabelConfigsInner,
)
from stackit.observability.models.create_scrape_config_payload_static_configs_inner import (
    CreateScrapeConfigPayloadStaticConfigsInner,
)


class CreateScrapeConfigPayload(BaseModel):
    """
    CreateScrapeConfigPayload
    """

    basic_auth: Optional[CreateScrapeConfigPayloadBasicAuth] = Field(default=None, alias="basicAuth")
    bearer_token: Optional[StrictStr] = Field(
        default=None,
        description="Sets the 'Authorization' header on every scrape request with the configured bearer token. It is mutually exclusive with 'bearer_token_file'. `Additional Validators:` * needs to be a valid bearer token * if bearerToken is in the body no other authentication method should be in the body",
        alias="bearerToken",
    )
    honor_labels: Optional[StrictBool] = Field(
        default=False,
        description="Note that any globally configured 'external_labels' are unaffected by this setting. In communication with external systems, they are always applied only when a time series does not have a given label yet and are ignored otherwise.",
        alias="honorLabels",
    )
    honor_time_stamps: Optional[StrictBool] = Field(
        default=False,
        description="honor_timestamps controls whether Prometheus respects the timestamps present in scraped data. If honor_timestamps is set to 'true', the timestamps of the metrics exposed by the target will be used.",
        alias="honorTimeStamps",
    )
    http_sd_configs: Optional[List[CreateScrapeConfigPayloadHttpSdConfigsInner]] = Field(
        default=None,
        description="HTTP-based service discovery provides a more generic way to configure static targets and serves as an interface to plug in custom service discovery mechanisms.",
        alias="httpSdConfigs",
    )
    job_name: Annotated[str, Field(min_length=1, strict=True, max_length=200)] = Field(
        description="The job name assigned to scraped metrics by default. `Additional Validators:` * must be unique * key and values should only include the characters: a-zA-Z0-9-",
        alias="jobName",
    )
    metrics_path: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=200)]] = Field(
        default="/metrics",
        description="The HTTP resource path on which to fetch metrics from targets. E.g. /metrics",
        alias="metricsPath",
    )
    metrics_relabel_configs: Optional[List[CreateScrapeConfigPayloadMetricsRelabelConfigsInner]] = Field(
        default=None, description="List of metric relabel configurations", alias="metricsRelabelConfigs"
    )
    oauth2: Optional[CreateScrapeConfigPayloadHttpSdConfigsInnerOauth2] = None
    params: Optional[Dict[str, Any]] = Field(
        default=None,
        description="Optional http params `Additional Validators:` * should not contain more than 5 keys * each key and value should not have more than 200 characters",
    )
    sample_limit: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None,
        description="Per-scrape limit on number of scraped samples that will be accepted. If more than this number of samples are present after metric relabeling the entire scrape will be treated as failed. The total limit depends on the service plan target limits * samples",
        alias="sampleLimit",
    )
    scheme: StrictStr = Field(description="Configures the protocol scheme used for requests. https or http")
    scrape_interval: Annotated[str, Field(min_length=2, strict=True, max_length=8)] = Field(
        description="How frequently to scrape targets from this job. E.g. 5m `Additional Validators:` * must be a valid time format* must be >= 60s",
        alias="scrapeInterval",
    )
    scrape_timeout: Annotated[str, Field(min_length=2, strict=True, max_length=8)] = Field(
        description="Per-scrape timeout when scraping this job. `Additional Validators:` * must be a valid time format* must be smaller than scrapeInterval",
        alias="scrapeTimeout",
    )
    static_configs: List[CreateScrapeConfigPayloadStaticConfigsInner] = Field(
        description="A list of scrape configurations.", alias="staticConfigs"
    )
    tls_config: Optional[CreateScrapeConfigPayloadHttpSdConfigsInnerOauth2TlsConfig] = Field(
        default=None, alias="tlsConfig"
    )
    __properties: ClassVar[List[str]] = [
        "basicAuth",
        "bearerToken",
        "honorLabels",
        "honorTimeStamps",
        "httpSdConfigs",
        "jobName",
        "metricsPath",
        "metricsRelabelConfigs",
        "oauth2",
        "params",
        "sampleLimit",
        "scheme",
        "scrapeInterval",
        "scrapeTimeout",
        "staticConfigs",
        "tlsConfig",
    ]

    @field_validator("scheme")
    def scheme_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(["http", "https"]):
            raise ValueError("must be one of enum values ('http', 'https')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of CreateScrapeConfigPayload from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of basic_auth
        if self.basic_auth:
            _dict["basicAuth"] = self.basic_auth.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in http_sd_configs (list)
        _items = []
        if self.http_sd_configs:
            for _item in self.http_sd_configs:
                if _item:
                    _items.append(_item.to_dict())
            _dict["httpSdConfigs"] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in metrics_relabel_configs (list)
        _items = []
        if self.metrics_relabel_configs:
            for _item in self.metrics_relabel_configs:
                if _item:
                    _items.append(_item.to_dict())
            _dict["metricsRelabelConfigs"] = _items
        # override the default output from pydantic by calling `to_dict()` of oauth2
        if self.oauth2:
            _dict["oauth2"] = self.oauth2.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in static_configs (list)
        _items = []
        if self.static_configs:
            for _item in self.static_configs:
                if _item:
                    _items.append(_item.to_dict())
            _dict["staticConfigs"] = _items
        # override the default output from pydantic by calling `to_dict()` of tls_config
        if self.tls_config:
            _dict["tlsConfig"] = self.tls_config.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CreateScrapeConfigPayload from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "basicAuth": (
                    CreateScrapeConfigPayloadBasicAuth.from_dict(obj["basicAuth"])
                    if obj.get("basicAuth") is not None
                    else None
                ),
                "bearerToken": obj.get("bearerToken"),
                "honorLabels": obj.get("honorLabels") if obj.get("honorLabels") is not None else False,
                "honorTimeStamps": obj.get("honorTimeStamps") if obj.get("honorTimeStamps") is not None else False,
                "httpSdConfigs": (
                    [CreateScrapeConfigPayloadHttpSdConfigsInner.from_dict(_item) for _item in obj["httpSdConfigs"]]
                    if obj.get("httpSdConfigs") is not None
                    else None
                ),
                "jobName": obj.get("jobName"),
                "metricsPath": obj.get("metricsPath") if obj.get("metricsPath") is not None else "/metrics",
                "metricsRelabelConfigs": (
                    [
                        CreateScrapeConfigPayloadMetricsRelabelConfigsInner.from_dict(_item)
                        for _item in obj["metricsRelabelConfigs"]
                    ]
                    if obj.get("metricsRelabelConfigs") is not None
                    else None
                ),
                "oauth2": (
                    CreateScrapeConfigPayloadHttpSdConfigsInnerOauth2.from_dict(obj["oauth2"])
                    if obj.get("oauth2") is not None
                    else None
                ),
                "params": obj.get("params"),
                "sampleLimit": obj.get("sampleLimit"),
                "scheme": obj.get("scheme"),
                "scrapeInterval": obj.get("scrapeInterval"),
                "scrapeTimeout": obj.get("scrapeTimeout"),
                "staticConfigs": (
                    [CreateScrapeConfigPayloadStaticConfigsInner.from_dict(_item) for _item in obj["staticConfigs"]]
                    if obj.get("staticConfigs") is not None
                    else None
                ),
                "tlsConfig": (
                    CreateScrapeConfigPayloadHttpSdConfigsInnerOauth2TlsConfig.from_dict(obj["tlsConfig"])
                    if obj.get("tlsConfig") is not None
                    else None
                ),
            }
        )
        return _obj
