from helper import *
from base10ops import *

def binary_conversions(binary, base):
    negative = False
    if binary[0] == "-":
        negative = True
        binary = binary[1:]

    base_10 = None
    # first convert to decimal
    int_part, frac_part = None,None
    if binary.isdigit():
        int_part = 0
        power = 0
        for i in range(len(binary)-1, -1, -1):
            int_part = int_part + int(binary[i])*(2**power)
            power = power + 1
        if negative:
            int_part = -1*int_part
        base_10 = str(int_part)
    else:
        
        binary_int_part, binary_frac_part = (str(binary).split("."))[0],(str(binary).split("."))[1]
        int_part = 0
        power = 0
        for i in range(len(binary_int_part)-1, -1, -1):
            int_part = int_part + int(binary_int_part[i])*(2**power)
            power = power + 1

        frac_part = 0
        for i in range(len(binary_frac_part)):
            frac_part = frac_part + int(binary_frac_part[i])*(2**(-i-1))
        base_10 = int_part + frac_part
        if negative:
            base_10 = -1*base_10
        base_10 = str(base_10)
    if base != 10:
        return decimal_conversions(base_10, base)
    else:
        return base_10
    

def parse_binary_string(to_parse, binary, binary_to_add, base):
    operations = ["+","-","*","/"]
    if to_parse == "":
        return binary_conversions(binary_to_add,base)
    elif to_parse and to_parse[-1] in operations:
        return to_parse+binary_conversions(binary_to_add,base)
    elif "+" not in to_parse and "-" not in to_parse and "/" not in to_parse and "*" not in to_parse:
        return binary_conversions(binary + binary_to_add, base)
    else:
        to_parse = to_parse.replace("e+","PLUS")
        to_parse = to_parse.replace("e-","MINUS")

        binary = binary.replace("e+","PLUS")
        binary = binary.replace("e-","MINUS")

        to_convert = ''
        i = len(binary) - 1
        while binary[i] not in operations:
            to_convert = binary[i] + to_convert
            i = i - 1
        to_add = binary_conversions( convert_scientific_notation(to_convert + binary_to_add), base)
        i = len(to_parse) - 1
        while to_parse[i] not in operations:
            i = i - 1
        return convert_scientific_notation(to_parse[:i+1] + to_add)

    
def parse_binary_backspace(to_parse, binary ,base):
    if binary == "":
        return ""
    if to_parse[-1] in ["+","-","*","/"] and binary[-1] not in ["+","-","*","/"]:
        return to_parse[:-1]
    if to_parse[-1] not in ["+","-","*","/"] and binary[-1] in ["+","-","*","/"]:
        while to_parse[-1] not in ["+","-","*","/"]:
            to_parse = to_parse[:-1]
        return to_parse
    elif "+" not in to_parse and "-" not in to_parse and "/" not in to_parse and "*" not in to_parse:
        return binary_conversions(binary, base)
    else:
        to_parse = to_parse.replace("e+","PLUS")
        to_parse = to_parse.replace("e-","MINUS")

        binary = binary.replace("e+","PLUS")
        binary = binary.replace("e-","MINUS")

        to_convert = ''
        i = len(binary) - 1
        operations = ["+","-","*","/"]
        while binary[i] not in operations:
            to_convert = binary[i] + to_convert
            i = i - 1
        converted_value = binary_conversions( convert_scientific_notation(to_convert), base)
        i = len(to_parse) - 1
        operations = ["+","-","*","/"]
        while to_parse[i] not in operations:
            i = i - 1
        return convert_scientific_notation(to_parse[:i+1]+converted_value)


