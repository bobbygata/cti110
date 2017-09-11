# CTI-110
# M2HW2 - Tip Tax Total
# Robert Crawford
# 9/6/2017

# foodCost, tipAmount, salesTax, totalCost

foodCost = int (input (" Please enter the cost of the meal: "))

tipAmount = 0.18 * foodCost

salesTax = 0.07 * foodCost

totalCost = foodCost + tipAmount + salesTax

print ("The tip cost is $", format(tipAmount, '.2f'))

print ("The sales tax is $", format (salesTax, '.2f'))

print ("The total cost of the meal is $", format (totalCost, '.2f'))
