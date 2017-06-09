import random
import math
def generate_grades(i):
    while i > 0:
        x = int(math.floor(60 + (41*random.random())))
        if 59 < x < 70:
            print "Score: " + str(x) + "; Your grade is D."
        elif 69 < x < 80:
            print "Score: " + str(x) + "; Your grade is C."
        elif 79 < x < 90:
            print "Score: " + str(x) + "; Your grade is B."
        elif 89 < x <= 100:
            print "Score: " + str(x) + "; Your grade is A."
        i = i - 1
    print "End of the program. Bye!"
generate_grades(10)
