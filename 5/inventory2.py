def display_inventory(inventory):
    print("持ち物リスト:")
    item_total = 0
    for k , v in inventory.items():
        print( str(v) + " " + str(k))
        item_total = v + item_total

    print("アイテム総数: " + str(item_total))

def add_to_inventory(inventory,add_items):
    for add in add_items:
        inventory.setdefault(add,0)
        inventory[add] = inventory[add] + 1
    return inventory
        
    
inv = {'金貨':42,'ロープ':1}
dragon_loot = ['金貨','手裏剣','金貨','金貨','ルビー']
inv = add_to_inventory(inv,dragon_loot)
display_inventory(inv)        
