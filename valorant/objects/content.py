import re
import typing as t
import operator as op

from .dto import DTO
from ..lexicon import Lex
from ..query import Expression


T = t.TypeVar("T")
attr = op.attrgetter


class ActDTO(DTO):
    name: str
    localizedNames: t.Mapping[str, str]
    id: str
    isActive: bool


class ContentItemDTO(DTO):
    name: str
    localizedNames: t.Optional[t.Mapping[str, str]]
    id: str
    assetName: str
    assetPath: str

    def __init__(self, obj):
        super().__init__(obj)

        self.localizedNames = obj.get("localizedNames")


class ContentDTO(DTO):
    version: str
    acts: t.List[ActDTO]
    characters: t.List[ContentItemDTO]
    maps: t.List[ContentItemDTO]
    chromas: t.List[ContentItemDTO]
    skins: t.List[ContentItemDTO]
    skinLevels: t.List[ContentItemDTO]
    equips: t.List[ContentItemDTO]
    gameModes: t.List[ContentItemDTO]
    sprays: t.List[ContentItemDTO]
    sprayLevels: t.List[ContentItemDTO]
    charms: t.List[ContentItemDTO]
    charmLevels: t.List[ContentItemDTO]
    playerCards: t.List[ContentItemDTO]
    playerTitles: t.List[ContentItemDTO]

    def __init__(self, obj):
        super().__init__(obj)

        self.acts = ContentList(ActDTO(i) for i in obj["acts"])

        for name in Lex.CONTENT_NAMES[1:]:
            self.__setattr__(name, ContentList(ContentItemDTO(i) for i in obj[name]))


def _fmt(key: t.Text) -> t.Text:
    if key.startswith("__") and key.endswith("__"):
        return re.sub(r"_{6}", "__.__", key)
    else:
        return re.sub(r"__(?!_)", ".", key)


def _operate(a, b):
    if isinstance(b, Expression):
        return b.statement(a)
    elif callable(b):
        return b(a)
    else:
        return op.eq(a, b)


class ContentList(list):
    def __init__(self, *args, **kwargs):
        super(ContentList, self).__init__(*args, **kwargs)

    def get(
        self, value: t.Optional[T] = None, **attrs: t.Mapping[t.Text, T]
    ) -> t.Optional[DTO]:
        """Get the first element in the ContentList with traits that match all the
        keyword arguments passed in `attrs`. The arguments passed can be any value,
        an expression, or a callable that returns a boolean or boolean-like object.

        A single argument defaults to checking for ``name``.

        Multiple arguments are checked using logical AND, not logical OR. The element
        `must` match all the arguments, not just one.

        Returns ``None`` if no elements in the ContentList match the given arguments.

        **Examples:**

        .. code-block:: python

            agent = agents.get(name="Neon")

        .. code-block:: python

            player = leaderboard.players.get(numberOfWins=lambda x: x >= 10)

        See the :doc:`guides/queries` page for more in-depth usage.

        :param value:
            Alias argument for ``name=value``. Ignores keyword arguments if passed.
        :type value: Optional[Any]

        :param attrs: Mapping of attribute traits to match for.
        :type attrs: Mapping[Any, Any]

        :rtype: Optional[DTO]
        """

        if value != None:
            attrs = {"name": value}

        funcs = [(attr(_fmt(key)), v) for key, v in attrs.items()]

        for el in self:
            try:
                if all(_operate(func(el), value) for func, value in funcs):
                    return el
            except AttributeError:
                continue

        return None

    def find(
        self, value: t.Optional[T] = None, **attrs: t.Mapping[t.Text, T]
    ) -> t.Optional[T]:
        """Semantic alias for :func:`.get`."""
        return self.get(value=value, **attrs)

    def get_all(
        self, value: t.Optional[T] = None, **attrs: t.Mapping[t.Text, T]
    ) -> t.List[DTO]:
        """Same functionality as :func:`.get()` but returns a list of every matching element.
        The list will be empty if no matching elements were found in the ContentList.

        :param value:
            Alias argument for ``name=value``. Ignores keyword arguments if passed.
        :type value: Optional[Any]

        :param attrs: Mapping of attribute traits to match for.
        :type attrs: Mapping[Any, Any]

        :rtype: List[DTO]
        """
        results = []

        if value != None:
            attrs = {"name": value}

        funcs = [(attr(_fmt(key)), v) for key, v in attrs.items()]

        for el in self:
            try:
                if all(_operate(func(el), value) for func, value in funcs):
                    results.append(el)
            except AttributeError:
                continue

        return results

    def find_all(
        self, value: t.Optional[T] = None, **attrs: t.Mapping[t.Text, T]
    ) -> t.Optional[T]:
        """Semantic alias for :func:`.get_all`."""
        return self.get_all(value=value, **attrs)
