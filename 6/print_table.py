## 6.7.1表の表示
##   apples Alice  dogs
##  oranges   Bob  cats
## cherries Carol moose
##   banana David goose
## のように表示させる

table_data = [['apples','orages','cherries','banana'],
              ['Alice','Bob','Carol','David'],
              ['dogs','cats','moose','goose']]


def print_table(list):
    for i in range(len(list)):
        for l in range(len(list[i])):
            col_widths = 





print_table(table_data)

'''    for i in range(len(list)):
        max = 0
        for l in range(len(i)):
            str_len[l] = len(l)
            if str_len[l - 1] < str_len[l]:
                max = str_len[l]
                '''