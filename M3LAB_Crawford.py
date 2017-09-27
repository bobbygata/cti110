# I was supposed to put a comment here
# CTI 110
# M3LAB
# Robert Crawford
# 9/13/2017

def main():
    # This program takes a number grade and outputs a letter grade.

    # system uses 10-point grading scale
    scoreA = 90
    scoreB = 80 
    scoreC = 70 
    scoreD = 60 
    scoreF = 59
    # TO DO: define the rest of the scores

    
    score = float (input('Please enter your grade: '))

    if score >= scoreA:
        print('Your grade is: A')
    elif score >= scoreB and score < scoreA:
         print('Your grade is: B')
    elif score >= scoreC and score < scoreB:
         print('Your grade is: C')
    elif score >= scoreD and score < scoreC:
         print('Your grade is: D')
    elif score <= scoreF:
         print('Your grade is: F')

    # TO DO: finish this



# program start
main()
