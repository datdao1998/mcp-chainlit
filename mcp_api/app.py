from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_mcp import FastApiMCP

from mcp_api.routers.user import user_router

app = FastAPI()

# Add CORS middleware to allow requests from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(user_router, prefix=f"/user")

mcp = FastApiMCP(
    app,
    name="Demo MCP FastAPI Server",
    describe_all_responses=True,
    describe_full_response_schema=True
)

mcp.mount()
