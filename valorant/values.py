import locale

SAFES = "~()*!.'"
CLIENT_API = "https://pd.{code}.a.pvp.net/"
WEB_API = "https://{code}.api.riotgames.com/"

LOCALE = locale.getdefaultlocale()[0].replace('_', '-')

ROUTES = ["americas", "asia", "europe"]

LOCALES = [
    "ar-AE",
    "de-DE",
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
    "tr-TR",
    "th-TH",
    "vi-VN",
    "zh-TW",
]

REGIONS = [
    "eu",
    "eune",
    "euw",
    "jp",
    "kr",
    "lan",
    "br",
    "las",
    "na",
    "oce",
    "ru",
    "tr",
    "latam",
    "ap",
]

ENDPOINTS = {
    "web": {
        "content": "val/content/v1/contents",
        "leaderboard": "val/ranked/v1/leaderboards/by-act/{actID}",
        "status": "val/status/v1/platform-data",
        "puuid": "riot/account/v1/accounts/by-puuid/{puuid}",
        "game-name": "riot/account/v1/accounts/by-riot-id/{name}/{tag}",
        "match": "val/match/v1/matches/{matchID}",
        "match-history": "val/match/v1/matchlists/by-puuid/{puuid}",
        "match-queue": "val/match/v1/recent-matches/by-queue/{queue}",
    },
    "client": {
        "mmr": "mmr/v1/players/{playerID}/competitiveupdates",
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
