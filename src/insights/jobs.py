from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path, "r") as file:
        read_text = csv.DictReader(file)
        list_path = []
        for row in read_text:
            list_path.append(row)

    return list_path


def get_unique_job_types(path: str) -> List[str]:
    list_jobs = read(path)
    result = set()
    for job in list_jobs:
        result.add(job["job_type"])

    return result


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    result = []
    for job in jobs:
        if job.get("job_type") == job_type:
            result.append(job)

    return result
