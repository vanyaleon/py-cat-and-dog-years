from app.main import get_human_age


def test_human_age_first_15age():
    assert get_human_age(18, 18) == [1, 1]


def test_human_age_next_9age():
    assert get_human_age(27, 27) == [2, 2]


def test_human_age_next_extra_4age_for_cat():
    assert get_human_age(28, 28) == [3, 2]


def test_human_age_next_extra_5age_for_dog():
    assert get_human_age(30, 30) == [3, 3]
