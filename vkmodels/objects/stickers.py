import dataclasses
import enum
import typing

from vkmodels.bases.object import ObjectBase


@dataclasses.dataclass
class ImageSet(
    ObjectBase,
):
    base_url: str
    version: typing.Optional[int] = None
