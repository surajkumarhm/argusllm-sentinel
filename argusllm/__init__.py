"""
ArgusLLM — lightweight LLM API security layer.

Library usage
-------------
    from argusllm import scan_request, scan_response, scan

    result = scan_request("ignore previous instructions")
    # ScanResult(score=30, decision='ALLOW_LOG', matches=['PROMPT_INJECTION'])

    result = scan_response("Here is your API key: sk-abc123...")
    # ScanResult(score=50, decision='WARN', matches=['API_KEY_LEAKAGE'])

    result = scan("user prompt", "model response")
    # FullScanResult(request_score=..., response_score=..., decision=..., ...)

CLI usage
---------
    argusllm serve              # start API server on :8000
    argusllm serve --port 9000  # custom port
    argusllm serve --host 0.0.0.0 --port 8080
"""

from argusllm.schemas import ScanResult, FullScanResult
from argusllm.scorer import compute_score, compute_decision
from argusllm.detectors.injection import scan_request_hits
from argusllm.detectors.secrets import scan_response_hits
from argusllm.detectors.encoding import scan_encoding_hits


def scan_request(content: str) -> ScanResult:
    """Scan a user prompt / LLM request for prompt injection, jailbreaks, and obfuscation."""
    hits = scan_request_hits(content) + scan_encoding_hits(content)
    score = compute_score(hits)
    decision = compute_decision(score)
    matches = list({name for name, _ in hits})
    return ScanResult(score=score, decision=decision, matches=matches)


def scan_response(content: str) -> ScanResult:
    """Scan an LLM response for secrets, PII, and sensitive data leakage."""
    hits = scan_response_hits(content)
    score = compute_score(hits)
    decision = compute_decision(score)
    matches = list({name for name, _ in hits})
    return ScanResult(score=score, decision=decision, matches=matches)


def scan(request: str, response: str) -> FullScanResult:
    """Scan both a request and response in one call. Decision reflects the worst of the two."""
    req = scan_request(request)
    res = scan_response(response)
    worst_score = max(req.score, res.score)
    decision = compute_decision(worst_score)
    return FullScanResult(
        request_score=req.score,
        response_score=res.score,
        decision=decision,
        request_matches=req.matches,
        response_matches=res.matches,
    )


__all__ = [
    "scan_request",
    "scan_response",
    "scan",
    "ScanResult",
    "FullScanResult",
]
