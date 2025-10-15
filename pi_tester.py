'''
@ASSESSME.USERID: az3638
@ASSESSME.AUTHOR: Aisha Zhankina
@ASSESSME.DESCRIPTION: MiniPractical
@ASSESSME.ANALYZE: YES
'''

# The  thecima values of PI
PI_VALUE = "3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"
pi_digits = PI_VALUE[2:]

def pi_tester():
    counter = 0 
    for i in range(len(pi_digits)):
        user_input = (input("Enter the {i+1} digit of pi:"))
        if user_input == pi_digits[i]:
            counter +=1
            print("Enter the next digit")
        else:
            print("Incorrect digit. The correct digit is " pi_digits[i])
            
        

def display_score(score):
    pass

def main():
    pass

if __name__ == "__main__":
    main()