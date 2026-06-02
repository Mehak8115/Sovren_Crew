# crew_tools.py

# print("CREW TOOLS START")

from database.candidate_repository import (
    get_candidate
)

from application.apply_matcher import (
    apply_for_jobs
)

from skill_gap.advanced_gap_analyzer import (
    analyze_gap
)


def get_candidate_profile(candidate_id):

    return get_candidate(candidate_id)


def find_matching_jobs(candidate):

    return apply_for_jobs(candidate)


def analyze_job_gap(candidate, job):

    return analyze_skill_gap(
        candidate,
        job
    )