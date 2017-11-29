# 例外処理

def spam(divide_by):
    try:
        return 42 / divide_by
    except ZeroDivisionError:
        print('エラー：不正な引数です')

r = int(input())
print(spam(r))