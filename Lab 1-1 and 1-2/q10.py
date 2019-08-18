#Lab 1-2 Question 10
#Reuben Hoogbruin
#reubendaniel2012@gmail.com

# The lines of text you need to use to generate the output are given below for you.  Do not alter anything inside the quotes.
# "Please enter your first name: "
# "Hi "
# ", pleased to meet you."
# " "
# "Please enter the first integer: "
# "Please enter the second integer: "
# "The answer to "
# " + "
# " - "
# " * "
# " / "
# " is "


first_name = input("Please enter your first name: ")
print("Hi ", first_name, ", pleased to meet you.", sep='')
print(" ")
first_integer = input("Please enter the first integer: ")
second_integer = input("Please enter the second integer: ")
print(" ")
print("The answer to ", int(first_integer), " + ", int(second_integer), " is ", int(first_integer)+int(second_integer), sep='')
print("The answer to ", int(second_integer), " + ", int(first_integer), " is ", int(second_integer)+int(first_integer), sep='')
print(" ")
print("The answer to ", int(first_integer), " - ", int(second_integer), " is ", int(first_integer)-int(second_integer), sep='')
print("The answer to ", int(second_integer), " - ", int(first_integer), " is ", int(second_integer)-int(first_integer), sep='')
print(" ")
print("The answer to ", int(first_integer), " * ", int(second_integer), " is ", int(first_integer)*int(second_integer), sep='')
print("The answer to ", int(second_integer), " * ", int(first_integer), " is ", int(second_integer)*int(first_integer), sep='')
print(" ")
print("The answer to ", int(first_integer), " / ", int(second_integer), " is ", int(first_integer)/int(second_integer), sep='')
print("The answer to ", int(second_integer), " / ", int(first_integer), " is ", int(second_integer)/int(first_integer), sep='')
