# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class VendorNetwork(str, enum.Enum):
    ENTITY = "ENTITY"
    PLATFORM = "PLATFORM"
    MERCOA = "MERCOA"

    def visit(
        self,
        entity: typing.Callable[[], T_Result],
        platform: typing.Callable[[], T_Result],
        mercoa: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is VendorNetwork.ENTITY:
            return entity()
        if self is VendorNetwork.PLATFORM:
            return platform()
        if self is VendorNetwork.MERCOA:
            return mercoa()