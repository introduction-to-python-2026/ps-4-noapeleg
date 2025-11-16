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
    מחזירה מחרוזת עד הספרה הראשונה + המספר הרצוף שמתחיל באותה ספרה.
    אם אין ספרה – מחזירה את כל המחרוזת + 1
    """
    if not formula:
        return "", 1

    for idx, char in enumerate(formula):
        if char.isdigit():
            # מצאנו את הספרה הראשונה
            start_num = idx
            end_num = idx
            while end_num < len(formula) and formula[end_num].isdigit():
                end_num += 1
            number = int(formula[start_num:end_num])
            return formula[:start_num], number

    # אם לא נמצאה ספרה
    return formula, 1
