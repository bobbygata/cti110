#M6HW1 - Test Average and Grades
#CTI 110
#Robert Crawford
#11/01/2017

scoreA = 90
scoreB = 80 
scoreC = 70 
scoreD = 60 
scoreF = 59
    
def main():
    test1 = float(input('Please enter frist test scores?'))
    test2 = float(input('Please enter second test scores?'))
    test3 = float(input('Please enter third test scores?'))
    test4 = float(input('Please enter fourth test scores?'))
    test5 = float(input('Please enter fifth test scores?'))
    total = (test1 + test2 + test3 + test4 + test5)
    print('Your test average is', calc_average(total))
    
    score =float(input('What is your test score?'))
    print('Your Letter grade is: ', determine_grade(score))
    

def calc_average(total):
   return total /5
    

def determine_grade(score):

    answer = 'Unkown'
    if score >= scoreA:
         answer = 'A' 
    elif score >= scoreB and score < scoreA:
         answer = 'B'
    elif score >= scoreC and score < scoreB:
         answer = 'C'
    elif score >= scoreD and score < scoreC:
         answer = 'D'
    elif score <= scoreF:
         answer = 'F'
    return answer


main()
