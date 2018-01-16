table_data = [['apples','orages','cherries','banana'],
              ['Alice','Bob','Carol','David'],
              ['dogs','cats','moose','goose']]

def print_test(list):
    for i in range(len(list)):
        print(list[i])
        for row in list[i]:
            print(row)

print_test(table_data)
