#! python3
# pw.py - パスワード管理プログラム(脆弱性あり)

PASSWORDS = {'email': '45WnPAS)f)Q)MrNpfNH%','blog': 'p-+/aufKm5+chGyd%f~,',
            'luggage': 'ncUW2j7Grsnn,ujF|P&3'}

import sys
import pyperclip
if len(sys.argv) < 2:
    print('使い方: python3 py.pw [アカウント名]')
    print('パスワードをクリップボードにコピーします')
    sys.exit()

account = sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print(account + 'のパスワードをクリップボードにコピーしました。')
else:
    print(account + 'というアカント名はありません。')