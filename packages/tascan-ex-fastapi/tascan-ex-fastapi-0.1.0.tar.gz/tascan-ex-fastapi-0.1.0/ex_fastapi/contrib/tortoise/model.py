from collections.abc import Callable
from typing import Any, Type

from tortoise import Model as DefaultModel


class Model(DefaultModel):

    class Meta:
        abstract = True

    @classmethod
    async def check_unique(cls, data: dict[str, Any]) -> list[str]:
        # TODO: self.__class__._meta.unique_together
        not_unique = []
        query = cls.all()
        for key, value in cls._meta.fields_map.items():
            if (
                    not value.generated
                    and value.unique
                    and (current_value := data.get(key)) is not None
            ):
                if await query.filter(**{key: current_value}).exists():
                    not_unique.append(key)
        return not_unique


def get_field(model: Type[Model], fname: str):
    return model._meta.fields_map[fname]


def max_len_of(model: Type[Model]) -> Callable[[str], int]:
    def wrapper(fname: str):
        return get_field(model, fname).max_length
    return wrapper


def default_of(model: Type[Model]) -> Callable[[str], Any]:
    def wrapper(fname: str):
        return get_field(model, fname).default
    return wrapper
