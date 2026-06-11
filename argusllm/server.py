import logging
from fastapi import FastAPI
from argusllm import scan_request, scan_response, scan
from argusllm.schemas import ScanResult, FullScanResult
from pydantic import BaseModel

logging.basicConfig(level=logging.INFO, format="[%(levelname)s] %(message)s")
logger = logging.getLogger("argusllm")


# ─── Request bodies ───────────────────────────────────────────────────────────

class RequestScanInput(BaseModel):
    content: str


class ResponseScanInput(BaseModel):
    content: str


class FullScanInput(BaseModel):
    request: str
    response: str


# ─── App ──────────────────────────────────────────────────────────────────────

app = FastAPI(
    title="ArgusLLM",
    description="Lightweight LLM API security layer — deterministic, no AI, no DB.",
    version="1.0.0",
)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/scan/request", response_model=ScanResult)
def api_scan_request(body: RequestScanInput):
    result = scan_request(body.content)
    logger.info("REQUEST score=%d decision=%s matches=%s", result.score, result.decision, ",".join(result.matches))
    return result


@app.post("/scan/response", response_model=ScanResult)
def api_scan_response(body: ResponseScanInput):
    result = scan_response(body.content)
    logger.info("RESPONSE score=%d decision=%s matches=%s", result.score, result.decision, ",".join(result.matches))
    return result


@app.post("/scan", response_model=FullScanResult)
def api_scan_full(body: FullScanInput):
    result = scan(body.request, body.response)
    logger.info(
        "FULL request_score=%d response_score=%d decision=%s",
        result.request_score, result.response_score, result.decision,
    )
    return result
