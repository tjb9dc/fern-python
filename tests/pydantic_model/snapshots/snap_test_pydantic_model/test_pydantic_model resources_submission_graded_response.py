# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

import pydantic
import typing_extensions

from ...core.datetime_utils import serialize_datetime
from .submission_id import SubmissionId
from .test_case_result_with_stdout import TestCaseResultWithStdout


class GradedResponse(pydantic.BaseModel):
    submission_id: SubmissionId = pydantic.Field(alias="submissionId")
    test_cases: typing.Dict[str, TestCaseResultWithStdout] = pydantic.Field(alias="testCases")

    class Partial(typing_extensions.TypedDict):
        submission_id: typing_extensions.NotRequired[SubmissionId]
        test_cases: typing_extensions.NotRequired[typing.Dict[str, TestCaseResultWithStdout]]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @GradedResponse.Validators.root()
            def validate(values: GradedResponse.Partial) -> GradedResponse.Partial:
                ...

            @GradedResponse.Validators.field("submission_id")
            def validate_submission_id(submission_id: SubmissionId, values: GradedResponse.Partial) -> SubmissionId:
                ...

            @GradedResponse.Validators.field("test_cases")
            def validate_test_cases(test_cases: typing.Dict[str, TestCaseResultWithStdout], values: GradedResponse.Partial) -> typing.Dict[str, TestCaseResultWithStdout]:
                ...
        """

        _pre_validators: typing.ClassVar[typing.List[GradedResponse.Validators._PreRootValidator]] = []
        _post_validators: typing.ClassVar[typing.List[GradedResponse.Validators._RootValidator]] = []
        _submission_id_pre_validators: typing.ClassVar[
            typing.List[GradedResponse.Validators.PreSubmissionIdValidator]
        ] = []
        _submission_id_post_validators: typing.ClassVar[
            typing.List[GradedResponse.Validators.SubmissionIdValidator]
        ] = []
        _test_cases_pre_validators: typing.ClassVar[typing.List[GradedResponse.Validators.PreTestCasesValidator]] = []
        _test_cases_post_validators: typing.ClassVar[typing.List[GradedResponse.Validators.TestCasesValidator]] = []

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[[GradedResponse.Validators._RootValidator], GradedResponse.Validators._RootValidator]:
            ...

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [GradedResponse.Validators._PreRootValidator], GradedResponse.Validators._PreRootValidator
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
            cls, field_name: typing_extensions.Literal["submission_id"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [GradedResponse.Validators.PreSubmissionIdValidator], GradedResponse.Validators.PreSubmissionIdValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls,
            field_name: typing_extensions.Literal["submission_id"],
            *,
            pre: typing_extensions.Literal[False] = False,
        ) -> typing.Callable[
            [GradedResponse.Validators.SubmissionIdValidator], GradedResponse.Validators.SubmissionIdValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["test_cases"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [GradedResponse.Validators.PreTestCasesValidator], GradedResponse.Validators.PreTestCasesValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["test_cases"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [GradedResponse.Validators.TestCasesValidator], GradedResponse.Validators.TestCasesValidator
        ]:
            ...

        @classmethod
        def field(cls, field_name: str, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "submission_id":
                    if pre:
                        cls._submission_id_pre_validators.append(validator)
                    else:
                        cls._submission_id_post_validators.append(validator)
                if field_name == "test_cases":
                    if pre:
                        cls._test_cases_pre_validators.append(validator)
                    else:
                        cls._test_cases_post_validators.append(validator)
                return validator

            return decorator

        class PreSubmissionIdValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: GradedResponse.Partial) -> typing.Any:
                ...

        class SubmissionIdValidator(typing_extensions.Protocol):
            def __call__(self, __v: SubmissionId, __values: GradedResponse.Partial) -> SubmissionId:
                ...

        class PreTestCasesValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: GradedResponse.Partial) -> typing.Any:
                ...

        class TestCasesValidator(typing_extensions.Protocol):
            def __call__(
                self, __v: typing.Dict[str, TestCaseResultWithStdout], __values: GradedResponse.Partial
            ) -> typing.Dict[str, TestCaseResultWithStdout]:
                ...

        class _PreRootValidator(typing_extensions.Protocol):
            def __call__(self, __values: typing.Any) -> typing.Any:
                ...

        class _RootValidator(typing_extensions.Protocol):
            def __call__(self, __values: GradedResponse.Partial) -> GradedResponse.Partial:
                ...

    @pydantic.root_validator(pre=True)
    def _pre_validate_graded_response(cls, values: GradedResponse.Partial) -> GradedResponse.Partial:
        for validator in GradedResponse.Validators._pre_validators:
            values = validator(values)
        return values

    @pydantic.root_validator(pre=False)
    def _post_validate_graded_response(cls, values: GradedResponse.Partial) -> GradedResponse.Partial:
        for validator in GradedResponse.Validators._post_validators:
            values = validator(values)
        return values

    @pydantic.validator("submission_id", pre=True)
    def _pre_validate_submission_id(cls, v: SubmissionId, values: GradedResponse.Partial) -> SubmissionId:
        for validator in GradedResponse.Validators._submission_id_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("submission_id", pre=False)
    def _post_validate_submission_id(cls, v: SubmissionId, values: GradedResponse.Partial) -> SubmissionId:
        for validator in GradedResponse.Validators._submission_id_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("test_cases", pre=True)
    def _pre_validate_test_cases(
        cls, v: typing.Dict[str, TestCaseResultWithStdout], values: GradedResponse.Partial
    ) -> typing.Dict[str, TestCaseResultWithStdout]:
        for validator in GradedResponse.Validators._test_cases_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("test_cases", pre=False)
    def _post_validate_test_cases(
        cls, v: typing.Dict[str, TestCaseResultWithStdout], values: GradedResponse.Partial
    ) -> typing.Dict[str, TestCaseResultWithStdout]:
        for validator in GradedResponse.Validators._test_cases_post_validators:
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
