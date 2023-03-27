# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from ...commons.types.key_value_pair import KeyValuePair
from ...commons.types.map_value import MapValue
from ...commons.types.variable_value import VariableValue
from .building_executor_response import BuildingExecutorResponse
from .errored_response import ErroredResponse
from .finished_response import FinishedResponse
from .graded_response import GradedResponse
from .graded_response_v_2 import GradedResponseV2
from .invalid_request_response import InvalidRequestResponse
from .recorded_response_notification import RecordedResponseNotification
from .recording_response_notification import RecordingResponseNotification
from .running_response import RunningResponse
from .stopped_response import StoppedResponse
from .workspace_ran_response import WorkspaceRanResponse


class CodeExecutionUpdate_BuildingExecutor(BuildingExecutorResponse):
    type: typing_extensions.Literal["buildingExecutor"]

    class Config:
        frozen = True


class CodeExecutionUpdate_Running(RunningResponse):
    type: typing_extensions.Literal["running"]

    class Config:
        frozen = True


class CodeExecutionUpdate_Errored(ErroredResponse):
    type: typing_extensions.Literal["errored"]

    class Config:
        frozen = True


class CodeExecutionUpdate_Stopped(StoppedResponse):
    type: typing_extensions.Literal["stopped"]

    class Config:
        frozen = True


class CodeExecutionUpdate_Graded(GradedResponse):
    type: typing_extensions.Literal["graded"]

    class Config:
        frozen = True


class CodeExecutionUpdate_GradedV2(GradedResponseV2):
    type: typing_extensions.Literal["gradedV2"]

    class Config:
        frozen = True


class CodeExecutionUpdate_WorkspaceRan(WorkspaceRanResponse):
    type: typing_extensions.Literal["workspaceRan"]

    class Config:
        frozen = True


class CodeExecutionUpdate_Recording(RecordingResponseNotification):
    type: typing_extensions.Literal["recording"]

    class Config:
        frozen = True


class CodeExecutionUpdate_Recorded(RecordedResponseNotification):
    type: typing_extensions.Literal["recorded"]

    class Config:
        frozen = True


class CodeExecutionUpdate_InvalidRequest(InvalidRequestResponse):
    type: typing_extensions.Literal["invalidRequest"]

    class Config:
        frozen = True


class CodeExecutionUpdate_Finished(FinishedResponse):
    type: typing_extensions.Literal["finished"]

    class Config:
        frozen = True


CodeExecutionUpdate = typing_extensions.Annotated[
    typing.Union[
        CodeExecutionUpdate_BuildingExecutor,
        CodeExecutionUpdate_Running,
        CodeExecutionUpdate_Errored,
        CodeExecutionUpdate_Stopped,
        CodeExecutionUpdate_Graded,
        CodeExecutionUpdate_GradedV2,
        CodeExecutionUpdate_WorkspaceRan,
        CodeExecutionUpdate_Recording,
        CodeExecutionUpdate_Recorded,
        CodeExecutionUpdate_InvalidRequest,
        CodeExecutionUpdate_Finished,
    ],
    pydantic.Field(discriminator="type"),
]
CodeExecutionUpdate_Graded.update_forward_refs(
    KeyValuePair=KeyValuePair, MapValue=MapValue, VariableValue=VariableValue
)
CodeExecutionUpdate_GradedV2.update_forward_refs(
    KeyValuePair=KeyValuePair, MapValue=MapValue, VariableValue=VariableValue
)
