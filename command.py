import random

son=random.randint(1,10)
while True:
    user_answer=int(input('Son taxmin qiling'))
    if user_answer==son:
        print('Sonni topdingiz')
    else:
        print('Xato qildingiz')