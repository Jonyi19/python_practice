birthdays = {'アリス': '4/1','ボブ': '12/12','キャロル':'4/4'}

while True:
    print('名前を入力して下さい: (終了するにはEnterだけ押して下さい)')
    name = input()
    if name == '':
        break

    if name in birthdays:
        print(name + 'の誕生日は' + birthdays[name])
    else:
        print(name + 'の誕生日は登録されていません。')
        print(name + 'の誕生日を入力して下さい')
        birthdays[name] = input()
        print(name + 'の誕生日をデータベースに更新しました。')