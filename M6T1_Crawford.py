#M6t1 - kilometer converter
#CTI 110
#Robert Crawford
#10/25/2017

CONVERSION_FACTOR = 0.6214

def main():
    # get the distance in kilometers
    kilometers = float(input('Enter a distance in kilometers: '))

    # display the distance converted to miles
    show_miles(kilometers)

def show_miles(km):
    # Calcuulate miles
    miles = km * CONVERSION_FACTOR
    
    # Display the miles
    print (km, 'kilometers equals', format(miles, '.2f') , 'miles.' )


main()
