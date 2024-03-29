# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

import httpx
import pydantic

from ...core.api_error import ApiError
from ...core.jsonable_encoder import jsonable_encoder
from ...environment import FernIrEnvironment
from ..commons.errors.invalid_movie_error import InvalidMovieError
from ..commons.errors.movie_already_exists_error import MovieAlreadyExistsError
from ..commons.errors.movie_not_found_error import MovieNotFoundError
from ..commons.types.movie import Movie
from ..commons.types.movie_id import MovieId


class AClient:
    def __init__(self, *, environment: FernIrEnvironment = FernIrEnvironment.PRODUCTION):
        self._environment = environment

    def get_movie(self, movie_id: MovieId) -> Movie:
        _response = httpx.request(
            "GET", urllib.parse.urljoin(f"{self._environment.server_a}/", f"movie/movie/{movie_id}"), timeout=60
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Movie, _response.json())  # type: ignore
        if _response.status_code == 404:
            raise MovieNotFoundError(pydantic.parse_obj_as(MovieId, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_all_movies(self) -> typing.List[Movie]:
        _response = httpx.request(
            "GET", urllib.parse.urljoin(f"{self._environment.server_b}/", "movie/all-movies"), timeout=60
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.List[Movie], _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create_movie(self, *, request: Movie) -> None:
        _response = httpx.request(
            "POST",
            urllib.parse.urljoin(f"{self._environment.server_a}/", "movie/movie"),
            json=jsonable_encoder(request),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return
        if _response.status_code == 429:
            raise MovieAlreadyExistsError()
        if _response.status_code == 400:
            raise InvalidMovieError(pydantic.parse_obj_as(MovieId, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def delete_movie(self, movie_id: MovieId) -> None:
        _response = httpx.request(
            "DELETE", urllib.parse.urljoin(f"{self._environment.server_a}/", f"movie/{movie_id}"), timeout=60
        )
        if 200 <= _response.status_code < 300:
            return
        if _response.status_code == 404:
            raise MovieNotFoundError(pydantic.parse_obj_as(MovieId, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncAClient:
    def __init__(self, *, environment: FernIrEnvironment = FernIrEnvironment.PRODUCTION):
        self._environment = environment

    async def get_movie(self, movie_id: MovieId) -> Movie:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "GET", urllib.parse.urljoin(f"{self._environment.server_a}/", f"movie/movie/{movie_id}"), timeout=60
            )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Movie, _response.json())  # type: ignore
        if _response.status_code == 404:
            raise MovieNotFoundError(pydantic.parse_obj_as(MovieId, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_all_movies(self) -> typing.List[Movie]:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "GET", urllib.parse.urljoin(f"{self._environment.server_b}/", "movie/all-movies"), timeout=60
            )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.List[Movie], _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def create_movie(self, *, request: Movie) -> None:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "POST",
                urllib.parse.urljoin(f"{self._environment.server_a}/", "movie/movie"),
                json=jsonable_encoder(request),
                timeout=60,
            )
        if 200 <= _response.status_code < 300:
            return
        if _response.status_code == 429:
            raise MovieAlreadyExistsError()
        if _response.status_code == 400:
            raise InvalidMovieError(pydantic.parse_obj_as(MovieId, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def delete_movie(self, movie_id: MovieId) -> None:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "DELETE", urllib.parse.urljoin(f"{self._environment.server_a}/", f"movie/{movie_id}"), timeout=60
            )
        if 200 <= _response.status_code < 300:
            return
        if _response.status_code == 404:
            raise MovieNotFoundError(pydantic.parse_obj_as(MovieId, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
