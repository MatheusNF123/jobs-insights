def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    for i in list(job):
        print(i)
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
    # raise NotImplementedError


matches_salary_range(
    [
        {"max_salary": 0, "min_salary": 10},
        {"max_salary": 10, "min_salary": 100},
        {"max_salary": -1, "min_salary": 10},
    ],
    100,
)