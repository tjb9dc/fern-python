# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

import pydantic
import typing_extensions

from ....core.datetime_utils import serialize_datetime


class TracedFile(pydantic.BaseModel):
    filename: str
    directory: str

    class Partial(typing_extensions.TypedDict):
        filename: typing_extensions.NotRequired[str]
        directory: typing_extensions.NotRequired[str]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @TracedFile.Validators.root()
            def validate(values: TracedFile.Partial) -> TracedFile.Partial:
                ...

            @TracedFile.Validators.field("filename")
            def validate_filename(filename: str, values: TracedFile.Partial) -> str:
                ...

            @TracedFile.Validators.field("directory")
            def validate_directory(directory: str, values: TracedFile.Partial) -> str:
                ...
        """

        _pre_validators: typing.ClassVar[typing.List[TracedFile.Validators._PreRootValidator]] = []
        _post_validators: typing.ClassVar[typing.List[TracedFile.Validators._RootValidator]] = []
        _filename_pre_validators: typing.ClassVar[typing.List[TracedFile.Validators.PreFilenameValidator]] = []
        _filename_post_validators: typing.ClassVar[typing.List[TracedFile.Validators.FilenameValidator]] = []
        _directory_pre_validators: typing.ClassVar[typing.List[TracedFile.Validators.PreDirectoryValidator]] = []
        _directory_post_validators: typing.ClassVar[typing.List[TracedFile.Validators.DirectoryValidator]] = []

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[[TracedFile.Validators._RootValidator], TracedFile.Validators._RootValidator]:
            ...

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[[TracedFile.Validators._PreRootValidator], TracedFile.Validators._PreRootValidator]:
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
            cls, field_name: typing_extensions.Literal["filename"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[[TracedFile.Validators.PreFilenameValidator], TracedFile.Validators.PreFilenameValidator]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["filename"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[[TracedFile.Validators.FilenameValidator], TracedFile.Validators.FilenameValidator]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["directory"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [TracedFile.Validators.PreDirectoryValidator], TracedFile.Validators.PreDirectoryValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["directory"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[[TracedFile.Validators.DirectoryValidator], TracedFile.Validators.DirectoryValidator]:
            ...

        @classmethod
        def field(cls, field_name: str, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "filename":
                    if pre:
                        cls._filename_pre_validators.append(validator)
                    else:
                        cls._filename_post_validators.append(validator)
                if field_name == "directory":
                    if pre:
                        cls._directory_pre_validators.append(validator)
                    else:
                        cls._directory_post_validators.append(validator)
                return validator

            return decorator

        class PreFilenameValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: TracedFile.Partial) -> typing.Any:
                ...

        class FilenameValidator(typing_extensions.Protocol):
            def __call__(self, __v: str, __values: TracedFile.Partial) -> str:
                ...

        class PreDirectoryValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: TracedFile.Partial) -> typing.Any:
                ...

        class DirectoryValidator(typing_extensions.Protocol):
            def __call__(self, __v: str, __values: TracedFile.Partial) -> str:
                ...

        class _PreRootValidator(typing_extensions.Protocol):
            def __call__(self, __values: typing.Any) -> typing.Any:
                ...

        class _RootValidator(typing_extensions.Protocol):
            def __call__(self, __values: TracedFile.Partial) -> TracedFile.Partial:
                ...

    @pydantic.root_validator(pre=True)
    def _pre_validate_traced_file(cls, values: TracedFile.Partial) -> TracedFile.Partial:
        for validator in TracedFile.Validators._pre_validators:
            values = validator(values)
        return values

    @pydantic.root_validator(pre=False)
    def _post_validate_traced_file(cls, values: TracedFile.Partial) -> TracedFile.Partial:
        for validator in TracedFile.Validators._post_validators:
            values = validator(values)
        return values

    @pydantic.validator("filename", pre=True)
    def _pre_validate_filename(cls, v: str, values: TracedFile.Partial) -> str:
        for validator in TracedFile.Validators._filename_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("filename", pre=False)
    def _post_validate_filename(cls, v: str, values: TracedFile.Partial) -> str:
        for validator in TracedFile.Validators._filename_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("directory", pre=True)
    def _pre_validate_directory(cls, v: str, values: TracedFile.Partial) -> str:
        for validator in TracedFile.Validators._directory_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("directory", pre=False)
    def _post_validate_directory(cls, v: str, values: TracedFile.Partial) -> str:
        for validator in TracedFile.Validators._directory_post_validators:
            v = validator(v, values)
        return v

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        extra = pydantic.Extra.forbid
        json_encoders = {dt.datetime: serialize_datetime}
