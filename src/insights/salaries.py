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
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    raise NotImplementedError


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    raise NotImplementedError
