with open("Cookbook.txt", "r", encoding="utf-8") as f:
    cook_book_dict = {}
    cook_book_keys = ["ingredient_name", "quantity", "measure"]
    ingredient_dict = {}
    dish_keys = []
    lines = f.readlines()




    # for line in lines:
    #     if "|" not in line:
    #         if line != "\n":
    #             try:
    #                 x = int(line)
    #             except:
    #                 dish_keys.append(line)
    #     else:
    #         ingredient_dict = dict(zip(cook_book_keys, line.split("|")))
    # for a in ingredient_dict.values():
    #     print(a)

    # cook_book_dict = zip(dish_keys, ingredient_dict)
    # print(ingredient_dict)


# # cook_book_dict = zip(dish_keys, ingredient_dict)
# print(ingredient_dict)
# print(dict(cook_book_dict))



