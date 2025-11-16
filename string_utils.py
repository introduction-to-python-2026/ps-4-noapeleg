def split_before_each_uppercases(formula):
    if not formula:
        return [], 1 
    number = 1
    i = len(formula) - 1
    while i >= 0 and formula[i].isdigit():
        i -= 1
    if i < len(formula) - 1:
        number = int(formula[i+1:])
        formula = formula[:i+1]
    result = []
    start = 0
    for i in range(1, len(formula)):
        if formula[i].isupper():
            result.append(formula[start:i])
            start = i
    if start < len(formula):
        result.append(formula[start:])  
    return result, number

def split_at_first_digit(formula):
    if not formula:
        return "",1
    for idx,char in enumerate(formula):
        if char.isdigit():
            start=idx
            end=idx
            while end<len(formula) and formula[end].isdigit():
                end+=1
            return formula[:start],int(formula[start:end])
    return formula,1
