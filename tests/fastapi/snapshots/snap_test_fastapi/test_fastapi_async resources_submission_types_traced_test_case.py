# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

import pydantic
import typing_extensions

from ....core.datetime_utils import serialize_datetime
from .test_case_result_with_stdout import TestCaseResultWithStdout


class TracedTestCase(pydantic.BaseModel):
    result: TestCaseResultWithStdout
    trace_responses_size: int = pydantic.Field(alias="traceResponsesSize")

    class Partial(typing_extensions.TypedDict):
        result: typing_extensions.NotRequired[TestCaseResultWithStdout]
        trace_responses_size: typing_extensions.NotRequired[int]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @TracedTestCase.Validators.root()
            def validate(values: TracedTestCase.Partial) -> TracedTestCase.Partial:
                ...

            @TracedTestCase.Validators.field("result")
            def validate_result(result: TestCaseResultWithStdout, values: TracedTestCase.Partial) -> TestCaseResultWithStdout:
                ...

            @TracedTestCase.Validators.field("trace_responses_size")
            def validate_trace_responses_size(trace_responses_size: int, values: TracedTestCase.Partial) -> int:
                ...
        """

        _pre_validators: typing.ClassVar[typing.List[TracedTestCase.Validators._PreRootValidator]] = []
        _post_validators: typing.ClassVar[typing.List[TracedTestCase.Validators._RootValidator]] = []
        _result_pre_validators: typing.ClassVar[typing.List[TracedTestCase.Validators.PreResultValidator]] = []
        _result_post_validators: typing.ClassVar[typing.List[TracedTestCase.Validators.ResultValidator]] = []
        _trace_responses_size_pre_validators: typing.ClassVar[
            typing.List[TracedTestCase.Validators.PreTraceResponsesSizeValidator]
        ] = []
        _trace_responses_size_post_validators: typing.ClassVar[
            typing.List[TracedTestCase.Validators.TraceResponsesSizeValidator]
        ] = []

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[[TracedTestCase.Validators._RootValidator], TracedTestCase.Validators._RootValidator]:
            ...

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [TracedTestCase.Validators._PreRootValidator], TracedTestCase.Validators._PreRootValidator
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
            cls, field_name: typing_extensions.Literal["result"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [TracedTestCase.Validators.PreResultValidator], TracedTestCase.Validators.PreResultValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["result"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[[TracedTestCase.Validators.ResultValidator], TracedTestCase.Validators.ResultValidator]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["trace_responses_size"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [TracedTestCase.Validators.PreTraceResponsesSizeValidator],
            TracedTestCase.Validators.PreTraceResponsesSizeValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls,
            field_name: typing_extensions.Literal["trace_responses_size"],
            *,
            pre: typing_extensions.Literal[False] = False,
        ) -> typing.Callable[
            [TracedTestCase.Validators.TraceResponsesSizeValidator],
            TracedTestCase.Validators.TraceResponsesSizeValidator,
        ]:
            ...

        @classmethod
        def field(cls, field_name: str, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "result":
                    if pre:
                        cls._result_pre_validators.append(validator)
                    else:
                        cls._result_post_validators.append(validator)
                if field_name == "trace_responses_size":
                    if pre:
                        cls._trace_responses_size_pre_validators.append(validator)
                    else:
                        cls._trace_responses_size_post_validators.append(validator)
                return validator

            return decorator

        class PreResultValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: TracedTestCase.Partial) -> typing.Any:
                ...

        class ResultValidator(typing_extensions.Protocol):
            def __call__(
                self, __v: TestCaseResultWithStdout, __values: TracedTestCase.Partial
            ) -> TestCaseResultWithStdout:
                ...

        class PreTraceResponsesSizeValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: TracedTestCase.Partial) -> typing.Any:
                ...

        class TraceResponsesSizeValidator(typing_extensions.Protocol):
            def __call__(self, __v: int, __values: TracedTestCase.Partial) -> int:
                ...

        class _PreRootValidator(typing_extensions.Protocol):
            def __call__(self, __values: typing.Any) -> typing.Any:
                ...

        class _RootValidator(typing_extensions.Protocol):
            def __call__(self, __values: TracedTestCase.Partial) -> TracedTestCase.Partial:
                ...

    @pydantic.root_validator(pre=True)
    def _pre_validate_traced_test_case(cls, values: TracedTestCase.Partial) -> TracedTestCase.Partial:
        for validator in TracedTestCase.Validators._pre_validators:
            values = validator(values)
        return values

    @pydantic.root_validator(pre=False)
    def _post_validate_traced_test_case(cls, values: TracedTestCase.Partial) -> TracedTestCase.Partial:
        for validator in TracedTestCase.Validators._post_validators:
            values = validator(values)
        return values

    @pydantic.validator("result", pre=True)
    def _pre_validate_result(
        cls, v: TestCaseResultWithStdout, values: TracedTestCase.Partial
    ) -> TestCaseResultWithStdout:
        for validator in TracedTestCase.Validators._result_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("result", pre=False)
    def _post_validate_result(
        cls, v: TestCaseResultWithStdout, values: TracedTestCase.Partial
    ) -> TestCaseResultWithStdout:
        for validator in TracedTestCase.Validators._result_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("trace_responses_size", pre=True)
    def _pre_validate_trace_responses_size(cls, v: int, values: TracedTestCase.Partial) -> int:
        for validator in TracedTestCase.Validators._trace_responses_size_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("trace_responses_size", pre=False)
    def _post_validate_trace_responses_size(cls, v: int, values: TracedTestCase.Partial) -> int:
        for validator in TracedTestCase.Validators._trace_responses_size_post_validators:
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