from fastapi import APIRouter

from database.candidate_repository import get_candidate

from application.apply_matcher import (
    apply_for_jobs
)

router = APIRouter()

@router.get("/apply/{candidate_id}")
def apply(candidate_id):

    candidate = get_candidate(
        candidate_id
    )

    if not candidate:

        return {
            "error": "Candidate not found"
        }

    jobs = apply_for_jobs(
        candidate
    )

    eligible_count = len(
        [
            job
            for job in jobs
            if job["eligible"]
        ]
    )

    return {

        "candidate":
        candidate["personal_info"]["name"],

        "eligible_count":
        eligible_count,

        "total_jobs":
        len(jobs),

        "job_matches":
        jobs
    }