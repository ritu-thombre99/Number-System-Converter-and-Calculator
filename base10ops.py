from helper import convert_scientific_notation
def decimal_conversions(decimal, base):
    negative = False
    if decimal[0] == "-":
        negative = True
        decimal = decimal[1:]
    int_part, frac_part = None,None
    if decimal.isdigit():
        int_part = int(decimal)
        if base == 2:
            int_part = (bin(int_part))[2:]
        elif base == 8:
            int_part = (oct(int_part))[2:]
        elif base == 16:
            int_part = (hex(int_part))[2:].upper()
        if negative:
            int_part = "-"+int_part
        return int_part
    else:
        int_part, frac_part = int((decimal.split("."))[0]), decimal.split(".")[1]
        frac_part = float("0."+frac_part)

        return_int = None
        if base == 2:
            return_int = (bin(int_part))[2:]
        if base == 8:
            return_int = (oct(int_part))[2:]
        if base == 16:
            return_int = ((hex(int_part))[2:]).upper()
        if negative:
            return_int = "-" + return_int
        
        rep = 30
        return_frac = ''
        hex_dict = {10:"A",11:"B",12:"C",13:"D",14:"E",15:"F"}
        temp = None
        for i in range(rep):
            temp = frac_part*base
            if temp>= base:
                temp = base-1
            mod, frac_part = int(temp), temp-int(temp)
            if base == 16 and mod >= 10:
                return_frac = return_frac + hex_dict[mod]
            else:
                return_frac = return_frac + str(mod)
        return (return_int + "." + (return_frac).rstrip("0"))

def parse_decimal_string(to_parse, decimal, decimal_to_add, base):
    operations = ["+","-","*","/"]
    if to_parse == "":
        return decimal_conversions(decimal_to_add,base)
    elif to_parse and to_parse[-1] in operations:
        return to_parse+decimal_conversions(decimal_to_add,base)
    elif "+" not in to_parse and "-" not in to_parse and "/" not in to_parse and "*" not in to_parse:
        return decimal_conversions(decimal + decimal_to_add, base)
    else:
        to_parse = to_parse.replace("e+","PLUS")
        to_parse = to_parse.replace("e-","MINUS")

        decimal = decimal.replace("e+","PLUS")
        decimal = decimal.replace("e-","MINUS")
        
        to_convert = ''
        i = len(decimal) - 1
        while decimal[i] not in operations:
            to_convert = decimal[i] + to_convert
            i = i - 1
        to_add = decimal_conversions( convert_scientific_notation(to_convert + decimal_to_add), base)
        i = len(to_parse) - 1
        while to_parse[i] not in operations:
            i = i - 1
        return convert_scientific_notation(to_parse[:i+1] + to_add)

    
def parse_decimal_backspace(to_parse, decimal ,base):
    if decimal == "":
        return ""
    if to_parse[-1] in ["+","-","*","/"] and decimal[-1] not in ["+","-","*","/"]:
        return to_parse[:-1]
    if to_parse[-1] not in ["+","-","*","/"] and decimal[-1] in ["+","-","*","/"]:
        while to_parse[-1] not in ["+","-","*","/"]:
            to_parse = to_parse[:-1]
        return to_parse
    elif "+" not in to_parse and "-" not in to_parse and "/" not in to_parse and "*" not in to_parse:
        return decimal_conversions(decimal, base)
    else:
        to_parse = to_parse.replace("e+","PLUS")
        to_parse = to_parse.replace("e-","MINUS")

        decimal = decimal.replace("e+","PLUS")
        decimal = decimal.replace("e-","MINUS")

        to_convert = ''
        i = len(decimal) - 1
        operations = ["+","-","*","/"]
        while decimal[i] not in operations:
            to_convert = decimal[i] + to_convert
            i = i - 1
        converted_value = decimal_conversions( convert_scientific_notation(to_convert), base)
        i = len(to_parse) - 1
        operations = ["+","-","*","/"]
        while to_parse[i] not in operations:
            i = i - 1
        return convert_scientific_notation(to_parse[:i+1]+converted_value)


