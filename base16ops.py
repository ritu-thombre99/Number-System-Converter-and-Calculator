from helper import *
from base2ops import *

def hex_conversions(hex, base):
    negative = False
    if hex[0] == "-":
        negative = True
        hex = hex[1:]
    

    hex_hash = {}
    for i in range(16):
        hex_hash[i] = bin(i)[2:]
        while len(hex_hash[i]) != 4:
            (hex_hash[i]) = "0" + (hex_hash[i])

    binary = None
    # first convert to decimal
    int_part, frac_part = None,None
    if "." not in hex:
        int_part = ''
        for digit in hex:
            if digit.isdigit():
                int_part = int_part + hex_hash[int(digit)]
            else:
                int_part = int_part + hex_hash[ord(digit)-55]
        binary = int_part
        binary = binary.lstrip("0")
        if binary == "":
            binary = "0"
        if negative:
            binary = "-1"+binary
    else:
        hex_int_part, hex_frac_part = (str(hex).split("."))[0],(str(hex).split("."))[1]
        int_part = ''
        for digit in hex_int_part:
            if digit.isdigit():
                int_part = int_part + hex_hash[int(digit)]
            else:
                int_part = int_part + hex_hash[ord(digit)-55]

        frac_part = ''
        for digit in hex_frac_part:
            if digit.isdigit():
                frac_part = frac_part + hex_hash[int(digit)]
            else:
                frac_part = frac_part + hex_hash[ord(digit)-55]

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
    
def parse_hex_string(to_parse, hex, hex_to_add, base):
    operations = ["+","-","*","/"]
    if to_parse == "":
        return hex_conversions(hex_to_add,base)
    elif to_parse and to_parse[-1] in operations:
        return to_parse+hex_conversions(hex_to_add,base)
    elif "+" not in to_parse and "-" not in to_parse and "/" not in to_parse and "*" not in to_parse:
        return hex_conversions(hex + hex_to_add, base)
    else:
        to_parse = to_parse.replace("e+","PLUS")
        to_parse = to_parse.replace("e-","MINUS")

        hex = hex.replace("e+","PLUS")
        hex = hex.replace("e-","MINUS")

        to_convert = ''
        i = len(hex) - 1
        while hex[i] not in operations:
            to_convert = hex[i] + to_convert
            i = i - 1
        to_add = hex_conversions( convert_scientific_notation(to_convert + hex_to_add), base)
        i = len(to_parse) - 1
        while to_parse[i] not in operations:
            i = i - 1
        return convert_scientific_notation(to_parse[:i+1] + to_add)

    
def parse_hex_backspace(to_parse, hex ,base):
    if hex == "":
        return ""
    if to_parse[-1] in ["+","-","*","/"] and hex[-1] not in ["+","-","*","/"]:
        return to_parse[:-1]
    if to_parse[-1] not in ["+","-","*","/"] and hex[-1] in ["+","-","*","/"]:
        while to_parse[-1] not in ["+","-","*","/"]:
            to_parse = to_parse[:-1]
        return to_parse
    elif "+" not in to_parse and "-" not in to_parse and "/" not in to_parse and "*" not in to_parse:
        return hex_conversions(hex, base)
    else:
        to_parse = to_parse.replace("e+","PLUS")
        to_parse = to_parse.replace("e-","MINUS")

        hex = hex.replace("e+","PLUS")
        hex = hex.replace("e-","MINUS")
    
        to_convert = ''
        i = len(hex) - 1
        operations = ["+","-","*","/"]
        while hex[i] not in operations:
            to_convert = hex[i] + to_convert
            i = i - 1
        converted_value = hex_conversions( convert_scientific_notation(to_convert), base)
        i = len(to_parse) - 1
        operations = ["+","-","*","/"]
        while to_parse[i] not in operations:
            i = i - 1
        return convert_scientific_notation(to_parse[:i+1]+converted_value)
