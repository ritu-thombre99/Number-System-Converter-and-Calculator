from helper import *
from base2ops import *

def octal_conversions(octal, base):
    negative = False
    if octal[0] == "-":
        negative = True
        octal = octal[1:]

    octal_hash = {}
    for i in range(8):
        octal_hash[i] = bin(i)[2:]
        while len(octal_hash[i]) != 3:
            (octal_hash[i]) = "0" + (octal_hash[i])

    binary = None
    # first convert to decimal
    int_part, frac_part = None,None
    if octal.isdigit():
        int_part = ''
        for digit in octal:
            int_part = int_part + octal_hash[int(digit)]
        binary = int_part
        binary = binary.lstrip("0")
        if binary == "":
            binary = "0"
        if negative:
            binary = "-1"+binary
    else:
        octal_int_part, octal_frac_part = (str(octal).split("."))[0],(str(octal).split("."))[1]
        int_part = ''
        for digit in octal_int_part:
            int_part = int_part + octal_hash[int(digit)]

        frac_part = ''
        for digit in octal_frac_part:
            frac_part = frac_part + octal_hash[int(digit)]

        binary = int_part + "." + frac_part
        binary = binary.lstrip("0")
        if binary == "" or binary[0] == ".":
            binary = "0" + binary
        if negative:
            binary = "-1"*+binary
    if base != 2:
        return binary_conversions(binary, base)
    else:
        return binary
    
def parse_octal_string(to_parse, octal, octal_to_add, base):
    operations = ["+","-","*","/"]
    if to_parse == "":
        return octal_conversions(octal_to_add,base)
    elif to_parse and to_parse[-1] in operations:
        return to_parse+octal_conversions(octal_to_add,base)
    elif "+" not in to_parse and "-" not in to_parse and "/" not in to_parse and "*" not in to_parse:
        return octal_conversions(octal + octal_to_add, base)
    else:
        to_parse = to_parse.replace("e+","PLUS")
        to_parse = to_parse.replace("e-","MINUS")

        octal = octal.replace("e+","PLUS")
        octal = octal.replace("e-","MINUS")

        to_convert = ''
        i = len(octal) - 1
        while octal[i] not in operations:
            to_convert = octal[i] + to_convert
            i = i - 1
        to_add = octal_conversions( convert_scientific_notation(to_convert + octal_to_add), base)
        i = len(to_parse) - 1
        while to_parse[i] not in operations:
            i = i - 1
        return convert_scientific_notation(to_parse[:i+1] + to_add)

    
def parse_octal_backspace(to_parse, octal ,base):
    if octal == "":
        return ""
    if to_parse[-1] in ["+","-","*","/"] and octal[-1] not in ["+","-","*","/"]:
        return to_parse[:-1]
    if to_parse[-1] not in ["+","-","*","/"] and octal[-1] in ["+","-","*","/"]:
        while to_parse[-1] not in ["+","-","*","/"]:
            to_parse = to_parse[:-1]
        return to_parse
    elif "+" not in to_parse and "-" not in to_parse and "/" not in to_parse and "*" not in to_parse:
        return octal_conversions(octal, base)
    else:
        to_parse = to_parse.replace("e+","PLUS")
        to_parse = to_parse.replace("e-","MINUS")

        octal = octal.replace("e+","PLUS")
        octal = octal.replace("e-","MINUS")
        to_convert = ''
        i = len(octal) - 1
        operations = ["+","-","*","/"]
        while octal[i] not in operations:
            to_convert = octal[i] + to_convert
            i = i - 1
        converted_value = octal_conversions( convert_scientific_notation(to_convert), base)
        i = len(to_parse) - 1
        operations = ["+","-","*","/"]
        while to_parse[i] not in operations:
            i = i - 1
        return convert_scientific_notation(to_parse[:i+1]+converted_value)






