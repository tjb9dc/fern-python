# This file was auto-generated by Fern from our API Definition.

import json
import typing
import urllib.parse
from json.decoder import JSONDecodeError

import httpx
import pydantic

from ...core.api_error import ApiError
from ...core.jsonable_encoder import jsonable_encoder
from .types.stream_response import StreamResponse


class AiClient:
    def __init__(self, *, environment: str):
        self._environment = environment

    def generate_stream(self, *, num_events: int) -> typing.Iterator[StreamResponse]:
        with httpx.stream(
            "POST",
            urllib.parse.urljoin(f"{self._environment}/", "generate-stream"),
            json=jsonable_encoder({"num_events": num_events}),
            timeout=60,
        ) as _response:
            if 200 <= _response.status_code < 300:
                for _text in _response.iter_text():
                    if len(_text) == 0:
                        continue
                    yield pydantic.parse_obj_as(StreamResponse, json.loads(_text))  # type: ignore
                return
            try:
                _response_json = _response.json()
            except JSONDecodeError:
                raise ApiError(status_code=_response.status_code, body=_response.text)
            raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncAiClient:
    def __init__(self, *, environment: str):
        self._environment = environment

    async def generate_stream(self, *, num_events: int) -> typing.AsyncIterator[StreamResponse]:
        async with httpx.AsyncClient() as _client:
            async with _client.stream(
                "POST",
                urllib.parse.urljoin(f"{self._environment}/", "generate-stream"),
                json=jsonable_encoder({"num_events": num_events}),
                timeout=60,
            ) as _response:
                if 200 <= _response.status_code < 300:
                    async for _text in _response.aiter_text():
                        if len(_text) == 0:
                            continue
                        yield pydantic.parse_obj_as(StreamResponse, json.loads(_text))  # type: ignore
                    return
                try:
                    _response_json = _response.json()
                except JSONDecodeError:
                    raise ApiError(status_code=_response.status_code, body=_response.text)
                raise ApiError(status_code=_response.status_code, body=_response_json)