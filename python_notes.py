# python course notes and examples.
# to write a function, define the function, then use the name of function.
# Example: def function_name():
			#(Tab) some code...
# example
# def is defining function, function called "greet_customer", then everything after ":" is what is run with the function.
#def greet_customer():
#	print("Welcome to Engrossing Grocers.")
#	print("Today's Special is mandarin oranges.")
#	print("Have fun shopping!")
# call the function. defining the function ends when the indentation is removed. Since the next line (12) is not indented,
# Python won't see it as part of the function above. No semi-colons necessary!
#greet_customer()
# prints greeting lines.

# PARAMETERS: Variables that can be passed into a function (see greet_customer above) when you call it.
# Example given:
def greet_customer(special_item):
	print("Welcome to Engrossing Grocers.")
	print("Today's Special is " + special_item + ".")
	print("Have fun shopping!")
# put what you want displayed as the special item, inside the call for the function's parenthesis. (see below).
greet_customer("peanut butter")
# displays peanut butter into the special of the day message.

def mult_two_add_three(number):
	# number = 5
	print(number * 2 + 3)

# Call mult_two_add_three() here:
mult_two_add_three(0)


