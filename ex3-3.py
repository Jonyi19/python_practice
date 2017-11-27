# コラッツ数列
def collatz(number):
    if number % 2 == 0 :
        number = number / 2
        print(number)
        return number
    elif number % 2 == 1 :
        number = number * 3 + 1
        print(number)
        return number
    
print('整数を入力してください')
number = int(input())
while True :
    number = collatz(number)
    if number == 1 :
        break

print('処理が終了しました')