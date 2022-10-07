import typing

import pydantic
import typing_extensions

from ..commons.file_info import FileInfo


class WorkspaceFiles(pydantic.BaseModel):
    main_file: FileInfo = pydantic.Field(alias="mainFile")
    read_only_files: typing.List[FileInfo] = pydantic.Field(alias="readOnlyFiles")

    @pydantic.validator("main_file")
    def _validate_main_file(cls, main_file: FileInfo) -> FileInfo:
        for validator in WorkspaceFiles.Validators._main_file:
            main_file = validator(main_file)
        return main_file

    @pydantic.validator("read_only_files")
    def _validate_read_only_files(cls, read_only_files: typing.List[FileInfo]) -> typing.List[FileInfo]:
        for validator in WorkspaceFiles.Validators._read_only_files:
            read_only_files = validator(read_only_files)
        return read_only_files

    class Validators:
        _main_file: typing.ClassVar[typing.List[typing.Callable[[FileInfo], FileInfo]]] = []
        _read_only_files: typing.ClassVar[
            typing.List[typing.Callable[[typing.List[FileInfo]], typing.List[FileInfo]]]
        ] = []

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["main_file"]
        ) -> typing.Callable[[typing.Callable[[FileInfo], FileInfo]], typing.Callable[[FileInfo], FileInfo]]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["read_only_files"]
        ) -> typing.Callable[
            [typing.Callable[[typing.List[FileInfo]], typing.List[FileInfo]]],
            typing.Callable[[typing.List[FileInfo]], typing.List[FileInfo]],
        ]:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "main_file":
                    cls._main_file.append(validator)
                elif field_name == "read_only_files":
                    cls._read_only_files.append(validator)
                else:
                    raise RuntimeError("Field does not exist on WorkspaceFiles: " + field_name)

                return validator

            return decorator

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    class Config:
        frozen = True
        allow_population_by_field_name = True