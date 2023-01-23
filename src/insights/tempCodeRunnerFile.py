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
    job_types = [jobs['job_type'] for jobs in list_jobs]
    print(list(set(job_types)))
    """Checks all different job types and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique job types
    """
    # raise NotImplementedError

get_unique_job_types('data/jobs.csv')