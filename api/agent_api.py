# apply_api.py

# print("AGENT API START")

from fastapi import APIRouter

from agents.crew_agent import (
    CrewAgent
)

router = APIRouter()

agent = CrewAgent()


@router.get(
    "/crew-agent/{candidate_id}"
)
def crew_agent(candidate_id):

    return agent.run(
        candidate_id
    )