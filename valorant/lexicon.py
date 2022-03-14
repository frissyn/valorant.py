import locale


class Lex:
    """Reference class for storing constants to be used across the library.
    Initializing isn't allowed and will throw a ``NotImplementedError``.
    """

    def __init__(self):
        raise NotImplementedError("Lexicon is not allowed to be initialized.")

    SAFES = "~()*!.'"
    """String of URL-safe characters in requests to the API."""

    CLIENT_API = "https://pd.{code}.a.pvp.net/"
    """URL for the Valorant client API."""

    WEB_API = "https://{code}.api.riotgames.com/"
    """URL for the Valorant client API."""

    LOCALE = locale.getdefaultlocale()[0].replace("_", "-")
    """Default locale as determine by Python's locale module."""

    ROUTES = ["americas", "asia", "europe"]
    """List of geographical routes supported by the Web API."""

    LOCALES = [
        "ar-AE",
        "de-DE",
        "en-GB",
        "en-US",
        "es-ES",
        "es-MX",
        "fr-FR",
        "id-ID",
        "it-IT",
        "ja-JP",
        "ko-KR",
        "pl-PL",
        "pt-BR",
        "ru-RU",
        "th-TH",
        "tr-TR",
        "vi-VN",
        "zh-CN",
        "zh-TW",
    ]
    """List of locales supported by the client and web API."""

    REGIONS = [
        "ap",
        "br",
        "eu",
        "eune",
        "euw",
        "jp",
        "kr",
        "lan",
        "las",
        "latam",
        "na",
        "oce",
        "ru",
        "tr",
    ]
    """List of locales supported by the client and web API."""

    CONTENT_NAMES = [
        "acts",
        "characters",
        "charmLevels",
        "charms",
        "chromas",
        "equips",
        "gameModes",
        "maps",
        "playerCards",
        "playerTitles",
        "skinLevels",
        "skins",
        "sprays",
    ]
    """List of content data attribute names."""

    ENDPOINTS = {
        "web": {
            "content": "val/content/v1/contents",
            "game-name": "riot/account/v1/accounts/by-riot-id/{name}/{tag}",
            "leaderboard": "val/ranked/v1/leaderboards/by-act/{actID}",
            "match": "val/match/v1/matches/{matchID}",
            "match-queue": "val/match/v1/recent-matches/by-queue/{queue}",
            "matchlists": "val/match/v1/matchlists/by-puuid/{puuid}",
            "puuid": "riot/account/v1/accounts/by-puuid/{puuid}",
            "status": "val/status/v1/platform-data",
        },
    }
    """Mappings of endpoint names to endpoint paths for the client and web API."""

    HEADERS = {
        "web": {"Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8"},
    }
    """Default headers for the client and web API."""

    RANKS = {
        0: "Unrated",
        3: "Iron 1",
        4: "Iron 2",
        5: "Iron 3",
        6: "Bronze 1",
        7: "Bronze 2",
        8: "Bronze 3",
        9: "Silver 1",
        10: "Silver 2",
        11: "Silver 3",
        12: "Gold 1",
        13: "Gold 2",
        14: "Gold 3",
        15: "Platinum 1",
        16: "Platinum 2",
        17: "Platinum 3",
        18: "Diamond 1",
        19: "Diamond 2",
        20: "Diamond 3",
        21: "Immortal 1",
        22: "Immortal 2",
        23: "Immortal 3",
        24: "Radiant",
    }
    """Mapping of competitiveTier values to rank title."""
