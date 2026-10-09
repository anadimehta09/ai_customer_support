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

    last_error = None

    for attempt in range(3):
        try:
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

            return SupportResponse.model_validate_json(response.text)

        except Exception as exc:
            last_error = exc

            if attempt < 2:
                time.sleep(2 ** attempt)

    raise RuntimeError(
        f"Gemini API failed after 3 attempts: {last_error}"
    )