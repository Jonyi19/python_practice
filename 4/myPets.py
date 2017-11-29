my_pets = ['Zophie','Pooka','Fat-tail']
print('ペットの名前を入力してください')
name = input()
if name not in my_pets:
    print(name + 'というペットは含まれていないので追加しておきますね。')
    my_pets = my_pets + [name]
    print(my_pets)
else:
    print(name + 'は私のペットです')