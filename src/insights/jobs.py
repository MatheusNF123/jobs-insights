from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path) as file:
        dicts = csv.DictReader(file, delimiter=",", quotechar='"')
        lista = [i for i in dicts]
        return lista
    # raise NotImplementedError


def get_unique_job_types(path: str) -> List[str]:
    list_jobs = read(path)
    job_types = [jobs['job_type'] for jobs in list_jobs if jobs['job_type']]
    return list(set(job_types))


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
