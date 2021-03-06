import dataclasses
import enum
import typing

from vkmodels.bases.object import ObjectBase


@dataclasses.dataclass
class Error(
    ObjectBase,
):
    error: str
    error_description: str
    redirect_uri: typing.Optional[str] = None
