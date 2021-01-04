student_scores = input('Enter your scores: ')
student_scores = int(student_scores)
if student_scores < 50 :
    print ('Code is F')
elif student_scores <= 59:
    print('Code is D')
elif student_scores <= 69:
    print('Code is C')
elif student_scores <= 89:
    print('Code is B')
elif student_scores <= 100:
    print('Code is A')