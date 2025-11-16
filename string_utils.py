def split_at_first_digit(formula):
    if not formula:
        return "", 1
    for idx, char in enumerate(formula):
        if char.isdigit():
            start = idx
            end = idx
            while end < len(formula) and formula[end].isdigit():
                end += 1
            return formula[:start], int(formula[start:end])
    return formula, 1

def split_before_each_uppercases(formula):
    if not formula:
        return []

    split_formula = []
    start = 0
    for i in range(1, len(formula)):
        if formula[i].isupper():
            split_formula.append(formula[start:i])
            start = i
    split_formula.append(formula[start:])
    return split_formula
