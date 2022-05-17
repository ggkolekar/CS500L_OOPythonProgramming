import random
def initiate_problem():
    num1=random.randint(1, 9)
    num2 = random.randint(1, 9)
    print("How much is {0:1d} and {1:1d}?".format(num1, num2))
    return num1 *num2

def check_result():
    #while True:
    product = initiate_problem()
    while True:
        student_input = int(input())
        if student_input == product:
            print("Very Good!")
            break
        else:
            print("No. Please try again.")

def main():check_result()

if __name__ =="__main__":
    main()