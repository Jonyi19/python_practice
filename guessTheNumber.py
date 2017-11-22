# 数あてゲーム

import random

select_number = random.randint(1,20)
print('1から20までの数を当てて下さい')

for guess_taken in range(1, 7):
    print(str(guess_taken) + '回目。数字を入力して下さい' )
    player_num = int(input())

    if player_num < select_number:
        print('残念！もっと上です！')
    elif player_num > select_number:
        print('残念!もっと下です!')
    else:
        break

if player_num == select_number:
    print('正解です!' + str(guess_taken) + '回で当たりました。')
else:
    print('残念。。正解は' + str(guess_taken) +'でした。次は頑張って!')