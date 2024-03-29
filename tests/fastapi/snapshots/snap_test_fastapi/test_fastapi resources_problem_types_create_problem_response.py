# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

import pydantic
import typing_extensions

from ....core.datetime_utils import serialize_datetime
from ...commons.types.problem_id import ProblemId
from .create_problem_error import CreateProblemError

T_Result = typing.TypeVar("T_Result")


class _Factory:
    def success(self, value: ProblemId) -> CreateProblemResponse:
        return CreateProblemResponse(__root__=_CreateProblemResponse.Success(type="success", value=value))

    def error(self, value: CreateProblemError) -> CreateProblemResponse:
        return CreateProblemResponse(__root__=_CreateProblemResponse.Error(type="error", value=value))


class CreateProblemResponse(pydantic.BaseModel):
    factory: typing.ClassVar[_Factory] = _Factory()

    def get_as_union(self) -> typing.Union[_CreateProblemResponse.Success, _CreateProblemResponse.Error]:
        return self.__root__

    def visit(
        self, success: typing.Callable[[ProblemId], T_Result], error: typing.Callable[[CreateProblemError], T_Result]
    ) -> T_Result:
        if self.__root__.type == "success":
            return success(self.__root__.value)
        if self.__root__.type == "error":
            return error(self.__root__.value)

    __root__: typing_extensions.Annotated[
        typing.Union[_CreateProblemResponse.Success, _CreateProblemResponse.Error], pydantic.Field(discriminator="type")
    ]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @CreateProblemResponse.Validators.validate
            def validate(value: typing.Union[_CreateProblemResponse.Success, _CreateProblemResponse.Error]) -> typing.Union[_CreateProblemResponse.Success, _CreateProblemResponse.Error]:
                ...
        """

        _validators: typing.ClassVar[
            typing.List[
                typing.Callable[
                    [typing.Union[_CreateProblemResponse.Success, _CreateProblemResponse.Error]],
                    typing.Union[_CreateProblemResponse.Success, _CreateProblemResponse.Error],
                ]
            ]
        ] = []

        @classmethod
        def validate(
            cls,
            validator: typing.Callable[
                [typing.Union[_CreateProblemResponse.Success, _CreateProblemResponse.Error]],
                typing.Union[_CreateProblemResponse.Success, _CreateProblemResponse.Error],
            ],
        ) -> None:
            cls._validators.append(validator)

    @pydantic.root_validator(pre=False)
    def _validate(cls, values: typing.Dict[str, typing.Any]) -> typing.Dict[str, typing.Any]:
        value = typing.cast(
            typing.Union[_CreateProblemResponse.Success, _CreateProblemResponse.Error], values.get("__root__")
        )
        for validator in CreateProblemResponse.Validators._validators:
            value = validator(value)
        return {**values, "__root__": value}

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        extra = pydantic.Extra.forbid
        json_encoders = {dt.datetime: serialize_datetime}


class _CreateProblemResponse:
    class Success(pydantic.BaseModel):
        type: typing_extensions.Literal["success"]
        value: ProblemId

    class Error(pydantic.BaseModel):
        type: typing_extensions.Literal["error"]
        value: CreateProblemError


CreateProblemResponse.update_forward_refs()
