from src.pre_built.sorting import sort_by


def test_sort_by_criteria():
    mock = [
        {
            "id": 1,
            "modulo": "Front end",
            "min_salary": 3000,
            "max_salary": 5000,
            "date_posted": "2021-01-01",
        },
        {
            "id": 2,
            "modulo": "back end",
            "min_salary": 5000,
            "max_salary": 7000,
            "date_posted": "2020-01-02",
        },
        {
            "id": 3,
            "modulo": "cs",
            "min_salary": 4500,
            "max_salary": 6000,
            "date_posted": "2019-01-03",
        },
    ]

    min_cres = [mock[0], mock[2], mock[1]]
    max_dec = [mock[1], mock[2], mock[0]]
    date_dec = [mock[0], mock[1], mock[2]]

    sort_by(mock, "min_salary")
    assert mock == min_cres

    sort_by(mock, "max_salary")
    assert mock == max_dec

    sort_by(mock, "date_posted")
    assert mock == date_dec
