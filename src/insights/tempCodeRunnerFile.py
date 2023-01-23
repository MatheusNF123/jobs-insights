from typing import Union, List, Dict
import src.insights.jobs as jobs

def get_max_salary(path: str) -> int:
    list_jobs = jobs.read(path)
    salary = [item['max_salary'] for item in list_jobs if item['max_salary']]
    print(salary)
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """
    raise NotImplementedError

get_max_salary('data/jobs.csv')