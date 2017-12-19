from inventory import display_inventory

def add_to_inventory(inventory,add_items):
    for add in add_items:
        inventory.setdefault(add,0)
        inventory[add] +=  1
    return inventory
        
    
inv = {'金貨':42,'ロープ':1}
dragon_loot = ['金貨','手裏剣','金貨','金貨','ルビー']
inv = add_to_inventory(inv,dragon_loot)
display_inventory(inv)        
