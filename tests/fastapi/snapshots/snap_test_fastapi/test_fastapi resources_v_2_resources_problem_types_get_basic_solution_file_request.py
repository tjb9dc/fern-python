# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

import pydantic
import typing_extensions

from ......core.datetime_utils import serialize_datetime
from .non_void_function_signature import NonVoidFunctionSignature


class GetBasicSolutionFileRequest(pydantic.BaseModel):
    method_name: str = pydantic.Field(alias="methodName")
    signature: NonVoidFunctionSignature

    class Partial(typing_extensions.TypedDict):
        method_name: typing_extensions.NotRequired[str]
        signature: typing_extensions.NotRequired[NonVoidFunctionSignature]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @GetBasicSolutionFileRequest.Validators.root()
            def validate(values: GetBasicSolutionFileRequest.Partial) -> GetBasicSolutionFileRequest.Partial:
                ...

            @GetBasicSolutionFileRequest.Validators.field("method_name")
            def validate_method_name(method_name: str, values: GetBasicSolutionFileRequest.Partial) -> str:
                ...

            @GetBasicSolutionFileRequest.Validators.field("signature")
            def validate_signature(signature: NonVoidFunctionSignature, values: GetBasicSolutionFileRequest.Partial) -> NonVoidFunctionSignature:
                ...
        """

        _pre_validators: typing.ClassVar[typing.List[GetBasicSolutionFileRequest.Validators._PreRootValidator]] = []
        _post_validators: typing.ClassVar[typing.List[GetBasicSolutionFileRequest.Validators._RootValidator]] = []
        _method_name_pre_validators: typing.ClassVar[
            typing.List[GetBasicSolutionFileRequest.Validators.PreMethodNameValidator]
        ] = []
        _method_name_post_validators: typing.ClassVar[
            typing.List[GetBasicSolutionFileRequest.Validators.MethodNameValidator]
        ] = []
        _signature_pre_validators: typing.ClassVar[
            typing.List[GetBasicSolutionFileRequest.Validators.PreSignatureValidator]
        ] = []
        _signature_post_validators: typing.ClassVar[
            typing.List[GetBasicSolutionFileRequest.Validators.SignatureValidator]
        ] = []

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [GetBasicSolutionFileRequest.Validators._RootValidator],
            GetBasicSolutionFileRequest.Validators._RootValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [GetBasicSolutionFileRequest.Validators._PreRootValidator],
            GetBasicSolutionFileRequest.Validators._PreRootValidator,
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
            cls, field_name: typing_extensions.Literal["method_name"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [GetBasicSolutionFileRequest.Validators.PreMethodNameValidator],
            GetBasicSolutionFileRequest.Validators.PreMethodNameValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["method_name"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [GetBasicSolutionFileRequest.Validators.MethodNameValidator],
            GetBasicSolutionFileRequest.Validators.MethodNameValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["signature"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [GetBasicSolutionFileRequest.Validators.PreSignatureValidator],
            GetBasicSolutionFileRequest.Validators.PreSignatureValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["signature"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [GetBasicSolutionFileRequest.Validators.SignatureValidator],
            GetBasicSolutionFileRequest.Validators.SignatureValidator,
        ]:
            ...

        @classmethod
        def field(cls, field_name: str, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "method_name":
                    if pre:
                        cls._method_name_pre_validators.append(validator)
                    else:
                        cls._method_name_post_validators.append(validator)
                if field_name == "signature":
                    if pre:
                        cls._signature_pre_validators.append(validator)
                    else:
                        cls._signature_post_validators.append(validator)
                return validator

            return decorator

        class PreMethodNameValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: GetBasicSolutionFileRequest.Partial) -> typing.Any:
                ...

        class MethodNameValidator(typing_extensions.Protocol):
            def __call__(self, __v: str, __values: GetBasicSolutionFileRequest.Partial) -> str:
                ...

        class PreSignatureValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: GetBasicSolutionFileRequest.Partial) -> typing.Any:
                ...

        class SignatureValidator(typing_extensions.Protocol):
            def __call__(
                self, __v: NonVoidFunctionSignature, __values: GetBasicSolutionFileRequest.Partial
            ) -> NonVoidFunctionSignature:
                ...

        class _PreRootValidator(typing_extensions.Protocol):
            def __call__(self, __values: typing.Any) -> typing.Any:
                ...

        class _RootValidator(typing_extensions.Protocol):
            def __call__(self, __values: GetBasicSolutionFileRequest.Partial) -> GetBasicSolutionFileRequest.Partial:
                ...

    @pydantic.root_validator(pre=True)
    def _pre_validate_v_2_get_basic_solution_file_request(
        cls, values: GetBasicSolutionFileRequest.Partial
    ) -> GetBasicSolutionFileRequest.Partial:
        for validator in GetBasicSolutionFileRequest.Validators._pre_validators:
            values = validator(values)
        return values

    @pydantic.root_validator(pre=False)
    def _post_validate_v_2_get_basic_solution_file_request(
        cls, values: GetBasicSolutionFileRequest.Partial
    ) -> GetBasicSolutionFileRequest.Partial:
        for validator in GetBasicSolutionFileRequest.Validators._post_validators:
            values = validator(values)
        return values

    @pydantic.validator("method_name", pre=True)
    def _pre_validate_method_name(cls, v: str, values: GetBasicSolutionFileRequest.Partial) -> str:
        for validator in GetBasicSolutionFileRequest.Validators._method_name_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("method_name", pre=False)
    def _post_validate_method_name(cls, v: str, values: GetBasicSolutionFileRequest.Partial) -> str:
        for validator in GetBasicSolutionFileRequest.Validators._method_name_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("signature", pre=True)
    def _pre_validate_signature(
        cls, v: NonVoidFunctionSignature, values: GetBasicSolutionFileRequest.Partial
    ) -> NonVoidFunctionSignature:
        for validator in GetBasicSolutionFileRequest.Validators._signature_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("signature", pre=False)
    def _post_validate_signature(
        cls, v: NonVoidFunctionSignature, values: GetBasicSolutionFileRequest.Partial
    ) -> NonVoidFunctionSignature:
        for validator in GetBasicSolutionFileRequest.Validators._signature_post_validators:
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
        extra = pydantic.Extra.forbid
        json_encoders = {dt.datetime: serialize_datetime}
