
import time

from google import genai
from google.genai import types

from app.core.config import settings
from app.prompts.support_prompts import SYSTEM_PROMPT


client = genai.Client(
    api_key=settings.gemini_api_key,
    http_options=types.HttpOptions(
        timeout=30_000
    )
)


def analyze_customer_message(message: str):
    last_error = None

    for attempt in range(3):
        try:
            response = client.models.generate_content_stream(
                model=settings.model_name,
                contents=message,
                config=types.GenerateContentConfig(
                    system_instruction=SYSTEM_PROMPT
                )
            )

            for chunk in response:
                if chunk.text:
                    yield chunk.text
                if chunk.usage_metadata:
                    print("Token usage:", chunk.usage_metadata)

            return

        except Exception as exc:
            last_error = exc

            if attempt < 2:
                time.sleep(2 ** attempt)

    raise RuntimeError(
        f"Gemini API failed after 3 attempts: {last_error}"
    )
