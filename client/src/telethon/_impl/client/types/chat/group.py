from typing import Optional, Self, Union

from ....session import PackedChat, PackedType
from ....tl import abcs, types
from ..meta import NoPublicConstructor


class Group(metaclass=NoPublicConstructor):
    """
    A small group or supergroup.

    You can get a group from messages via :attr:`telethon.types.Message.chat`,
    or from methods such as :meth:`telethon.Client.resolve_username`.
    """

    __slots__ = ("_raw",)

    def __init__(
        self,
        raw: Union[
            types.ChatEmpty,
            types.Chat,
            types.ChatForbidden,
            types.Channel,
            types.ChannelForbidden,
        ],
    ) -> None:
        self._raw = raw

    @classmethod
    def _from_raw(cls, chat: abcs.Chat) -> Self:
        if isinstance(chat, (types.ChatEmpty, types.Chat, types.ChatForbidden)):
            return cls._create(chat)
        elif isinstance(chat, (types.Channel, types.ChannelForbidden)):
            if chat.broadcast:
                raise RuntimeError("cannot create group from broadcast channel")
            return cls._create(chat)
        else:
            raise RuntimeError("unexpected case")

    @property
    def id(self) -> int:
        return self._raw.id

    def pack(self) -> Optional[PackedChat]:
        if isinstance(self._raw, (types.ChatEmpty, types.Chat, types.ChatForbidden)):
            return PackedChat(ty=PackedType.CHAT, id=self._raw.id, access_hash=None)
        elif self._raw.access_hash is None:
            return None
        else:
            return PackedChat(
                ty=PackedType.MEGAGROUP, id=self._raw.id, access_hash=None
            )

    @property
    def title(self) -> str:
        return getattr(self._raw, "title", None) or ""

    @property
    def full_name(self) -> str:
        return self.title

    @property
    def username(self) -> Optional[str]:
        return getattr(self._raw, "username", None)

    @property
    def is_megagroup(self) -> bool:
        return isinstance(self._raw, (types.Channel, types.ChannelForbidden))
