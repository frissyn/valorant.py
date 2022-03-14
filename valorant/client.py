import requests
import typing as t
import urllib.parse

from .lexicon import Lex

from .caller import WebCaller

from .objects import (
    DTO,
    ActDTO,
    AccountDTO,
    ContentDTO,
    ContentItemDTO,
    LeaderboardDTO,
    LeaderboardIterator,
    PlatformDataDTO,
)


class Client(object):
    """Represents a connection to the Riot Games API.
    Interacts specifically with VALORANT related endpoints.

    A number of options can be passed to the :class:`Client`.

    :param key:
        An access key used to authenticate with the API. Depending on the key's
        access level, match endpoints may be restricted.
    :type key: str
    :param locale:
        The region locale to use when making requests. This defaults to the system's
        locale as determined by Python.
        (i.e `locale.getdefaultlocale() <https://docs.python.org/3/library/locale.html#locale.getdefaultlocale>`_)
        If set to ``None``, :attr:`ContentItemDTO.localizedNames` will be included in
        the response.
    :type locale: Optional[str]
    :param region:
        The region to use when making requests. This defaults to `na`. Valid regions
        include `na`, `eu`, `latam`, etc. See :data:`Lex.REGIONS` for a complete list
        of valid regions.
    :type region: Optional[str]
    :param route:
        The region route to use when making requests for Riot Accounts. This defaults
        to `americas`. Valid routes are `americas`, `asia`, `europe`, and `esports`.
        See :data:`Lex.ROUTES` for a complete list of valid routes.
    :type route: Optional[str]
    :param load_content:
        Whether to load and cache content data from VALORANT upon initialization.
        Defaults to `True`.
    :type load_content: bool

    *Changed in version 1.0:* Renamed *reload* parameter to *load_content*.
    """

    def __init__(
        self,
        key: t.Text,
        locale: t.Optional[t.Text] = Lex.LOCALE,
        region: t.Text = "na",
        route: t.Text = "americas",
        load_content: bool = True,
    ):
        self.key = key
        self.route = route
        self.locale = locale
        self.region = region
        self.handle = WebCaller(key, locale, region, route)

        if load_content:
            self.get_content(cache=True)
        else:
            self.content = None

    def _content_if_cache(self) -> ContentDTO:
        content = getattr(self, "content", None)

        if content:
            return content
        else:
            return ContentDTO(self.handle.call("GET", "content"))

    def __getattribute__(self, name):
        return super(Client, self).__getattribute__(name)

    def asset(
        self, **attributes: t.Mapping[t.Text, t.Any]
    ) -> t.Optional[t.Union[ActDTO, ContentItemDTO]]:
        """Find an item in VALORANT content data matching all given attributes.
        Returns ``None`` if item is not found. This works because there are no
        semantic distinctions between Content Items.

        For example, ``client.asset(name="Viper")`` would return a
        :class:`ContentItemDTO` denoting content data for Viper.

        .. note::
            If content data is not cached, this function will make a request
            for it when called. Be wary of ratelimits should you decide not to
            cache content data.

        :param attributes: A mapping of keyword arguments to match for.
        :type attributes: Mapping[str, Any]
        :rtype: Optional[Union[ActDTO, ContentItemDTO]]
        """
        content = self._content_if_cache()

        for name in Lex.CONTENT_NAMES:
            el = getattr(content, name).get(**attributes)

            if el:
                return el

        return None

    def get_acts(self) -> t.List[ActDTO]:
        """Get a :class:`ContentList` of :class:`ActDTO` objects from VALORANT.

        :rtype: ContentList[ActDTO]
        """
        return self._content_if_cache().acts

    def get_characters(self) -> t.List[ContentItemDTO]:
        """Get a :class:`ContentList` of :class:`ContentItemDTO` objects that each
        represent an Agent from VALORANT.

        :rtype: ContentList[ContentItemDTO]
        """
        return self._content_if_cache().characters

    def get_charm_levels(self) -> t.List[ContentItemDTO]:
        """Get a :class:`ContentList` of :class:`ContentItemDTO` objects that each
        represent a Gun Buddy Variant from VALORANT.

        :rtype: ContentList[ContentItemDTO]
        """
        return self._content_if_cache().charmLevels

    def get_charms(self) -> t.List[ContentItemDTO]:
        """Get a :class:`ContentList` of :class:`ContentItemDTO` objects that each
        represent a Gun Buddy from VALORANT.

        :rtype: ContentList[ContentItemDTO]
        """
        return self._content_if_cache().charms

    def get_chromas(self, strip: bool = False) -> t.List[ContentItemDTO]:
        """Get a :class:`ContentList` of :class:`ContentItemDTO` objects that each
        represent a Gun Skin or Gun Skin Color Variant from VALORANT.

        :param strip:
            If set to ``True``, the ``\\r\\n`` and ``\\n`` characters will be
            replaced by a single space character. This is useful for formatting the
            gun skin names.
        :type strip: bool

        :rtype: ContentList[ContentItemDTO]
        """
        chromas = self._content_if_cache().chromas

        if strip:
            for c in chromas:
                c.name = c.name.replace("\r\n", " ")
                c.name = c.name.replace("\n", " ")

        return chromas

    def get_content(self, cache: bool = True) -> ContentDTO:
        """Get complete content data from VALORANT.

        :param cache: If set to ``True``, the Client will cache the response data,
            and subsequent calls wills return the cache. Update this cache by calling
            :func:`Client.get_content` again with cache set to ``True``.

        .. note::
            The cache provided is stored in memory and will not persist across program
            restarts.

        :type cache: bool
        :rtype: ContentDTO
        """
        content = self._content_if_cache()

        if cache:
            self.content = content

        return content

    def get_current_act(self) -> t.Optional[ActDTO]:
        """Helper function to get the current act from VALORANT. Returns ``None`` if
        the current act can't be determined.

        :rtype: Optional[ActDTO]
        """

        return self.get_acts().find(isActive=True)

    def get_equips(self) -> t.List[ContentItemDTO]:
        """Get a :class:`ContentList` of :class:`ContentItemDTO` objects that each
        represent an Equippable items from from VALORANT (Includes abilities and
        standard guns/melee).

        :rtype: ContentList[ContentItemDTO]
        """
        return self._content_if_cache().equips

    def get_game_modes(self) -> t.List[ContentItemDTO]:
        """Get a :class:`ContentList` of :class:`ContentItemDTO` objects that each
        represent a Game Mode from VALORANT.

        :rtype: ContentList[ContentItemDTO]
        """
        return self._content_if_cache().gameModes

    def get_leaderboard(
        self,
        size: int = 100,
        page: int = 0,
        pages: t.Optional[int] = None,
        actID: t.Text = "",
    ) -> t.Union[LeaderboardDTO, LeaderboardIterator]:
        actID = self.get_current_act().id if not actID else actID

        if pages:
            return LeaderboardIterator(self.handle, pages=pages, size=size, actID=actID)

        params = {"size": size, "startIndex": size * page}

        r = self.handle.call("GET", "leaderboard", params=params, actID=actID)

        return LeaderboardDTO(r)

    def get_maps(self) -> t.List[ContentItemDTO]:
        """Get a :class:`ContentList` of :class:`ContentItemDTO` objects that each
        represent a Map from VALORANT.

        :rtype: ContentList[ContentItemDTO]
        """
        return self._content_if_cache().maps

    def get_platform_status(self) -> PlatformDataDTO:
        r = self.handle.call("GET", "status")

        return PlatformDataDTO(r)

    def get_player_cards(self) -> t.List[ContentItemDTO]:
        """Get a :class:`ContentList` of :class:`ContentItemDTO` objects that each
        represent a Player Card from VALORANT.

        :rtype: ContentList[ContentItemDTO]
        """
        return self._content_if_cache().playerCards

    def get_player_titles(self) -> t.List[ContentItemDTO]:
        """Get a :class:`ContentList` of :class:`ContentItemDTO` objects that each
        represent a Player Title from VALORANT.

        :rtype: ContentList[ContentItemDTO]
        """
        return self._content_if_cache().playerTitles

    def get_skin_levels(self) -> t.List[ContentItemDTO]:
        """Get a :class:`ContentList` of :class:`ContentItemDTO` objects that each
        represent a Gun Skin from VALORANT (Including levels, but not color variants).

        :rtype: ContentList[ContentItemDTO]
        """
        return self._content_if_cache().skinLevels

    def get_skins(self) -> t.List[ContentItemDTO]:
        """Get a :class:`ContentList` of :class:`ContentItemDTO` objects that each
        represent a Gun Skin from VALORANT (Not including levels or color variants.)

        :rtype: ContentList[ContentItemDTO]
        """
        return self._content_if_cache().skins

    def get_spray_levels(self) -> t.List[ContentItemDTO]:
        """Get a :class:`ContentList` of :class:`ContentItemDTO` objects that each
        represent a Spray Variant from VALORANT.

        :rtype: ContentList[ContentItemDTO]
        """
        return self._content_if_cache().sprayLevels

    def get_sprays(self) -> t.List[ContentItemDTO]:
        """Get a :class:`ContentList` of :class:`ContentItemDTO` objects that each
        represent a Spray from VALORANT.

        :rtype: ContentList[ContentItemDTO]
        """
        return self._content_if_cache().sprays

    def get_user(
        self, puuid: t.Text, route: t.Text = "americas"
    ) -> t.Optional[AccountDTO]:
        """Get a Riot Account by their PUUID. Returns ``None`` if user could not
        be found.

        :param puuid: The PUUID of the account to retrieve.
        :type puuid: str
        :param route:
            Geographical route to get the account from. See :data:`Lex.ROUTES` for
            a list of valid routes. Defaults `americas`.
        :type route: str
        :rtype: Optional[AccountDTO]
        """

        try:
            r = self.handle.call("GET", "puuid", route=True, puuid=puuid)
        except requests.exceptions.HTTPError as e:
            if e.response.status_code in (400, 404):
                return None
            else:
                e.response.raise_for_status()

        return AccountDTO(r, self.handle)

    def get_user_by_name(
        self, name: t.Text, route: t.Text = "americas"
    ) -> t.Optional[AccountDTO]:
        """Gets a Riot Account by their game name and tag line. Returns ``None`` if
        user could not be found.

        :param name:
            The account's full game name and tag line, split by a hastag.
            (i.e `frissyn#6969`)
        :type name: str
        :param route:
            Geographical route to get the account from. See :data:`Lex.ROUTES` for
            a list of valid routes. Defaults `americas`.
        :type route: str
        :rtype: Optional[AccountDTO]
        """
        vals = name.split("#")
        vals = [urllib.parse.quote(v, safe=Lex.SAFES) for v in vals]

        try:
            r = self.handle.call(
                "GET", "game-name", route=True, name=vals[0], tag=vals[1]
            )
        except requests.exceptions.HTTPError as e:
            if e.response.status_code in (400, 404):
                return None
            else:
                e.response.raise_for_status()

        return AccountDTO(r, self.handle)
