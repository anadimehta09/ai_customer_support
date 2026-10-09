import time

from google import genai
from google.genai import types

from app.core.config import settings
from app.prompts.support_prompts import SYSTEM_PROMPT
from app.schemas.support import SupportResponse


client = genai.Client(
    api_key=settings.gemini_api_key
)


def analyze_customer_message(message: str) -> SupportResponse:

    response = client.models.generate_content(
                model=settings.model_name,
                contents=f"""
                {SYSTEM_PROMPT}

                Customer message:
                {message}
                """,
                config=types.GenerateContentConfig(
                    response_mime_type="application/json",
                    response_schema=SupportResponse,
                ),
            )

          