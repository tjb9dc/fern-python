# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import typing_extensions

from ..commons.key_value_pair import KeyValuePair
from ..commons.map_value import MapValue
from ..commons.variable_value import VariableValue
from .test_submission_state import TestSubmissionState
from .workspace_submission_state import WorkspaceSubmissionState


class SubmissionTypeState_Test(TestSubmissionState):
    type: typing_extensions.Literal["test"]

    class Config:
        allow_population_by_field_name = True


class SubmissionTypeState_Workspace(WorkspaceSubmissionState):
    type: typing_extensions.Literal["workspace"]

    class Config:
        allow_population_by_field_name = True


SubmissionTypeState = typing.Union[SubmissionTypeState_Test, SubmissionTypeState_Workspace]
SubmissionTypeState_Test.update_forward_refs(KeyValuePair=KeyValuePair, MapValue=MapValue, VariableValue=VariableValue)
