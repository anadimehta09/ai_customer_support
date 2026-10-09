
from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from app.schemas.support import SupportRequest
from app.services.llm_service import analyze_customer_message


router = APIRouter(prefix="/support", tags=["Support"])


@router.post("/chat")
def support_chat(request: SupportRequest):

    return StreamingResponse(
        analyze_customer_message(request.message),
        media_type="text/plain",
    )
