# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

import pydantic
import typing_extensions

from ....core.datetime_utils import serialize_datetime
from ...v_2.resources.problem.types.test_case_id import TestCaseId
from .test_case_grade import TestCaseGrade


class GradedTestCaseUpdate(pydantic.BaseModel):
    test_case_id: TestCaseId = pydantic.Field(alias="testCaseId")
    grade: TestCaseGrade

    class Partial(typing_extensions.TypedDict):
        test_case_id: typing_extensions.NotRequired[TestCaseId]
        grade: typing_extensions.NotRequired[TestCaseGrade]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @GradedTestCaseUpdate.Validators.root()
            def validate(values: GradedTestCaseUpdate.Partial) -> GradedTestCaseUpdate.Partial:
                ...

            @GradedTestCaseUpdate.Validators.field("test_case_id")
            def validate_test_case_id(test_case_id: TestCaseId, values: GradedTestCaseUpdate.Partial) -> TestCaseId:
                ...

            @GradedTestCaseUpdate.Validators.field("grade")
            def validate_grade(grade: TestCaseGrade, values: GradedTestCaseUpdate.Partial) -> TestCaseGrade:
                ...
        """

        _pre_validators: typing.ClassVar[typing.List[GradedTestCaseUpdate.Validators._PreRootValidator]] = []
        _post_validators: typing.ClassVar[typing.List[GradedTestCaseUpdate.Validators._RootValidator]] = []
        _test_case_id_pre_validators: typing.ClassVar[
            typing.List[GradedTestCaseUpdate.Validators.PreTestCaseIdValidator]
        ] = []
        _test_case_id_post_validators: typing.ClassVar[
            typing.List[GradedTestCaseUpdate.Validators.TestCaseIdValidator]
        ] = []
        _grade_pre_validators: typing.ClassVar[typing.List[GradedTestCaseUpdate.Validators.PreGradeValidator]] = []
        _grade_post_validators: typing.ClassVar[typing.List[GradedTestCaseUpdate.Validators.GradeValidator]] = []

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [GradedTestCaseUpdate.Validators._RootValidator], GradedTestCaseUpdate.Validators._RootValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [GradedTestCaseUpdate.Validators._PreRootValidator], GradedTestCaseUpdate.Validators._PreRootValidator
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
            cls, field_name: typing_extensions.Literal["test_case_id"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [GradedTestCaseUpdate.Validators.PreTestCaseIdValidator],
            GradedTestCaseUpdate.Validators.PreTestCaseIdValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["test_case_id"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [GradedTestCaseUpdate.Validators.TestCaseIdValidator], GradedTestCaseUpdate.Validators.TestCaseIdValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["grade"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [GradedTestCaseUpdate.Validators.PreGradeValidator], GradedTestCaseUpdate.Validators.PreGradeValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["grade"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [GradedTestCaseUpdate.Validators.GradeValidator], GradedTestCaseUpdate.Validators.GradeValidator
        ]:
            ...

        @classmethod
        def field(cls, field_name: str, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "test_case_id":
                    if pre:
                        cls._test_case_id_pre_validators.append(validator)
                    else:
                        cls._test_case_id_post_validators.append(validator)
                if field_name == "grade":
                    if pre:
                        cls._grade_pre_validators.append(validator)
                    else:
                        cls._grade_post_validators.append(validator)
                return validator

            return decorator

        class PreTestCaseIdValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: GradedTestCaseUpdate.Partial) -> typing.Any:
                ...

        class TestCaseIdValidator(typing_extensions.Protocol):
            def __call__(self, __v: TestCaseId, __values: GradedTestCaseUpdate.Partial) -> TestCaseId:
                ...

        class PreGradeValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: GradedTestCaseUpdate.Partial) -> typing.Any:
                ...

        class GradeValidator(typing_extensions.Protocol):
            def __call__(self, __v: TestCaseGrade, __values: GradedTestCaseUpdate.Partial) -> TestCaseGrade:
                ...

        class _PreRootValidator(typing_extensions.Protocol):
            def __call__(self, __values: typing.Any) -> typing.Any:
                ...

        class _RootValidator(typing_extensions.Protocol):
            def __call__(self, __values: GradedTestCaseUpdate.Partial) -> GradedTestCaseUpdate.Partial:
                ...

    @pydantic.root_validator(pre=True)
    def _pre_validate_graded_test_case_update(
        cls, values: GradedTestCaseUpdate.Partial
    ) -> GradedTestCaseUpdate.Partial:
        for validator in GradedTestCaseUpdate.Validators._pre_validators:
            values = validator(values)
        return values

    @pydantic.root_validator(pre=False)
    def _post_validate_graded_test_case_update(
        cls, values: GradedTestCaseUpdate.Partial
    ) -> GradedTestCaseUpdate.Partial:
        for validator in GradedTestCaseUpdate.Validators._post_validators:
            values = validator(values)
        return values

    @pydantic.validator("test_case_id", pre=True)
    def _pre_validate_test_case_id(cls, v: TestCaseId, values: GradedTestCaseUpdate.Partial) -> TestCaseId:
        for validator in GradedTestCaseUpdate.Validators._test_case_id_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("test_case_id", pre=False)
    def _post_validate_test_case_id(cls, v: TestCaseId, values: GradedTestCaseUpdate.Partial) -> TestCaseId:
        for validator in GradedTestCaseUpdate.Validators._test_case_id_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("grade", pre=True)
    def _pre_validate_grade(cls, v: TestCaseGrade, values: GradedTestCaseUpdate.Partial) -> TestCaseGrade:
        for validator in GradedTestCaseUpdate.Validators._grade_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("grade", pre=False)
    def _post_validate_grade(cls, v: TestCaseGrade, values: GradedTestCaseUpdate.Partial) -> TestCaseGrade:
        for validator in GradedTestCaseUpdate.Validators._grade_post_validators:
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