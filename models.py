from pydantic import BaseModel, Field

class InferenceRequest(BaseModel):
    prompt: str = Field(..., min_length=1, description="Input prompt from the Android client")
    max_tokens: int = Field(100, ge=10, le=500, description="Max token limit for generation")

class InferenceResponse(BaseModel):
    success: bool
    result: str
    tokens_used: int