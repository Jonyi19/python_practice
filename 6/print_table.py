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
    for i in range(len(list)):
        for t in range(len(list[i])):
            if col_widths[i] < len(list[i][t]):
                col_widths[i] = len(list[i][t])
    return col_widths

def print_table(list,width):
    string = ''
    for t in range(4):
        for i in range(len(list)):
            string += list[i][t].rjust(width[i],' ') + ' '
        string += "\n"

    print(string)

print_table(table_data,str_size(table_data))
