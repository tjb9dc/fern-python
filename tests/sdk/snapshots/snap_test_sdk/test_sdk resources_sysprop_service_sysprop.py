# This file was auto-generated by Fern from our API Definition.

import typing

from ...commons.types.language import Language


class Sysprop:
    def __init__(self, *, environment: str):
        ...

    def set_num_warm_instances(self, *, language: Language, num_warm_instances: int) -> None:
        ...

    def get_num_warm_instances(self) -> typing.Dict[Language, int]:
        ...