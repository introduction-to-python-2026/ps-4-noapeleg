def split_before_each_uppercases(formula):
    """
    מחלקת מחרוזת לרשימה של תת-מחרוזות, כך שכל תת-מחרוזת מתחילה באות גדולה (אם יש),
    ומסיימת לפני האות הגדולה הבאה או לפני ספרה.
    מחזירה רשימה של מחרוזות ורצף המספר האחרון אם קיים.
    """
    if not formula:
        return [], 1  # מחרוזת ריקה

    # בידוד המספר האחרון אם המחרוזת מסתיימת בספרות
    number = 1
    for i in range(len(formula) - 1, -1, -1):
        if formula[i].isdigit():
            continue
        else:
            if i < len(formula) - 1:
                number = int(formula[i + 1:])
                formula = formula[:i + 1]
            break

    # חלוקה לפני כל אות גדולה
    result = []
    start = 0
    for i in range(1, len(formula)):
        if formula[i].isupper():
            result.append(formula[start:i])
            start = i
    result.append(formula[start:])  # הוספת החלק האחרון

    return result, number


def split_at_first_digit(formula):
    """
    מחזירה מחרוזת עד הספרה הראשונה במספר + המספר שנמצא אחרי.
    אם אין ספרה – מחזירה את כל המחרוזת + 1
    """
    if not formula:
        return "", 1

    if len(formula) == 1:
        if formula[0].isdigit():
            return "", int(formula[0])
        else:
            return formula, 1

    # חיפוש הספרה הראשונה
    digit_location = len(formula)  # ברירת מחדל – אין ספרה
    for idx, char in enumerate(formula):
        if char.isdigit():
            digit_location = idx
            break

    if digit_location == len(formula):
        return formula, 1  # אין ספרה במחרוזת
    else:
        return formula[:digit_location], int(formula[digit_location:])
