import urllib
from urllib.parse import quote

from inference.core.env import LICENSE_SERVER


def wrap_url(url: str) -> str:
    if LICENSE_SERVER:
        return f"http://{LICENSE_SERVER}/proxy?url={quote(url, safe='~()*!''')}"
    return url
