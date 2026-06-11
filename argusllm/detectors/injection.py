import regex
from typing import List, Tuple
from argusllm.rules import REQUEST_RULES


def scan_request_hits(content: str) -> List[Tuple[str, int]]:
    triggered = []
    content_lower = content.lower()

    for rule_name, rule in REQUEST_RULES.items():
        for pattern in rule["patterns"]:
            try:
                if regex.search(pattern, content_lower, regex.IGNORECASE):
                    triggered.append((rule_name, rule["weight"]))
                    break
            except regex.error:
                if pattern.lower() in content_lower:
                    triggered.append((rule_name, rule["weight"]))
                    break

    return triggered
