# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from .playlist_id import PlaylistId


class PlaylistIdNotFoundErrorBody_PlaylistId(pydantic.BaseModel):
    type: typing_extensions.Literal["playlistId"]
    value: PlaylistId


PlaylistIdNotFoundErrorBody = typing.Union[PlaylistIdNotFoundErrorBody_PlaylistId]
