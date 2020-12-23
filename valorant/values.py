import locale

BASE_URL = "https://{code}.api.riotgames.com/"
LOCALE = locale.getlocale()[0].replace("_", "-")
ROUTES = ["americas", "asia", "europe"]

REIGONS = [
    "eu", "eune", "euw", "jp", "kr", "lan", "br",
    "las", "na", "oce", "ru", "tr", "latam", "ap"
]

ENDPOINTS = {
    "content": "val/content/v1/contents",
    "status": "val/status/v1/platform-data",
    "puuid": "riot/account/v1/accounts/by-puuid/{puuid}",
    "gamename": "riot/account/v1/accounts/by-riot-id/{name}/{tag}"
}

HEADERS = {
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8"
}

def _build_header(mixin: dict):
    c = HEADERS.copy()

    for n, v in mixin.items():
        c[n] = v
    
    return c

def _build_url(code="na", endpoint="content", p=None):
    if code not in REIGONS and code not in ROUTES:
        raise ValueError(f"Invalid Route Code: '{code}'")
    else:
        pass

    try:
        end = ENDPOINTS[endpoint]
    except ValueError:
        raise ValueError(f"The endpoint '{endpoint}' does not exist.")

    url = BASE_URL.format(code=code) + end

    return url
