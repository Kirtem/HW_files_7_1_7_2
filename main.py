with open("Cookbook.txt", "r", encoding="utf-8") as file:
    cook_book_dict = {}
    cook_book_keys = ["ingredient_name", "quantity", "measure"]
    for line in file:
        dish_name = line.strip()
        counter = int(file.readline())
        dish_ingr_list = []
        for _ in range(counter):
            ingr = file.readline().strip().split("|")
            ing_dict = dict(zip(cook_book_keys, ingr))
            dish_ingr_list.append(ing_dict)
        file.readline()
        cook_book_dict[dish_name] = dish_ingr_list
    print(cook_book_dict)

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ing in cook_book_dict[dish]:
            ing_name = ing["ingredient_name"]
            shop_list[ing_name] = { "quantity": int(ing["quantity"]) * person_count, "measure": ing["measure"]}
    return shop_list

print(get_shop_list_by_dishes(["Омлет", "Фахитос"], 2))

