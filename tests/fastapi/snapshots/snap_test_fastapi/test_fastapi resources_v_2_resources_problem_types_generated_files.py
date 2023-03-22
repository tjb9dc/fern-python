# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

import pydantic
import typing_extensions

from ......core.datetime_utils import serialize_datetime
from .....commons.types.language import Language
from .files import Files


class GeneratedFiles(pydantic.BaseModel):
    generated_test_case_files: typing.Dict[Language, Files] = pydantic.Field(alias="generatedTestCaseFiles")
    generated_template_files: typing.Dict[Language, Files] = pydantic.Field(alias="generatedTemplateFiles")
    other: typing.Dict[Language, Files]

    class Partial(typing_extensions.TypedDict):
        generated_test_case_files: typing_extensions.NotRequired[typing.Dict[Language, Files]]
        generated_template_files: typing_extensions.NotRequired[typing.Dict[Language, Files]]
        other: typing_extensions.NotRequired[typing.Dict[Language, Files]]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @GeneratedFiles.Validators.root()
            def validate(values: GeneratedFiles.Partial) -> GeneratedFiles.Partial:
                ...

            @GeneratedFiles.Validators.field("generated_test_case_files")
            def validate_generated_test_case_files(generated_test_case_files: typing.Dict[Language, Files], values: GeneratedFiles.Partial) -> typing.Dict[Language, Files]:
                ...

            @GeneratedFiles.Validators.field("generated_template_files")
            def validate_generated_template_files(generated_template_files: typing.Dict[Language, Files], values: GeneratedFiles.Partial) -> typing.Dict[Language, Files]:
                ...

            @GeneratedFiles.Validators.field("other")
            def validate_other(other: typing.Dict[Language, Files], values: GeneratedFiles.Partial) -> typing.Dict[Language, Files]:
                ...
        """

        _pre_validators: typing.ClassVar[typing.List[GeneratedFiles.Validators._PreRootValidator]] = []
        _post_validators: typing.ClassVar[typing.List[GeneratedFiles.Validators._RootValidator]] = []
        _generated_test_case_files_pre_validators: typing.ClassVar[
            typing.List[GeneratedFiles.Validators.PreGeneratedTestCaseFilesValidator]
        ] = []
        _generated_test_case_files_post_validators: typing.ClassVar[
            typing.List[GeneratedFiles.Validators.GeneratedTestCaseFilesValidator]
        ] = []
        _generated_template_files_pre_validators: typing.ClassVar[
            typing.List[GeneratedFiles.Validators.PreGeneratedTemplateFilesValidator]
        ] = []
        _generated_template_files_post_validators: typing.ClassVar[
            typing.List[GeneratedFiles.Validators.GeneratedTemplateFilesValidator]
        ] = []
        _other_pre_validators: typing.ClassVar[typing.List[GeneratedFiles.Validators.PreOtherValidator]] = []
        _other_post_validators: typing.ClassVar[typing.List[GeneratedFiles.Validators.OtherValidator]] = []

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[[GeneratedFiles.Validators._RootValidator], GeneratedFiles.Validators._RootValidator]:
            ...

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [GeneratedFiles.Validators._PreRootValidator], GeneratedFiles.Validators._PreRootValidator
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
            cls,
            field_name: typing_extensions.Literal["generated_test_case_files"],
            *,
            pre: typing_extensions.Literal[True],
        ) -> typing.Callable[
            [GeneratedFiles.Validators.PreGeneratedTestCaseFilesValidator],
            GeneratedFiles.Validators.PreGeneratedTestCaseFilesValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls,
            field_name: typing_extensions.Literal["generated_test_case_files"],
            *,
            pre: typing_extensions.Literal[False] = False,
        ) -> typing.Callable[
            [GeneratedFiles.Validators.GeneratedTestCaseFilesValidator],
            GeneratedFiles.Validators.GeneratedTestCaseFilesValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls,
            field_name: typing_extensions.Literal["generated_template_files"],
            *,
            pre: typing_extensions.Literal[True],
        ) -> typing.Callable[
            [GeneratedFiles.Validators.PreGeneratedTemplateFilesValidator],
            GeneratedFiles.Validators.PreGeneratedTemplateFilesValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls,
            field_name: typing_extensions.Literal["generated_template_files"],
            *,
            pre: typing_extensions.Literal[False] = False,
        ) -> typing.Callable[
            [GeneratedFiles.Validators.GeneratedTemplateFilesValidator],
            GeneratedFiles.Validators.GeneratedTemplateFilesValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["other"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [GeneratedFiles.Validators.PreOtherValidator], GeneratedFiles.Validators.PreOtherValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["other"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[[GeneratedFiles.Validators.OtherValidator], GeneratedFiles.Validators.OtherValidator]:
            ...

        @classmethod
        def field(cls, field_name: str, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "generated_test_case_files":
                    if pre:
                        cls._generated_test_case_files_pre_validators.append(validator)
                    else:
                        cls._generated_test_case_files_post_validators.append(validator)
                if field_name == "generated_template_files":
                    if pre:
                        cls._generated_template_files_pre_validators.append(validator)
                    else:
                        cls._generated_template_files_post_validators.append(validator)
                if field_name == "other":
                    if pre:
                        cls._other_pre_validators.append(validator)
                    else:
                        cls._other_post_validators.append(validator)
                return validator

            return decorator

        class PreGeneratedTestCaseFilesValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: GeneratedFiles.Partial) -> typing.Any:
                ...

        class GeneratedTestCaseFilesValidator(typing_extensions.Protocol):
            def __call__(
                self, __v: typing.Dict[Language, Files], __values: GeneratedFiles.Partial
            ) -> typing.Dict[Language, Files]:
                ...

        class PreGeneratedTemplateFilesValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: GeneratedFiles.Partial) -> typing.Any:
                ...

        class GeneratedTemplateFilesValidator(typing_extensions.Protocol):
            def __call__(
                self, __v: typing.Dict[Language, Files], __values: GeneratedFiles.Partial
            ) -> typing.Dict[Language, Files]:
                ...

        class PreOtherValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: GeneratedFiles.Partial) -> typing.Any:
                ...

        class OtherValidator(typing_extensions.Protocol):
            def __call__(
                self, __v: typing.Dict[Language, Files], __values: GeneratedFiles.Partial
            ) -> typing.Dict[Language, Files]:
                ...

        class _PreRootValidator(typing_extensions.Protocol):
            def __call__(self, __values: typing.Any) -> typing.Any:
                ...

        class _RootValidator(typing_extensions.Protocol):
            def __call__(self, __values: GeneratedFiles.Partial) -> GeneratedFiles.Partial:
                ...

    @pydantic.root_validator(pre=True)
    def _pre_validate(cls, values: GeneratedFiles.Partial) -> GeneratedFiles.Partial:
        for validator in GeneratedFiles.Validators._pre_validators:
            values = validator(values)
        return values

    @pydantic.root_validator(pre=False)
    def _post_validate(cls, values: GeneratedFiles.Partial) -> GeneratedFiles.Partial:
        for validator in GeneratedFiles.Validators._post_validators:
            values = validator(values)
        return values

    @pydantic.validator("generated_test_case_files", pre=True)
    def _pre_validate_generated_test_case_files(
        cls, v: typing.Dict[Language, Files], values: GeneratedFiles.Partial
    ) -> typing.Dict[Language, Files]:
        for validator in GeneratedFiles.Validators._generated_test_case_files_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("generated_test_case_files", pre=False)
    def _post_validate_generated_test_case_files(
        cls, v: typing.Dict[Language, Files], values: GeneratedFiles.Partial
    ) -> typing.Dict[Language, Files]:
        for validator in GeneratedFiles.Validators._generated_test_case_files_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("generated_template_files", pre=True)
    def _pre_validate_generated_template_files(
        cls, v: typing.Dict[Language, Files], values: GeneratedFiles.Partial
    ) -> typing.Dict[Language, Files]:
        for validator in GeneratedFiles.Validators._generated_template_files_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("generated_template_files", pre=False)
    def _post_validate_generated_template_files(
        cls, v: typing.Dict[Language, Files], values: GeneratedFiles.Partial
    ) -> typing.Dict[Language, Files]:
        for validator in GeneratedFiles.Validators._generated_template_files_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("other", pre=True)
    def _pre_validate_other(
        cls, v: typing.Dict[Language, Files], values: GeneratedFiles.Partial
    ) -> typing.Dict[Language, Files]:
        for validator in GeneratedFiles.Validators._other_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("other", pre=False)
    def _post_validate_other(
        cls, v: typing.Dict[Language, Files], values: GeneratedFiles.Partial
    ) -> typing.Dict[Language, Files]:
        for validator in GeneratedFiles.Validators._other_post_validators:
            v = validator(v, values)
        return v

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        allow_population_by_field_name = True
        extra = pydantic.Extra.forbid
        json_encoders = {dt.datetime: serialize_datetime}