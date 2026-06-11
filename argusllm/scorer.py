from typing import List, Tuple
from argusllm.config import SCORE_ALLOW, SCORE_ALLOW_LOG, SCORE_WARN


def compute_score(hits: List[Tuple[str, int]]) -> int:
    raw = sum(weight for _, weight in hits)
    return min(raw, 100)


def compute_decision(score: int) -> str:
    if score < SCORE_ALLOW:
        return "ALLOW"
    elif score < SCORE_ALLOW_LOG:
        return "ALLOW_LOG"
    elif score < SCORE_WARN:
        return "WARN"
    else:
        return "BLOCK"
