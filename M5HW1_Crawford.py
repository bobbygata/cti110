#M5HW1 - Distance traveled
#CTI 110
#Robert Crawford
#10/16/2017



def main():

    vehicleSpeed = float(input("What is the speed of the vehicle in mph?: "))

    timeTraveled = int(input("How many hours has it traveled?: "))

    print("Hour","\tDistance")
    print('----------------')
    for currentHour in range(1, timeTraveled + 1):
        distanceTraveled = vehicleSpeed * currentHour
        print(currentHour,"\t",distanceTraveled)
                  

main()
