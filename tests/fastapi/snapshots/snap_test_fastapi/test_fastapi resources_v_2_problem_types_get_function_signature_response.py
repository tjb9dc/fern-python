# This file was auto-generated by Fern from our API Definition.

# flake8: noqa
# fmt: off
# isort: skip_file

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from ....commons.types.language import Language


class GetFunctionSignatureResponse(pydantic.BaseModel):
    function_by_language: typing.Dict[Language, str] = pydantic.Field(alias="functionByLanguage")

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @GetFunctionSignatureResponse.Validators.field("function_by_language")
            def validate_function_by_language(v: typing.Dict[Language, str], values: GetFunctionSignatureResponse.Partial) -> typing.Dict[Language, str]:
                ...
        """

        _function_by_language_validators: typing.ClassVar[
            typing.List[GetFunctionSignatureResponse.Validators.FunctionByLanguageValidator]
        ] = []

        @typing.overload  # type: ignore
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["function_by_language"]
        ) -> typing.Callable[
            [GetFunctionSignatureResponse.Validators.FunctionByLanguageValidator],
            GetFunctionSignatureResponse.Validators.FunctionByLanguageValidator,
        ]:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "function_by_language":
                    cls._function_by_language_validators.append(validator)
                return validator

            return decorator

        class FunctionByLanguageValidator(typing_extensions.Protocol):
            def __call__(
                self, v: typing.Dict[Language, str], *, values: GetFunctionSignatureResponse.Partial
            ) -> typing.Dict[Language, str]:
                ...

    @pydantic.validator("function_by_language")
    def _validate_function_by_language(
        cls, v: typing.Dict[Language, str], values: GetFunctionSignatureResponse.Partial
    ) -> typing.Dict[Language, str]:
        for validator in GetFunctionSignatureResponse.Validators._function_by_language_validators:
            v = validator(v, values=values)
        return v

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Partial(typing.TypedDict):
        function_by_language: typing_extensions.NotRequired[typing.Dict[Language, str]]

    class Config:
        frozen = True
        allow_population_by_field_name = True