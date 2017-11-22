#examples

CURRENT_TAX_RATE = 0.085

def main():
    cost = float(input("Product cost? "))
    finalCost = cost = calc_tax(cost)
    print ('Cost with tax is:', finalCost)

def calc_tax(cost):
    #return cost * 0.085
    tax = cost * CURRENT_TAX_RATE
    return tax


main()


#random numbers

import random

def main():
    for times in range(20):
        ranNum = random.randint(1,10)
        print (ranNum)
