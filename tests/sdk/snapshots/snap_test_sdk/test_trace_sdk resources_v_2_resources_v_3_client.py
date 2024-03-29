# This file was auto-generated by Fern from our API Definition.

import typing

from .....environment import FernIrEnvironment
from .resources.problem.client import AsyncProblemClient, ProblemClient


class V3Client:
    def __init__(
        self,
        *,
        environment: FernIrEnvironment = FernIrEnvironment.PROD,
        x_random_header: typing.Optional[str] = None,
        token: typing.Optional[str] = None
    ):
        self._environment = environment
        self.x_random_header = x_random_header
        self._token = token
        self.problem = ProblemClient(
            environment=self._environment, x_random_header=self.x_random_header, token=self._token
        )


class AsyncV3Client:
    def __init__(
        self,
        *,
        environment: FernIrEnvironment = FernIrEnvironment.PROD,
        x_random_header: typing.Optional[str] = None,
        token: typing.Optional[str] = None
    ):
        self._environment = environment
        self.x_random_header = x_random_header
        self._token = token
        self.problem = AsyncProblemClient(
            environment=self._environment, x_random_header=self.x_random_header, token=self._token
        )
