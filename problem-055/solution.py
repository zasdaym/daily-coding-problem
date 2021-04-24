from typing import Dict, Set
from random import choice
from string import ascii_letters, digits


class Shortener:
    def __init__(self):
        self.url_by_shortened: Dict[str, str] = {}

    def shorten(self, url: str) -> str:
        if url in self.url_by_shortened:
            return self.url_by_shortened[url]

        short_url = random_alphanumeric(6)
        self.url_by_shortened[short_url] = url
        return short_url

    def restore(self, short_url: str):
        return self.url_by_shortened.get(short_url, "")


def random_alphanumeric(length: int) -> str:
    return "".join(choice(ascii_letters + digits) for _ in range(length))
