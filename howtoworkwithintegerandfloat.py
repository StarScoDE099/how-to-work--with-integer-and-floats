#INTEGER(ARE WHOLE NUMBERS WITHOUT DECIMAL POINT AND ITS NEGATIVE OR POSITIVE)

#INTEGER ADDITION.

my_int_1 = 56
my_int_2 = 12

sum_ints = my_int_1 + my_int_2
print('integer Addition:',sum_ints)

Addition= 56 +12
print('Integer Addition:',Addition)

Addition_1 = 56
Addition_2 = 12

sum_add = Addition_1 + Addition_2

print('Integer Addition: ',sum_add)


#SUBTRACTION WITH INTEGER

my_int_1 =56
my_int_2 = 12

sub_ints = my_int_1 - my_int_2

print('Integer Subtraction:', sub_ints)

subtraction_1 = 56
subtraction_2 = 12
sum_sub = subtraction_1 -subtraction_2
print('Integer subtraction : ' ,sum_sub)

#OR

subtract = 56 - 12
print('Integer Subtract :',subtract)

#MULTIPLICATION WITH INTEGER

my_int_1 =12
my_int_2 =4

product_int = my_int_1 * my_int_2
print('Integer Multiplication : ' , product_int)

#OR

multiply = 12 * 4
print('Integer Multiplication : ' , multiply)

#DIVISION 

my_int_1 = 56
my_int_2 = 12

div_ints = my_int_1/my_int_2
print('Integer Division :',div_ints)

# OR

division = 56 / 12
print('Integer Division :',division)

#FLOATS (ARE POSITIVE OR NEGATIVE NUMBERS WITH DECIMAL POINTS)

#ADDITION OF FLOATS

my_float_1 = 5.6
my_float_2 = 12.0

float_addition = my_float_1 + my_float_2
print('Float Additon:',float_addition)

#OR

Add_float = 5.6 + 12.0
print('Float Addition:', Add_float)

#SUBTRACTION OF FLOAT
my_float_1 = 5.4
my_float_2 = 12.0

float_subtract = my_float_2 - my_float_1
print('Float subtraction:',float_subtract)

#OR

Sub_float = 12.0 - 5.4
print('Float subtraction:' ,Sub_float)


#MULTIPLICATION OF FLOATS
my_float_1 = 5.4
my_float_2 = 120

float_multipy = my_float_1 * my_float_2
print('Float Multiplication:',float_multipy)

#OR

float_multipy = 5.4 * 12.0
print('Float Multiplication:', float_multipy)

#DIVISION OF FLOAT

my_float_1 = 5.4
my_float_2 = 12.0

float_divisison = my_float_2 / my_float_1
print('Float Division :',float_divisison)

#OR

Float_div = 12.0 / 5.4

print('Float Division:',Float_div)

#ADDING OF INTEGER AND FLOATS

my_int =56
my_float = 5.4

sum_int_and_float = my_int + my_float
print (sum_int_and_float)

#OR

sum_int_and_float = 56 + 5.4
print(sum_int_and_float )

#MODULO (FINDING THE REMAINDER BTW TWO VALUS OR NUMERS)

my_int_1 = 56
my_int_2 =12

mod_int = my_int_1 % my_int_2
print('Integer Modulos:',mod_int)

#OR

mod_ints = 56 % 12
print('Integer Modulo:',mod_int)

my_float_1 = 5.4
my_float_2 =12.0

mod_float = my_float_2 % my_float_1
print('Float Modulo:',mod_float)

#OR

mod_float = 12.0 % 5.4
print('Float Modulo:',mod_float)


#FLOOR DIVISION(DIVIDES TWO NUMBERS AND RETURNS THE GREATESTINTEGER LESS OR EQUAL TO THE RESULT)
my_int_1 = 56
my_int_2 = 12

floor_div_int = my_int_1 // my_int_2

print('Integer Floor Division:',floor_div_int)

#OR

floor_div = 56 // 12
print('Integer Floor Division:',floor_div)

my_float_1 = 5.4
my_float_2 =12.0
floor_div_float = my_float_2 // my_float_1
print('float Floor Division:',floor_div_float)

#OR

floor_div_float = 12.0 // 5.4
print('Float floor Division:',floor_div_float)

#EXPONENTION (RAISES A NUMBER TO THE POWER OF ANOTHER AND IS DONE WITH THE DOUBLE ASTERISK OPERATOR(**))
my_int_1 = 56
my_int_2 = 12
exp_ints =my_int_1 ** my_int_2 
print('Integer Exponentiation:',exp_ints)

#OR 

exp_ints = 56 ** 12
print('Integer Exponentiation:',exp_ints)

my_float_1 = 5.4
my_float_2 =12.0
exp_floats = my_float_1 **my_float_2 
print('Float Exponentiation:',exp_floats)

#OR

exp_floats = 5.4 ** 12.0
print('Float Exponentiation:',exp_floats)


#FLOAT() RETURNS THE FLOATING-POINT NUMBER CONSTRUCTED FROM THE GIVEN NUMBER
my_int_1 = 56
my_float_1 = float(my_int_1)

print(my_float_1)

#INT()FUNCTION RETURNS AN INTEGER CONSTRUCTED FROM THE GIVEN NUMBER
my_float = 12.92563
my_int = int(my_float)

print(my_int)


#CONVERT STRING INTO EITHER FLOAT OR INTEGER
my_str_int ='45'
my_float_int = '7.5'

converted_int = int(my_str_int)
converted_float = float(my_float_int)

print(converted_int,type(converted_int))
print(converted_float)

#ROUND()ROUND A NUMBER TO THE SPECIFIED NUMBER OF DECIMAL POINT.
my_int_1 = 4.798
my_int_2 = 4.253

rounded_int_1 =round(my_int_1)
rounded_int_2 = round(my_int_2,1)

print(rounded_int_1)
print(rounded_int_2)

#ABS() RETURNS THE ABSOLUTE VALUE OF ANUMBER

num = -15

absolute_value = abs(num)
print(absolute_value)

#OR
print(abs(num))

#POWER():RAISES A NUMBER TO THE POWER OF ANOTHER OR PERFORMS MODULAR EXPONENTIATION
result_1 = pow(2,3)
print(result_1)

result_2 = pow(2,3,5)
print(result_2)


