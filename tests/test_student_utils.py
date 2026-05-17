import pytest
from src.basics.student_utils import get_student_grade
from tests.test_data.student_data import student_grade_data

@pytest.mark.parametrize("name, expected",
    student_grade_data)

@pytest.mark.regression
def test_get_student_grade_from_fixtures(students, name, expected):
    assert get_student_grade(students, name) == expected

@pytest.mark.negative
def test_invalid_student(students):
    assert get_student_grade(students, "NonExistentStudent") is None