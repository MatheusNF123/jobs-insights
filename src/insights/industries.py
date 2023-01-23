from typing import List, Dict
import src.insights.jobs as jobs


def get_unique_industries(path: str) -> List[str]:
    list_jobs = jobs.read(path)
    industry = [item["industry"] for item in list_jobs if item["industry"]]
    return list(set(industry))
    # raise NotImplementedError


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    filter_industry = [
        industry_filter
        for industry_filter in jobs
        if industry_filter["industry"] == industry
    ]
    return filter_industry
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    raise NotImplementedError
