from typing import Union, List, Dict

import src.insights.jobs as jobs

# import jobs


def get_max_salary(path: str) -> int:
    list_jobs = jobs.read(path)
    salary = [
        int(item["max_salary"])
        for item in list_jobs
        if item["max_salary"] and item["max_salary"].isnumeric()
    ]

    return max(salary)
    # raise NotImplementedError


def get_min_salary(path: str) -> int:
    list_jobs = jobs.read(path)
    salary = [
        int(item["min_salary"])
        for item in list_jobs
        if item["min_salary"] and item["min_salary"].isnumeric()
    ]

    return min(salary)
    raise NotImplementedError


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    try:
        if int(job["min_salary"]) > int(job["max_salary"]):
            raise ValueError
        elif job.get("max_salary") is None and job.get("min_salary") is None:
            raise ValueError
        else:
            return (
                int(job["min_salary"]) <= int(salary) <= int(job["max_salary"])
            )
    except Exception:
        raise ValueError


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:
    arr = []
    for i in jobs:
        try:
            if matches_salary_range(i, salary):
                arr.append(i)
        except ValueError:
            pass
    return arr
