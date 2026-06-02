# agents/crew_agent.py-orchestration file

# print("CREW AGENT START")

from agents.crew_tools import (
    get_candidate_profile,
    find_matching_jobs
)


class CrewAgent:

    def run(
        self,
        candidate_id
    ):

        candidate = get_candidate_profile(
            candidate_id
        )

        if not candidate:

            return {
                "error":
                "Candidate not found"
            }

        jobs = find_matching_jobs(
            candidate
        )

        return {

            "candidate":
            candidate["personal_info"]["name"],

            "total_jobs":
            len(jobs),

            "matches":
            jobs
        }