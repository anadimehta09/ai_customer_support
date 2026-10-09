from fastapi import APIRouter

from app.schemas.support import SupportRequest, SupportResponse
from app.services.llm_service import analyze_customer_message


router = APIRouter(prefix="/support", tags=["Support"])


@router.post("/chat", response_model=SupportResponse)
def support_chat(request: SupportRequest):

    result = analyze_customer_message(
        request.message
    )

    return result