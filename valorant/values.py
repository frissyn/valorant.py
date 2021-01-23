import locale

BASE_URL = "https://{code}.api.riotgames.com/"
LOCALE = locale.getdefaultlocale()[0].replace("_", "-")
ROUTES = ["americas", "asia", "europe"]

REGIONS = [
    "eu", "eune", "euw", "jp", "kr", "lan", "br",
    "las", "na", "oce", "ru", "tr", "latam", "ap"
]

ENDPOINTS = {
    "content": "val/content/v1/contents",
    "leaderboard": "val/ranked/v1/leaderboards/by-act/{actId}",
    "status": "val/status/v1/platform-data",
    "puuid": "riot/account/v1/accounts/by-puuid/{puuid}",
    "gamename": "riot/account/v1/accounts/by-riot-id/{name}/{tag}",
    "match": "val/match/v1/matches/{matchID}",
    "match-history": "val/match/v1/matchlists/by-puuid/{puuid}",
    "match-queue": "val/match/v1/recent-matches/by-queue/{queue}"
}

HEADERS = {
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8"
}
