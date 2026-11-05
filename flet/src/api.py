"""The HTTP client of the test app."""

import httpx
from pydantic import BaseModel


class Reply(BaseModel):
    """One reply."""

    status: int


def fetch(url: str) -> Reply:
    """Get one URL."""
    return Reply(status=httpx.get(url, timeout=10).status_code)
