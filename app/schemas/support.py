from typing import Literal

from pydantic import BaseModel


class SupportRequest(BaseModel):
    message: str


class SupportResponse(BaseModel):
    category: Literal[
        "PAYMENT",
        "DELIVERY",
        "REFUND",
        "COMPLAINT",
        "OTHER"
    ]

    priority: Literal[
        "LOW",
        "MEDIUM",
        "HIGH"
    ]

    needs_human: bool

    response: str