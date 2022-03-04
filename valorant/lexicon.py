import locale


class Lex:
    SAFES = "~()*!.'"
    CLIENT_API = "https://pd.{code}.a.pvp.net/"
    WEB_API = "https://{code}.api.riotgames.com/"
    LOCALE = locale.getdefaultlocale()[0].replace("_", "-")
    ROUTES = ["americas", "asia", "europe"]

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

    ENDPOINTS = {
        "client": {
            "mmr": "mmr/v1/players/{playerID}/competitiveupdates",
        },
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

    HEADERS = {
        "web": {"Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8"},
        "client": {
            "Authorization": "Bearer {token}",
            "Content-Type": "application/json",
            "X-Riot-Entitlements-JWT": "riot_entitlement",
        },
    }

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
