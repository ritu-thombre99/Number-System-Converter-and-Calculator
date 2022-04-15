def convert_scientific_notation(flt):
    flt = flt.replace("e+","PLUS")
    flt = flt.replace("e-","MINUS")
    if 'MINUS' not in flt and "PLUS" not in flt: 
        return flt
    elif "MINUS" in flt:
        str_vals = str(flt).split('MINUS')
        coef = float(str_vals[0])
        exp = int(str_vals[1])
        return_val = ''
        return_val += '0.'
        return_val += ''.join(['0' for _ in range(0, abs(exp) - 1)])
        return_val += str(coef).replace('.', '')
        return return_val.rstrip("0")
    elif "PLUS" in flt:
        str_vals = str(flt).split('PLUS')
        coef = float(str_vals[0])
        exp = int(str_vals[1])
        return_val = ''
        return_val += str(coef).replace('.', '')
        return_val += ''.join(['0' for _ in range(0, abs(exp - len(str(coef).split('.')[1])))])
        return return_val

def check_leading_zeros(expr):
    if not expr:
        return ''
    negative = False
    if expr[0] == "-":
        negative = True
        expr = expr[1:]
    numbers = expr.replace("+"," ")
    numbers = numbers.replace("-"," ")
    numbers = numbers.replace("/"," ")
    numbers = numbers.replace("*"," ")
    numbers = numbers.split(" ")
    for n in numbers:
        if n in expr:
            new_n = n.lstrip("0")
            if new_n == "":
                new_n = "0"
            if new_n == ".":
                new_n = "0"
            if len(new_n)>1 and new_n[0] == ".":
                new_n = "0"+new_n
            expr = expr.replace(n,new_n)
            
    if negative:
        expr = "-"+expr
    return expr

def is_decimal_valid(expr):
    if "+" not in expr and "-" not in expr and "/" not in expr and "*" not in expr and "." not in expr:
        return True
    if ("+" not in expr and "-" not in expr and "/" not in expr and "*" not in expr) and "." in expr:
        return False
    last_decimal = len(expr) - 1
    while expr[last_decimal] not in ["+","-","*","/"]:
        last_decimal = last_decimal - 1
    is_fraction = True
    for i in range(last_decimal+1,len(expr)):
        if expr[i] == ".":
            return False
    return True

def check_length(expr, base):
    if not expr:
        return True
    base_dict = {2:52,8:16,10:14,16:13}
    operations = ['+','-','/','*']
    if "+" not in expr and "-" not in expr and "/" not in expr and "*" not in expr:
        if "." not in expr:
            expr = check_leading_zeros(expr)
            num_digits = len(expr)
            if num_digits >= base_dict[base]:
                return False
            else:
                return True
        else:
            return True
        
    else:
        index = len(expr)-1
        while expr[index] not in operations:
            index = index - 1
        num_to_check = expr[index+1:]
        num_to_check = check_leading_zeros(num_to_check)
        if '.' in num_to_check:
            return True
        else:
            num_digits = len(num_to_check)
            if num_digits >= base_dict[base]:
                return False
            else:
                return True

def check_sanity(expr):
    allowed = ['+','-','/','*','.']
    for i in range(10):
        allowed.append(str(i))
    expr = list(expr)
    for e in expr:
        if e not in allowed:
            return False
    return True