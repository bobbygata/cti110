#M5HW2 - Running Total
#CTI 110
#Robert Crawford
#10/25/2017

def main():

    runningTotal = 0
    keepGoing = True

    while keepGoing:
        print("Enter a number: ")
        number = int(input('>'))

        if number < 0:
            keepGoing = False

        else:
            runningTotal += number

    print("Total is:", runningTotal)

main()
