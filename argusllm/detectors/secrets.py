import regex
from typing import List, Tuple
from argusllm.rules import RESPONSE_RULES


def scan_response_hits(content: str) -> List[Tuple[str, int]]:
    triggered = []

    for rule_name, rule in RESPONSE_RULES.items():
        for pattern in rule["patterns"]:
            try:
                if regex.search(pattern, content, regex.IGNORECASE):
                    triggered.append((rule_name, rule["weight"]))
                    break
            except regex.error:
                if pattern in content:
                    triggered.append((rule_name, rule["weight"]))
                    break

    return triggered
