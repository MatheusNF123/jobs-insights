import jobs
from typing import List, Dict


def get_unique_industries(path: str) -> List[str]:
    list_jobs = jobs.read(path)
    industry = [item['industry'] for item in list_jobs]
    # return list(set(industry))
    print(list(set(industry)))
    """Checks all different industries and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique industries
    """
    # raise NotImplementedError

get_unique_industries('data/jobs.csv')