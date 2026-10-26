from fastapi import FastAPI, HTTPException
from models import InferenceRequest, InferenceResponse
from services import AIService

app = FastAPI(
    title="Staff Mobile AI Backend",
    version="1.0.0",
    description="High-performance backend designed for native Android integration."
)

ai_service = AIService()


@app.get("/health", tags=["System"])
async def health_check():
    """Health check endpoint for container orchestration and client connectivity."""
    return {"status": "online", "architecture": "Clean Python Architecture"}


@app.post("/api/v1/inference", response_model=InferenceResponse, tags=["AI"])
async def run_inference(payload: InferenceRequest):
    """Executes asynchronous AI inference requested by the mobile client."""
    try:
        response_text = await ai_service.process_inference(payload.prompt, payload.max_tokens)

        return InferenceResponse(
            success=True,
            result=response_text,
            tokens_used=len(payload.prompt.split()) + 15
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))