import pytest
from src.basics.student_utils import get_student_grade

@pytest.mark.parametrize("name, expected",
    [
        ( "Eshita", "A"),
        ( "Rahul", "B"),
        ("Priya", "A+")
    ])

def test_get_student_grade(name, expected):
    students = {
        "Eshita":"A",
        "Rahul":"B",
        "Priya":"A+"
    }

    assert get_student_grade(students,name) == expected