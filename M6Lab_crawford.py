#M6Lab
#CTI 110
#Robert Crawford
#10/25/2017


def main():
    name = input('What is your name? ')
    greet(name)

    age = float(input('What is your age?'))
    print ('You are a', ageCategory(age))

def greet(name):
    print ('Hello', name)

def ageCategory(age):
    answer = 'Unknown'
    if age <= 1:
        answer = 'infant'

    elif age > 1 and age < 13:
        answer = 'child.'
    
    elif age  >= 13 and age < 20:
        answer = 'teenager.'
    
    elif age >= 20:
        answer = 'adult.'

    return answer
    
main()

