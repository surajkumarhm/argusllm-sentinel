import regex
from typing import List, Tuple
from argusllm.config import MAX_INPUT_LENGTH

BASE64_PATTERN = r"[A-Za-z0-9+/]{60,}={0,2}"


def scan_encoding_hits(content: str) -> List[Tuple[str, int]]:
    triggered = []

    if len(content) > MAX_INPUT_LENGTH:
        triggered.append(("EXCESSIVE_LENGTH", 20))

    if regex.search(BASE64_PATTERN, content):
        triggered.append(("BASE64_PAYLOAD", 15))

    return triggered
