from src.pre_built.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    dicttest = {"salary": "2000", "title": "Maquinista", "type": "trainee"}
    assert (
        read_brazilian_file("tests/mocks/brazilians_jobs.csv")[0] == dicttest
    )
    assert len(read_brazilian_file("tests/mocks/brazilians_jobs.csv")) == 15

    try:
        read_brazilian_file("tests/mocks/brazilians_jobsasd.csv")
    except Exception as e:
        assert e
