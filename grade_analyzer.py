def process_scores(students):
    result = {}
    for student, scores in students.items():
        average_score = sum(scores) / len(scores)
        result[student] = round(average_score, 2)
    return result

def classify_grades(averages):
    grade_a = 90
    grade_b = 75
    grade_c = 60
    grades_dict = {}
    for student, score in averages.items():
        if score >= grade_a:
            grades_dict[student] = (score, "A")
        elif score >= grade_b:
            grades_dict[student] = (score, "B")
        elif score >= grade_c:
            grades_dict[student] = (score, "C")
        else:
            grades_dict[student] = (score, "F")
    return grades_dict

def generate_report(classified, passing_avg=70):
    passed_student = 0
    total = len(classified)
    print("===== Student Grade Report =====")
    for student, (average, grade) in classified.items():
        if average >= passing_avg:
            status = "PASS"
            passed_student += 1
        else:
            status = "FAIL"
        print(f"{student:<10}| Avg: {average:.2f} | Grade: {grade} | Status: {status}")
    print("================================")
    print(f"Total Students : {total}")
    print(f"Passed         : {passed_student}")
    print(f"Failed         : {total - passed_student}")
    return passed_student


input_dict = {"Alice": [92, 90, 78], "Bob": [60, 60, 60], "Clara": [90, 90, 90]}
average_score_dict = process_scores(input_dict)
grade_dict = classify_grades(average_score_dict)
passed_students = generate_report(grade_dict,60)