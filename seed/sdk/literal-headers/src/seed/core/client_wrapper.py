# This file was auto-generated by Fern from our API Definition.

import typing

import httpx
import typing_extensions


class BaseClientWrapper:
    def __init__(self, *, api_header: typing_extensions.Literal["api header value"], base_url: str):
        self._api_header = api_header
        self._base_url = base_url

    def get_headers(self) -> typing.Dict[str, str]:
        headers: typing.Dict[str, str] = {
            "X-Fern-Language": "Python",
            "X-Fern-SDK-Name": "seed",
            "X-Fern-SDK-Version": "0.0.0",
        }
        headers["X-API-Header"] = self._api_header
        return headers

    def get_base_url(self) -> str:
        return self._base_url


class SyncClientWrapper(BaseClientWrapper):
    def __init__(
        self, *, api_header: typing_extensions.Literal["api header value"], base_url: str, httpx_client: httpx.Client
    ):
        super().__init__(api_header=api_header, base_url=base_url)
        self.httpx_client = httpx_client


class AsyncClientWrapper(BaseClientWrapper):
    def __init__(
        self,
        *,
        api_header: typing_extensions.Literal["api header value"],
        base_url: str,
        httpx_client: httpx.AsyncClient
    ):
        super().__init__(api_header=api_header, base_url=base_url)
        self.httpx_client = httpx_client
