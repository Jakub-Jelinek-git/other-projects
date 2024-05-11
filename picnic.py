
def show_picnic_items(picnic_list: dict,left_width: int,right_width: int):
    """prints out nicely formated items from the given picnic distionary"""
    print("Picnic Items".upper().center(left_width+right_width,"="))
    for item, num_item in picnic_list.items():
        print(item.title().ljust(left_width,".") + 
              str(num_item).title().rjust(right_width," "))

picnic = {"Chocolate": 3,"Wine":6,"Beer":12,"Basket":1,"apples": 6}
show_picnic_items(picnic,13,3)
show_picnic_items(picnic,18,6)