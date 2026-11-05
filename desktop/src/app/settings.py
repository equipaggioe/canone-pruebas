"""The settings of the test app."""

from pydantic import BaseModel


class Settings(BaseModel):
    """One setting."""

    title: str = "Hello"
