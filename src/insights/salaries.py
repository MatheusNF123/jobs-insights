from typing import Union, List, Dict

import src.insights.jobs as jobs


def get_max_salary(path: str) -> int:
    list_jobs = jobs.read(path)
    salary = [
        int(item["max_salary"])
        for item in list_jobs
        if item["max_salary"] and item["max_salary"].isnumeric()
    ]

    return max(salary)


def get_min_salary(path: str) -> int:
    list_jobs = jobs.read(path)
    salary = [
        int(item["min_salary"])
        for item in list_jobs
        if item["min_salary"] and item["min_salary"].isnumeric()
    ]

    return min(salary)


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    try:
        max_salary = int(job["max_salary"])
        min_salary = int(job["min_salary"])
        int_salary = int(salary)
    except Exception:
        raise ValueError

    if min_salary > max_salary:
        raise ValueError
    else:
        return min_salary <= int_salary <= max_salary


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
