## 6.7.1表の表示
##   apples Alice  dogs
##  oranges   Bob  cats
## cherries Carol moose
##   banana David goose
## のように表示させる

table_data = [['apples','orages','cherries','banana'],
              ['Alice','Bob','Carol','David'],
              ['dogs','cats','moose','goose']]

def str_size(list):
    col_widths = [0] * len(list)
    for col in range(len(list)):
        for row in list[col]:
            col_widths[col] = max(col_widths[col],len(row))
    return col_widths

def print_table(list,width):
    for row in range(len(list[0])):
        for col in range(len(list)):
            print(list[col][row].rjust(width[col]), end=' ')
        print()

print_table(table_data,str_size(table_data))
