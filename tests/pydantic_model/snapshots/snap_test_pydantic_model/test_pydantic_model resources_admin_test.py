# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions


class Test_And(pydantic.BaseModel):
    type: typing_extensions.Literal["and"]
    value: bool


class Test_Or(pydantic.BaseModel):
    type: typing_extensions.Literal["or"]
    value: bool


Test = typing.Union[Test_And, Test_Or]
