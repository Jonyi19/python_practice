list = [['aaa','bbbb','yyy'],
        ['ccccc','ddd','xxxx'],
        ['ee','ffff','zzz']]

def print_list(list):
    for i in range(len(list)):
        for row in list[i]:
            print(row)

print_list(list)