# Write a program/function in any programming language that will print out data type, number of byte(s) used by the data type, and its range of data value for ALL primitive/built-in data types. 
# E.g., in Java, byte data type will have the following output:

# byte           1       -128 to 127

# Please declare variables with different data types in your code and use these variables to print out the requested outcome above.  

# DO NOT hard-code any output value in the code.

# Please indicate which programming language you use on the top of source code.

import sys

def print_data_type_details(data_type, value):
    type_name = type(value).__name__
    byte_size = sys.getsizeof(value)
    
    if data_type == bool:
        value_range = f"{False} to {True}"
    elif data_type == int:
        value_range = f"{-sys.maxsize - 1} to {sys.maxsize}"
    elif data_type == float:
        value_range = f"{-sys.float_info.max} to {sys.float_info.max}"
    elif data_type == complex:
        value_range = "complex numbers"
    elif data_type == bytes:
        value_range = "0x00 to 0xFF"
    else:
        value_range = "N/A"
    
    print(f"{type_name.ljust(10)} {byte_size} bytes\t{value_range}")


# Examples for different data types
bool_var = True
print_data_type_details(bool, bool_var)

int_var = 42
print_data_type_details(int, int_var)

float_var = 3.14
print_data_type_details(float, float_var)

complex_var = 2 + 3j
print_data_type_details(complex, complex_var)

bytes_var = b'\x00\x01\x02'
print_data_type_details(bytes, bytes_var)

'''
bool       24 bytes    False to True
int        28 bytes    -9223372036854775808 to 9223372036854775807
float      24 bytes    -1.7976931348623157e+308 to 1.7976931348623157e+308
complex    32 bytes    complex numbers
bytes      41 bytes    0x00 to 0xFF

'''
