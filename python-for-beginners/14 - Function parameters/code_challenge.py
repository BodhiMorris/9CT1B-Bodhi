# Create a calculator function
# The function should accept three parameters:
# first_number: a numeric value for the math operation
# second_number: a numeric value for the math operation
# operation: the word 'add' or 'subtract'. The default operation is 'add'
# the function should return the result of the two numbers added or subtracted
# based on the value passed in for the operator
#
def calculate(num1, num2, opp = 'add'):
    if opp == 'add':
        return num1 + num2
    elif opp == 'subtract':
        return num1 - num2
    else:
        return 'I hate you'



# Test your function using named notation passing in only the numbers 6 and 4
# Should return 10

print(calculate(6, 4))

# Test your function using named notation with the values 6,4, subtract 
# Should return 2

print(calculate(6, 4, 'subtract'))

# BONUS: Test your function with the values 6, 4 and divide 
# Have your function return an error message when invalid values are received
