from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path) as file:
        dicts = csv.DictReader(file, delimiter=",", quotechar='"')
        lista = [i for i in dicts]
        return lista


def get_unique_job_types(path: str) -> List[str]:
    list_jobs = read(path)
    job_types = [jobs["job_type"] for jobs in list_jobs if jobs["job_type"]]
    return list(set(job_types))


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    filter_job = [
        job_filter
        for job_filter in jobs
        if job_filter["job_type"] == job_type
    ]
    return filter_job
