from pydantic import BaseModel
from typing import List


class ScanResult(BaseModel):
    score: int
    decision: str
    matches: List[str]


class FullScanResult(BaseModel):
    request_score: int
    response_score: int
    decision: str
    request_matches: List[str]
    response_matches: List[str]
