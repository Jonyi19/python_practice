import random
def get_answer(answer_number):
    if answer_number == 1:
        return 'This is One'
    elif answer_number == 2:
        return 'This is Two'
    elif answer_number == 3:
        return '3ですね'
    elif answer_number == 4:
        return 'これは4です'
    elif answer_number == 5:
        return '5'


#r = random.randint(1,5)
#fortune = get_answer(r)
#print(fortune)
print(get_answer(random.randint(1,5)))
