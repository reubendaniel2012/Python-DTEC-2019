#Lab 1-2 Question 9
#Reuben Hoogbruin
#reubendaniel2012@gmail.com

# The lines of text you need to use to generate the output are given below for you.  Do not alter anything inside the quotes.
# "Please enter your first name: "
# "Hi "
# ", pleased to meet you."
# "Please enter your age: "
# "I see you are "
# " years old."
# "In two years you will be "
# " years old."

two_years = 2
first_name = input("Please enter your first name: ")
print("Hi ", first_name, ", pleased to meet you.", sep='')
user_age = input("Please enter your age: ")
print("I see you are ", int(user_age), " years old.", sep='')
print("In two years you will be ", int(user_age) + int(two_years), " years old.", sep='')

