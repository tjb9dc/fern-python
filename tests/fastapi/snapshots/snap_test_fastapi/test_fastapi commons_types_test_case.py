import typing

import pydantic
import typing_extensions

from .variable_value import VariableValue


class TestCase(pydantic.BaseModel):
    id: str
    params: typing.List[VariableValue]

    @pydantic.validator("id")
    def _validate_id(cls, id: str) -> str:
        for validator in TestCase.Validators._id:
            id = validator(id)
        return id

    @pydantic.validator("params")
    def _validate_params(cls, params: typing.List[VariableValue]) -> typing.List[VariableValue]:
        for validator in TestCase.Validators._params:
            params = validator(params)
        return params

    class Validators:
        _id: typing.ClassVar[typing.List[typing.Callable[[str], str]]] = []
        _params: typing.ClassVar[
            typing.List[typing.Callable[[typing.List[VariableValue]], typing.List[VariableValue]]]
        ] = []

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["id"]
        ) -> typing.Callable[[typing.Callable[[str], str]], typing.Callable[[str], str]]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["params"]
        ) -> typing.Callable[
            [typing.Callable[[typing.List[VariableValue]], typing.List[VariableValue]]],
            typing.Callable[[typing.List[VariableValue]], typing.List[VariableValue]],
        ]:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "id":
                    cls._id.append(validator)
                elif field_name == "params":
                    cls._params.append(validator)
                else:
                    raise RuntimeError("Field does not exist on TestCase: " + field_name)

                return validator

            return decorator

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    class Config:
        frozen = True