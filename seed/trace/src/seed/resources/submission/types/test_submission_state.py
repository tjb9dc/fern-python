# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ....core.datetime_utils import serialize_datetime
from ...commons.types.problem_id import ProblemId
from ...commons.types.test_case import TestCase
from .test_submission_status import TestSubmissionStatus


class TestSubmissionState(pydantic.BaseModel):
    problem_id: ProblemId = pydantic.Field(alias="problemId")
    default_test_cases: typing.List[TestCase] = pydantic.Field(alias="defaultTestCases")
    custom_test_cases: typing.List[TestCase] = pydantic.Field(alias="customTestCases")
    status: TestSubmissionStatus

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        json_encoders = {dt.datetime: serialize_datetime}