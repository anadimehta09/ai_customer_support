from fastapi import FastAPI

from app.routes.support import router


app = FastAPI(
    title="AI Customer Support API"
)

app.include_router(router)


@app.get("/")
def home():
    return {
        "message": "AI Customer Support API is running"
    }