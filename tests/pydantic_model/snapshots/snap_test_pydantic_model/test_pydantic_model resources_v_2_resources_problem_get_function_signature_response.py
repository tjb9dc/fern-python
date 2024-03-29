# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

import pydantic
import typing_extensions

from .....core.datetime_utils import serialize_datetime
from ....commons.language import Language


class GetFunctionSignatureResponse(pydantic.BaseModel):
    function_by_language: typing.Dict[Language, str] = pydantic.Field(alias="functionByLanguage")

    class Partial(typing_extensions.TypedDict):
        function_by_language: typing_extensions.NotRequired[typing.Dict[Language, str]]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @GetFunctionSignatureResponse.Validators.root()
            def validate(values: GetFunctionSignatureResponse.Partial) -> GetFunctionSignatureResponse.Partial:
                ...

            @GetFunctionSignatureResponse.Validators.field("function_by_language")
            def validate_function_by_language(function_by_language: typing.Dict[Language, str], values: GetFunctionSignatureResponse.Partial) -> typing.Dict[Language, str]:
                ...
        """

        _pre_validators: typing.ClassVar[typing.List[GetFunctionSignatureResponse.Validators._PreRootValidator]] = []
        _post_validators: typing.ClassVar[typing.List[GetFunctionSignatureResponse.Validators._RootValidator]] = []
        _function_by_language_pre_validators: typing.ClassVar[
            typing.List[GetFunctionSignatureResponse.Validators.PreFunctionByLanguageValidator]
        ] = []
        _function_by_language_post_validators: typing.ClassVar[
            typing.List[GetFunctionSignatureResponse.Validators.FunctionByLanguageValidator]
        ] = []

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [GetFunctionSignatureResponse.Validators._RootValidator],
            GetFunctionSignatureResponse.Validators._RootValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [GetFunctionSignatureResponse.Validators._PreRootValidator],
            GetFunctionSignatureResponse.Validators._PreRootValidator,
        ]:
            ...

        @classmethod
        def root(cls, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if pre:
                    cls._pre_validators.append(validator)
                else:
                    cls._post_validators.append(validator)
                return validator

            return decorator

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["function_by_language"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [GetFunctionSignatureResponse.Validators.PreFunctionByLanguageValidator],
            GetFunctionSignatureResponse.Validators.PreFunctionByLanguageValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls,
            field_name: typing_extensions.Literal["function_by_language"],
            *,
            pre: typing_extensions.Literal[False] = False,
        ) -> typing.Callable[
            [GetFunctionSignatureResponse.Validators.FunctionByLanguageValidator],
            GetFunctionSignatureResponse.Validators.FunctionByLanguageValidator,
        ]:
            ...

        @classmethod
        def field(cls, field_name: str, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "function_by_language":
                    if pre:
                        cls._function_by_language_pre_validators.append(validator)
                    else:
                        cls._function_by_language_post_validators.append(validator)
                return validator

            return decorator

        class PreFunctionByLanguageValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: GetFunctionSignatureResponse.Partial) -> typing.Any:
                ...

        class FunctionByLanguageValidator(typing_extensions.Protocol):
            def __call__(
                self, __v: typing.Dict[Language, str], __values: GetFunctionSignatureResponse.Partial
            ) -> typing.Dict[Language, str]:
                ...

        class _PreRootValidator(typing_extensions.Protocol):
            def __call__(self, __values: typing.Any) -> typing.Any:
                ...

        class _RootValidator(typing_extensions.Protocol):
            def __call__(self, __values: GetFunctionSignatureResponse.Partial) -> GetFunctionSignatureResponse.Partial:
                ...

    @pydantic.root_validator(pre=True)
    def _pre_validate_v_2_get_function_signature_response(
        cls, values: GetFunctionSignatureResponse.Partial
    ) -> GetFunctionSignatureResponse.Partial:
        for validator in GetFunctionSignatureResponse.Validators._pre_validators:
            values = validator(values)
        return values

    @pydantic.root_validator(pre=False)
    def _post_validate_v_2_get_function_signature_response(
        cls, values: GetFunctionSignatureResponse.Partial
    ) -> GetFunctionSignatureResponse.Partial:
        for validator in GetFunctionSignatureResponse.Validators._post_validators:
            values = validator(values)
        return values

    @pydantic.validator("function_by_language", pre=True)
    def _pre_validate_function_by_language(
        cls, v: typing.Dict[Language, str], values: GetFunctionSignatureResponse.Partial
    ) -> typing.Dict[Language, str]:
        for validator in GetFunctionSignatureResponse.Validators._function_by_language_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("function_by_language", pre=False)
    def _post_validate_function_by_language(
        cls, v: typing.Dict[Language, str], values: GetFunctionSignatureResponse.Partial
    ) -> typing.Dict[Language, str]:
        for validator in GetFunctionSignatureResponse.Validators._function_by_language_post_validators:
            v = validator(v, values)
        return v

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        allow_population_by_field_name = True
        json_encoders = {dt.datetime: serialize_datetime}
