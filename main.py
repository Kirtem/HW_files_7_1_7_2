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
    #                 print(dish_keys)
    # for x in range(0, len(lines)):
    #     if x

    print(type(lines))
    i = 0
    k = lines[0]
    i = i +1
    o = int(lines[i])
    i = i + 1
    l = []
    for x in range(i, i + o):
        # if "|" not in line:
        #     if line != "\n":
        #         try:
        #             x = int(line)
        #         except:
        #             dish_keys.append(line)
        #             print(dish_keys)
        l.append(dict(zip(cook_book_keys, lines[x].split("|"))))
    print(l)

# i + 2 И ВСЕ В WHILE

    # cook_book_dict = zip(k, l)
    # print(cook_book_dict)


    # while

# # cook_book_dict = zip(dish_keys, ingredient_dict)
# print(ingredient_dict)
# print(dict(cook_book_dict))



