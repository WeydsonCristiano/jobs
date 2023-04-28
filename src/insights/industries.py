from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    list_industry = read(path)
    result = set()
    for ind in list_industry:
        industria = ind["industry"].strip()
        if industria:
            result.add(ind["industry"])

    return result


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    result = []
    for job in jobs:
        if job["industry"] == industry:
            result.append(job)

    return result
