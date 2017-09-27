# CTI 110
# M3HW2 - Software Sales
# Robert Crawford
# 9/18/2017

def main():

# software company sells a package for $99
    userPurchase = int(input("Please enter how many packages you would like to buy; "))

    packageCost = 99
    totalCost = userPurchase * packageCost
    
    if userPurchase < 10:
        print ("You receive no discount")
        print ("The total cost is $", format (totalCost, '.2f'))
                
# quantity 10-19: 10% discount
    elif userPurchase >= 10 and userPurchase < 19:
        discountCost = totalCost * .1
        newTotal = totalCost - discountCost
        print ("You receive a 10% discount")
        print ("The total cost with discount is $", format (newTotal, '.2f'))
                
# quantity 20-49: 20% discount 
    elif userPurchase >= 20 and userPurchase < 49:
        discountCost = totalCost * .2
        newTotal = totalCost - discountCost
        print ("You receive a 20% discount")
        print ("The total cost with discount is $", format (newTotal, '.2f'))
        
# quantity 50-99: 30% discount
    elif userPurchase >= 50 and userPurchase < 99:
        discountCost = totalCost * .3
        newTotal = totalCost - discountCost
        print ("You receive a 30% discount")
        print ("The total cost with discount is $", format (newTotal, '.2f'))
        
# quantity 100+: 40% discount
    elif userPurchase >= 100:
        discountCost = totalCost * .4
        newTotal = totalCost - discountCost
        print ("You receive a 40% discount")
        print ("The total cost with discount is $", format (newTotal, '.2f'))


main()

#print ("The discount is $", format (totalCost, '.2f'))
