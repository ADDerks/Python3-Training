# Assign initial variables.
# description of store item and price
lovely_loveseat_description = '''
Lovely Loveseat. Tufted polyester blend on wood. 
32 inches high x 40 inches wide x 30 inches deep. 
Red or white.
'''
lovely_loveseat_price = 254.00
# description of second piece and price
stylish_settee_description = '''
Stylish Settee. Faux leather on birch. 
29.50 inches high x 54.75 inches wide x 28 inches deep. 
Black.
'''
stylish_settee_description = 180.50
# desc. of third piece and price
luxurious_lamp_description = '''
Luxurious Lamp. Glass and iron. 
36 inches tall. 
Brown with cream shade.
'''
luxurious_lamp_price = 52.15

# variable for sales tax
sales_tax = .088

#customer one is shopping. Variables for total and items seletcted is zeroed-out.
customer_one_total = 0
customer_one_itemization = ""
# customer wants to buy loveseat
customer_one_total += lovely_loveseat_price
# add description to their items list
customer_one_itemization += lovely_loveseat_description
# wants to buy lamp too.
customer_one_total += luxurious_lamp_price
# add desc. to items list.
customer_one_itemization += luxurious_lamp_description
# create variable for customer order sales tax.
customer_one_tax = customer_one_total * sales_tax
# add sales tax to customer total cost
customer_one_total = customer_one_tax + customer_one_total
# start printing the reciept and items.
print("Customer One Items:")
print(customer_one_itemization)
print("Customer One Total:")
# Use round() function to set float value to only show two digits after decimal.
# with round(), must use another digit (like 2 in this case) to signal how many digits.
print(round(customer_one_total, 2))

# complete