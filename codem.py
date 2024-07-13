import random
import time

OPERATORS = ["+", "-", "*"]
MIN_OPERAND = 3
MAX_OPERAND = 15
NO_PROBLEMS = 10


def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MIN_OPERAND)
    operator = random.choice(OPERATORS)

    expr = str(left) + " " + operator + " " + str(right)
    answer = eval(expr)
    return expr, answer

wrong = 0
print("press enter to start!")
print("________________________")

start = time.time()


for i in range(NO_PROBLEMS):
    expr, answer = generate_problem()
    while True:
         guess = input("problem #" + str( i + 1) + " " + ":" +  " " + expr + "=" + " ")
         if guess == str(answer):
           break
         else:
             print("sorry, you mistaken!!!")
         wrong += 1

end = time.time()
interval = round(start - end, 2)


print("_________________________")
print("you mistaken : ", wrong, "times")
print("Nice  work!, you finished in", interval , "seconds")




