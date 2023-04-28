from src.pre_built.counter import count_ocurrences


def test_counter():
    numbCountPy = count_ocurrences('data/jobs.csv', 'Python')

    assert numbCountPy == 1639

    numbCountp2 = count_ocurrences('data/jobs.csv', 'python')

    assert numbCountp2 == 1639

    numbCountJv = count_ocurrences('data/jobs.csv', 'Javascript')

    assert numbCountJv == 122

    numbCountjv2 = count_ocurrences('data/jobs.csv', 'javascript')

    assert numbCountjv2 == 122
