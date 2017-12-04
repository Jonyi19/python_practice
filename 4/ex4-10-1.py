spam = ['apples','bananas','tofu','cats']

def andString(param):
    print('\'', end='')
    for i in range(len(param)):
        if len(param) -1 > i:
            print(str(param[i]) + ', ', end='')
        else:
            print('and ' + str(param[i]) + '\'')

andString(spam)

    