# crew.py

from fastapi import FastAPI
from api.resume_api import router as resume_router
from api.matching_api import router as matching_router
from api.skill_gap_api import router as skill_gap_router
from api.apply_api import router as apply_router
# from api.agent_api import router as agent_router

print("ALL IMPORTS DONE")

app = FastAPI(
    title="Sovren Crew Service"
)


@app.get("/")
def home():
    return {"message": "API is running"}

# app.include_router(
#     agent_router,
#     tags=["Agentic AI Agents"]
# )

app.include_router(
    apply_router,
    tags=["Apply For Job"]
)
app.include_router(resume_router)
app.include_router(matching_router)
app.include_router(skill_gap_router)
app.include_router(apply_router)
# app.include_router(agent_router)