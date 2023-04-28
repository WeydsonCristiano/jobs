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
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    raise NotImplementedError
