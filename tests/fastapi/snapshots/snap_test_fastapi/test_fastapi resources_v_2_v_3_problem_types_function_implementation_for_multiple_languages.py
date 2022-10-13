# This file was auto-generated by Fern from our API Definition.

# flake8: noqa
# fmt: off
# isort: skip_file

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from .....commons.types.language import Language
from .function_implementation import FunctionImplementation


class FunctionImplementationForMultipleLanguages(pydantic.BaseModel):
    code_by_language: typing.Dict[Language, FunctionImplementation] = pydantic.Field(alias="codeByLanguage")

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @FunctionImplementationForMultipleLanguages.Validators.field("code_by_language")
            def validate_code_by_language(v: typing.Dict[Language, FunctionImplementation], values: FunctionImplementationForMultipleLanguages.Partial) -> typing.Dict[Language, FunctionImplementation]:
                ...
        """

        _code_by_language_validators: typing.ClassVar[
            typing.List[FunctionImplementationForMultipleLanguages.Validators.CodeByLanguageValidator]
        ] = []

        @typing.overload  # type: ignore
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["code_by_language"]
        ) -> typing.Callable[
            [FunctionImplementationForMultipleLanguages.Validators.CodeByLanguageValidator],
            FunctionImplementationForMultipleLanguages.Validators.CodeByLanguageValidator,
        ]:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "code_by_language":
                    cls._code_by_language_validators.append(validator)
                return validator

            return decorator

        class CodeByLanguageValidator(typing_extensions.Protocol):
            def __call__(
                self,
                v: typing.Dict[Language, FunctionImplementation],
                *,
                values: FunctionImplementationForMultipleLanguages.Partial,
            ) -> typing.Dict[Language, FunctionImplementation]:
                ...

    @pydantic.validator("code_by_language")
    def _validate_code_by_language(
        cls,
        v: typing.Dict[Language, FunctionImplementation],
        values: FunctionImplementationForMultipleLanguages.Partial,
    ) -> typing.Dict[Language, FunctionImplementation]:
        for validator in FunctionImplementationForMultipleLanguages.Validators._code_by_language_validators:
            v = validator(v, values=values)
        return v

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Partial(typing.TypedDict):
        code_by_language: typing_extensions.NotRequired[typing.Dict[Language, FunctionImplementation]]

    class Config:
        frozen = True
        allow_population_by_field_name = True