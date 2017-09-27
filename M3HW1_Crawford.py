# CTI 110
# M3HW1 - Age Classifier
# Robert Crawford
# 9/13/2017

def main():
    
# get the age from person
    userAge = float(input('Please enter your age: '))

# if the person is 1 year old or less, he or she is an infant

    if userAge <= 1:
        print('You are a infant.')

# if the person is older than one year, but younger than 13 years, he or she is a child

    elif userAge > 1 and userAge < 13:
        print ('You are a child.')
    
# if the person is at least 13 years old, but less than 20 years old, he or she is a teenager

    elif userAge  >= 13 and userAge < 20:
        print ('You are a teenager.')
    
# if the person is at least 20 years old, he or she is an adult.

    elif userAge >= 20:
        print ('You are a adult.')

main()
