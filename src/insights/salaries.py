from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    list_salary = read(path)
    resp = []
    for sal in list_salary:
        if sal["max_salary"] and sal["max_salary"].isdigit():
            resp.append(int(sal["max_salary"]))
    return max(resp, default=0)


def get_min_salary(path: str) -> int:
    list_salary = read(path)
    resp = []
    for sal in list_salary:
        if sal["min_salary"] and sal["min_salary"].isdigit():
            resp.append(int(sal["min_salary"]))
    return min(resp, default=0)


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    try:
        if int(job["min_salary"]) > int(job["max_salary"]):
            raise ValueError
        return int(job["min_salary"]) <= int(salary) <= int(job["max_salary"])
    except TypeError:
        raise ValueError
    except KeyError:
        raise ValueError


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:
    job_list = []
    for row in jobs:
        try:
            compare = matches_salary_range(row, salary)
            if compare:
                job_list.append(row)
        except ValueError:
            print("error")

    return job_list
