# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from .error_info import ErrorInfo
from .running_submission_state import RunningSubmissionState
from .workspace_run_details import WorkspaceRunDetails


class WorkspaceSubmissionStatus_Stopped(pydantic.BaseModel):
    type: typing_extensions.Literal["stopped"]

    class Config:
        frozen = True


class WorkspaceSubmissionStatus_Errored(pydantic.BaseModel):
    type: typing_extensions.Literal["errored"]
    value: ErrorInfo

    class Config:
        frozen = True


class WorkspaceSubmissionStatus_Running(pydantic.BaseModel):
    type: typing_extensions.Literal["running"]
    value: RunningSubmissionState

    class Config:
        frozen = True


class WorkspaceSubmissionStatus_Ran(WorkspaceRunDetails):
    type: typing_extensions.Literal["ran"]

    class Config:
        frozen = True


class WorkspaceSubmissionStatus_Traced(WorkspaceRunDetails):
    type: typing_extensions.Literal["traced"]

    class Config:
        frozen = True


WorkspaceSubmissionStatus = typing_extensions.Annotated[
    typing.Union[
        WorkspaceSubmissionStatus_Stopped,
        WorkspaceSubmissionStatus_Errored,
        WorkspaceSubmissionStatus_Running,
        WorkspaceSubmissionStatus_Ran,
        WorkspaceSubmissionStatus_Traced,
    ],
    pydantic.Field(discriminator="type"),
]
