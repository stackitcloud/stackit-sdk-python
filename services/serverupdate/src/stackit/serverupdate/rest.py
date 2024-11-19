# coding: utf-8

"""
    STACKIT Server Update Management API

    API endpoints for Server Update Operations on STACKIT Servers.

    The version of the OpenAPI document: 1.0
    Contact: support@stackit.de
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501 docstring might be too long

import io
import json
import re

import requests
from stackit.core.authorization import Authorization
from stackit.core.configuration import Configuration

from stackit.serverupdate.exceptions import ApiException, ApiValueError


RESTResponseType = requests.Response


class RESTResponse(io.IOBase):

    def __init__(self, resp) -> None:
        self.response = resp
        self.status = resp.status_code
        self.reason = resp.reason
        self.data = None

    def read(self):
        if self.data is None:
            self.data = self.response.content
        return self.data

    def getheaders(self):
        """Returns a dictionary of the response headers."""
        return self.response.headers

    def getheader(self, name, default=None):
        """Returns a given response header."""
        return self.response.headers.get(name, default)


class RESTClientObject:
    def __init__(self, config: Configuration) -> None:
        self.session = config.custom_http_session if config.custom_http_session else requests.Session()
        authorization = Authorization(config)
        self.session.auth = authorization.auth_method

    def request(self, method, url, headers=None, body=None, post_params=None, _request_timeout=None):
        """Perform requests.

        :param method: http request method
        :param url: http request url
        :param headers: http request headers
        :param body: request json body, for `application/json`
        :param post_params: request post parameters,
                            `application/x-www-form-urlencoded`
                            and `multipart/form-data`
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        """
        method = method.upper()
        if method not in ["GET", "HEAD", "DELETE", "POST", "PUT", "PATCH", "OPTIONS"]:
            raise ValueError("Method %s not allowed", method)

        if post_params and body:
            raise ApiValueError("body parameter cannot be used with post_params parameter.")

        post_params = post_params or {}
        headers = headers or {}

        try:
            # For `POST`, `PUT`, `PATCH`, `OPTIONS`, `DELETE`
            if method in ["POST", "PUT", "PATCH", "OPTIONS", "DELETE"]:

                # no content type provided or payload is json
                content_type = headers.get("Content-Type")
                if not content_type or re.search("json", content_type, re.IGNORECASE):
                    request_body = None
                    if body is not None:
                        request_body = json.dumps(body)
                    r = self.session.request(
                        method,
                        url,
                        data=request_body,
                        headers=headers,
                    )
                elif content_type == "application/x-www-form-urlencoded":
                    r = self.session.request(
                        method,
                        url,
                        params=post_params,
                        headers=headers,
                    )
                elif content_type == "multipart/form-data":
                    # must del headers['Content-Type'], or the correct
                    # Content-Type which generated by urllib3 will be
                    # overwritten.
                    del headers["Content-Type"]
                    # Ensures that dict objects are serialized
                    post_params = [(a, json.dumps(b)) if isinstance(b, dict) else (a, b) for a, b in post_params]
                    r = self.session.request(
                        method,
                        url,
                        files=post_params,
                        headers=headers,
                    )
                # Pass a `string` parameter directly in the body to support
                # other content types than JSON when `body` argument is
                # provided in serialized form.
                elif isinstance(body, str) or isinstance(body, bytes):
                    r = self.session.request(
                        method,
                        url,
                        data=body,
                        headers=headers,
                    )
                elif headers["Content-Type"] == "text/plain" and isinstance(body, bool):
                    request_body = "true" if body else "false"
                    r = self.session.request(method, url, data=request_body, headers=headers)
                else:
                    # Cannot generate the request from given parameters
                    msg = """Cannot prepare a request message for provided
                             arguments. Please check that your arguments match
                             declared content type."""
                    raise ApiException(status=0, reason=msg)
            # For `GET`, `HEAD`
            else:
                r = self.session.request(
                    method,
                    url,
                    params={},
                    headers=headers,
                )
        except requests.exceptions.SSLError as e:
            msg = "\n".join([type(e).__name__, str(e)])
            raise ApiException(status=0, reason=msg)

        return RESTResponse(r)