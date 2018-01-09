#! python3
# bulletPontAdder.py - クリップボードのテキストの各業に
# 点を打って、wikipediaの箇条書きにする

import pyperclip
text = pyperclip.paste()

lines = text.split('\n')
for i in range(len(lines)):     # "lines"リストの各要素をループする
    lines[i] = '* ' + lines[i]  # "lines"の要素に"* "を追加する

text = '\n'.join(lines)
pyperclip.copy(text)
print(text)