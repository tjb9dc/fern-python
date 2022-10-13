# This file was auto-generated by Fern from our API Definition.

# flake8: noqa
# fmt: off
# isort: skip_file

import abc
import functools
import inspect
import logging
import typing

import fastapi

from ...core.abstract_fern_service import AbstractFernService
from ...core.exceptions import FernHTTPException
from ...core.route_args import get_route_args
from ..submission.types.test_submission_status import TestSubmissionStatus
from ..submission.types.test_submission_update import TestSubmissionUpdate
from ..submission.types.trace_response_v_2 import TraceResponseV2
from ..submission.types.workspace_submission_status import WorkspaceSubmissionStatus
from ..submission.types.workspace_submission_update import WorkspaceSubmissionUpdate
from .types.store_traced_test_case_request import StoreTracedTestCaseRequest
from .types.store_traced_workspace_request import StoreTracedWorkspaceRequest


class AbstractAdminService(AbstractFernService):
    """
    AbstractAdminService is an abstract class containing the methods that your
    AdminService implementation should implement.

    Each method is associated with an API route, which will be registered
    with FastAPI when you register your implementation using Fern's register()
    function.
    """

    @abc.abstractmethod
    def update_test_submission_status(self, *, body: TestSubmissionStatus, submission_id: str) -> None:
        ...

    @abc.abstractmethod
    def send_test_submission_update(self, *, body: TestSubmissionUpdate, submission_id: str) -> None:
        ...

    @abc.abstractmethod
    def update_workspace_submission_status(self, *, body: WorkspaceSubmissionStatus, submission_id: str) -> None:
        ...

    @abc.abstractmethod
    def send_workspace_submission_update(self, *, body: WorkspaceSubmissionUpdate, submission_id: str) -> None:
        ...

    @abc.abstractmethod
    def store_traced_test_case(
        self, *, body: StoreTracedTestCaseRequest, submission_id: str, test_case_id: str
    ) -> None:
        ...

    @abc.abstractmethod
    def store_traced_test_case_v_2(
        self, *, body: typing.List[TraceResponseV2], submission_id: str, test_case_id: str
    ) -> None:
        ...

    @abc.abstractmethod
    def store_traced_workspace(self, *, body: StoreTracedWorkspaceRequest, submission_id: str) -> None:
        ...

    @abc.abstractmethod
    def store_traced_workspace_v_2(self, *, body: typing.List[TraceResponseV2], submission_id: str) -> None:
        ...

    """
    Below are internal methods used by Fern to register your implementation.
    You can ignore them.
    """

    @classmethod
    def _init_fern(cls, router: fastapi.APIRouter) -> None:
        cls.__init_update_test_submission_status(router=router)
        cls.__init_send_test_submission_update(router=router)
        cls.__init_update_workspace_submission_status(router=router)
        cls.__init_send_workspace_submission_update(router=router)
        cls.__init_store_traced_test_case(router=router)
        cls.__init_store_traced_test_case_v_2(router=router)
        cls.__init_store_traced_workspace(router=router)
        cls.__init_store_traced_workspace_v_2(router=router)

    @classmethod
    def __init_update_test_submission_status(cls, router: fastapi.APIRouter) -> None:
        endpoint_function = inspect.signature(cls.update_test_submission_status)
        new_parameters: typing.List[inspect.Parameter] = []
        for index, (parameter_name, parameter) in enumerate(endpoint_function.parameters.items()):
            if index == 0:
                new_parameters.append(parameter.replace(default=fastapi.Depends(cls)))
            elif parameter_name == "body":
                new_parameters.append(parameter.replace(default=fastapi.Body(...)))
            elif parameter_name == "submission_id":
                new_parameters.append(parameter.replace(default=fastapi.Path(...)))
            else:
                new_parameters.append(parameter)
        setattr(
            cls.update_test_submission_status, "__signature__", endpoint_function.replace(parameters=new_parameters)
        )

        @functools.wraps(cls.update_test_submission_status)
        def wrapper(*args: typing.Any, **kwargs: typing.Any) -> None:
            try:
                return cls.update_test_submission_status(*args, **kwargs)
            except FernHTTPException as e:
                logging.getLogger(__name__).warn(
                    f"update_test_submission_status unexpectedly threw {e.__class__.__name__}. "
                    + f"If this was intentional, please add {e.__class__.__name__} to "
                    + "update_test_submission_status's errors list in your Fern Definition."
                )
                raise e

        router.post(
            path="/admin/store-test-submission-status/{submission_id}",
            **get_route_args(cls.update_test_submission_status),
        )(wrapper)

    @classmethod
    def __init_send_test_submission_update(cls, router: fastapi.APIRouter) -> None:
        endpoint_function = inspect.signature(cls.send_test_submission_update)
        new_parameters: typing.List[inspect.Parameter] = []
        for index, (parameter_name, parameter) in enumerate(endpoint_function.parameters.items()):
            if index == 0:
                new_parameters.append(parameter.replace(default=fastapi.Depends(cls)))
            elif parameter_name == "body":
                new_parameters.append(parameter.replace(default=fastapi.Body(...)))
            elif parameter_name == "submission_id":
                new_parameters.append(parameter.replace(default=fastapi.Path(...)))
            else:
                new_parameters.append(parameter)
        setattr(cls.send_test_submission_update, "__signature__", endpoint_function.replace(parameters=new_parameters))

        @functools.wraps(cls.send_test_submission_update)
        def wrapper(*args: typing.Any, **kwargs: typing.Any) -> None:
            try:
                return cls.send_test_submission_update(*args, **kwargs)
            except FernHTTPException as e:
                logging.getLogger(__name__).warn(
                    f"send_test_submission_update unexpectedly threw {e.__class__.__name__}. "
                    + f"If this was intentional, please add {e.__class__.__name__} to "
                    + "send_test_submission_update's errors list in your Fern Definition."
                )
                raise e

        router.post(
            path="/admin/store-test-submission-status-v2/{submission_id}",
            **get_route_args(cls.send_test_submission_update),
        )(wrapper)

    @classmethod
    def __init_update_workspace_submission_status(cls, router: fastapi.APIRouter) -> None:
        endpoint_function = inspect.signature(cls.update_workspace_submission_status)
        new_parameters: typing.List[inspect.Parameter] = []
        for index, (parameter_name, parameter) in enumerate(endpoint_function.parameters.items()):
            if index == 0:
                new_parameters.append(parameter.replace(default=fastapi.Depends(cls)))
            elif parameter_name == "body":
                new_parameters.append(parameter.replace(default=fastapi.Body(...)))
            elif parameter_name == "submission_id":
                new_parameters.append(parameter.replace(default=fastapi.Path(...)))
            else:
                new_parameters.append(parameter)
        setattr(
            cls.update_workspace_submission_status,
            "__signature__",
            endpoint_function.replace(parameters=new_parameters),
        )

        @functools.wraps(cls.update_workspace_submission_status)
        def wrapper(*args: typing.Any, **kwargs: typing.Any) -> None:
            try:
                return cls.update_workspace_submission_status(*args, **kwargs)
            except FernHTTPException as e:
                logging.getLogger(__name__).warn(
                    f"update_workspace_submission_status unexpectedly threw {e.__class__.__name__}. "
                    + f"If this was intentional, please add {e.__class__.__name__} to "
                    + "update_workspace_submission_status's errors list in your Fern Definition."
                )
                raise e

        router.post(
            path="/admin/store-workspace-submission-status/{submission_id}",
            **get_route_args(cls.update_workspace_submission_status),
        )(wrapper)

    @classmethod
    def __init_send_workspace_submission_update(cls, router: fastapi.APIRouter) -> None:
        endpoint_function = inspect.signature(cls.send_workspace_submission_update)
        new_parameters: typing.List[inspect.Parameter] = []
        for index, (parameter_name, parameter) in enumerate(endpoint_function.parameters.items()):
            if index == 0:
                new_parameters.append(parameter.replace(default=fastapi.Depends(cls)))
            elif parameter_name == "body":
                new_parameters.append(parameter.replace(default=fastapi.Body(...)))
            elif parameter_name == "submission_id":
                new_parameters.append(parameter.replace(default=fastapi.Path(...)))
            else:
                new_parameters.append(parameter)
        setattr(
            cls.send_workspace_submission_update, "__signature__", endpoint_function.replace(parameters=new_parameters)
        )

        @functools.wraps(cls.send_workspace_submission_update)
        def wrapper(*args: typing.Any, **kwargs: typing.Any) -> None:
            try:
                return cls.send_workspace_submission_update(*args, **kwargs)
            except FernHTTPException as e:
                logging.getLogger(__name__).warn(
                    f"send_workspace_submission_update unexpectedly threw {e.__class__.__name__}. "
                    + f"If this was intentional, please add {e.__class__.__name__} to "
                    + "send_workspace_submission_update's errors list in your Fern Definition."
                )
                raise e

        router.post(
            path="/admin/store-workspace-submission-status-v2/{submission_id}",
            **get_route_args(cls.send_workspace_submission_update),
        )(wrapper)

    @classmethod
    def __init_store_traced_test_case(cls, router: fastapi.APIRouter) -> None:
        endpoint_function = inspect.signature(cls.store_traced_test_case)
        new_parameters: typing.List[inspect.Parameter] = []
        for index, (parameter_name, parameter) in enumerate(endpoint_function.parameters.items()):
            if index == 0:
                new_parameters.append(parameter.replace(default=fastapi.Depends(cls)))
            elif parameter_name == "body":
                new_parameters.append(parameter.replace(default=fastapi.Body(...)))
            elif parameter_name == "submission_id":
                new_parameters.append(parameter.replace(default=fastapi.Path(...)))
            elif parameter_name == "test_case_id":
                new_parameters.append(parameter.replace(default=fastapi.Path(...)))
            else:
                new_parameters.append(parameter)
        setattr(cls.store_traced_test_case, "__signature__", endpoint_function.replace(parameters=new_parameters))

        @functools.wraps(cls.store_traced_test_case)
        def wrapper(*args: typing.Any, **kwargs: typing.Any) -> None:
            try:
                return cls.store_traced_test_case(*args, **kwargs)
            except FernHTTPException as e:
                logging.getLogger(__name__).warn(
                    f"store_traced_test_case unexpectedly threw {e.__class__.__name__}. "
                    + f"If this was intentional, please add {e.__class__.__name__} to "
                    + "store_traced_test_case's errors list in your Fern Definition."
                )
                raise e

        router.post(
            path="/admin/store-test-trace/submission/{submission_id}/testCase/{test_case_id}",
            **get_route_args(cls.store_traced_test_case),
        )(wrapper)

    @classmethod
    def __init_store_traced_test_case_v_2(cls, router: fastapi.APIRouter) -> None:
        endpoint_function = inspect.signature(cls.store_traced_test_case_v_2)
        new_parameters: typing.List[inspect.Parameter] = []
        for index, (parameter_name, parameter) in enumerate(endpoint_function.parameters.items()):
            if index == 0:
                new_parameters.append(parameter.replace(default=fastapi.Depends(cls)))
            elif parameter_name == "body":
                new_parameters.append(parameter.replace(default=fastapi.Body(...)))
            elif parameter_name == "submission_id":
                new_parameters.append(parameter.replace(default=fastapi.Path(...)))
            elif parameter_name == "test_case_id":
                new_parameters.append(parameter.replace(default=fastapi.Path(...)))
            else:
                new_parameters.append(parameter)
        setattr(cls.store_traced_test_case_v_2, "__signature__", endpoint_function.replace(parameters=new_parameters))

        @functools.wraps(cls.store_traced_test_case_v_2)
        def wrapper(*args: typing.Any, **kwargs: typing.Any) -> None:
            try:
                return cls.store_traced_test_case_v_2(*args, **kwargs)
            except FernHTTPException as e:
                logging.getLogger(__name__).warn(
                    f"store_traced_test_case_v_2 unexpectedly threw {e.__class__.__name__}. "
                    + f"If this was intentional, please add {e.__class__.__name__} to "
                    + "store_traced_test_case_v_2's errors list in your Fern Definition."
                )
                raise e

        router.post(
            path="/admin/store-test-trace-v2/submission/{submission_id}/testCase/{test_case_id}",
            **get_route_args(cls.store_traced_test_case_v_2),
        )(wrapper)

    @classmethod
    def __init_store_traced_workspace(cls, router: fastapi.APIRouter) -> None:
        endpoint_function = inspect.signature(cls.store_traced_workspace)
        new_parameters: typing.List[inspect.Parameter] = []
        for index, (parameter_name, parameter) in enumerate(endpoint_function.parameters.items()):
            if index == 0:
                new_parameters.append(parameter.replace(default=fastapi.Depends(cls)))
            elif parameter_name == "body":
                new_parameters.append(parameter.replace(default=fastapi.Body(...)))
            elif parameter_name == "submission_id":
                new_parameters.append(parameter.replace(default=fastapi.Path(...)))
            else:
                new_parameters.append(parameter)
        setattr(cls.store_traced_workspace, "__signature__", endpoint_function.replace(parameters=new_parameters))

        @functools.wraps(cls.store_traced_workspace)
        def wrapper(*args: typing.Any, **kwargs: typing.Any) -> None:
            try:
                return cls.store_traced_workspace(*args, **kwargs)
            except FernHTTPException as e:
                logging.getLogger(__name__).warn(
                    f"store_traced_workspace unexpectedly threw {e.__class__.__name__}. "
                    + f"If this was intentional, please add {e.__class__.__name__} to "
                    + "store_traced_workspace's errors list in your Fern Definition."
                )
                raise e

        router.post(
            path="/admin/store-workspace-trace/submission/{submission_id}", **get_route_args(cls.store_traced_workspace)
        )(wrapper)

    @classmethod
    def __init_store_traced_workspace_v_2(cls, router: fastapi.APIRouter) -> None:
        endpoint_function = inspect.signature(cls.store_traced_workspace_v_2)
        new_parameters: typing.List[inspect.Parameter] = []
        for index, (parameter_name, parameter) in enumerate(endpoint_function.parameters.items()):
            if index == 0:
                new_parameters.append(parameter.replace(default=fastapi.Depends(cls)))
            elif parameter_name == "body":
                new_parameters.append(parameter.replace(default=fastapi.Body(...)))
            elif parameter_name == "submission_id":
                new_parameters.append(parameter.replace(default=fastapi.Path(...)))
            else:
                new_parameters.append(parameter)
        setattr(cls.store_traced_workspace_v_2, "__signature__", endpoint_function.replace(parameters=new_parameters))

        @functools.wraps(cls.store_traced_workspace_v_2)
        def wrapper(*args: typing.Any, **kwargs: typing.Any) -> None:
            try:
                return cls.store_traced_workspace_v_2(*args, **kwargs)
            except FernHTTPException as e:
                logging.getLogger(__name__).warn(
                    f"store_traced_workspace_v_2 unexpectedly threw {e.__class__.__name__}. "
                    + f"If this was intentional, please add {e.__class__.__name__} to "
                    + "store_traced_workspace_v_2's errors list in your Fern Definition."
                )
                raise e

        router.post(
            path="/admin/store-workspace-trace-v2/submission/{submission_id}",
            **get_route_args(cls.store_traced_workspace_v_2),
        )(wrapper)