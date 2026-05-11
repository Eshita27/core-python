from src.basics.student_utils import get_student_grade

def test_get_student_grade():
    students = {
        "Eshita":"A",
        "Rahul":"B",
        "Priya":"A+"
    }

    result = get_student_grade(students, "Eshita")
    assert result == "A"
    result = get_student_grade(students, "Rahul")
    assert result == "B"
    result = get_student_grade(students, "Priya")
    assert result == "A+"