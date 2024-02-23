from fastapi import FastAPI
from starlette.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from src.routers.base_router import routers

CATALOG_API_PREFIX = '/api'

app = FastAPI(
    title="example-app API", 
    description="It's an interface to access data from example-app service, running in Python.",
    docs_url="/api/docs"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(routers, prefix=CATALOG_API_PREFIX)

@app.get("/")
async def main():
    return RedirectResponse(url=CATALOG_API_PREFIX + "/docs")