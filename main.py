# with open("Cookbook.txt", "r", encoding="utf-8") as f:
#     cook_book_dict = {}
#     cook_book_keys = ["ingredient_name", "quantity", "measure"]
#     ingredient_dict = {}
#     dish_keys = []
#     lines = f.readlines()
#
#
#     i = 0
#     k = lines[0]
#     i = i + 1
#     o = int(lines[i])
#     i = i + 1
#     l = []
#     for x in range(i, i + o):
#         l.append(dict(zip(cook_book_keys, lines[x].split("|"))))
#     print(l)

# i + 2 И ВСЕ В WHILE

    # cook_book_dict = zip(k, l)
    # print(cook_book_dict)



# # cook_book_dict = zip(dish_keys, ingredient_dict)
# print(ingredient_dict)
# print(dict(cook_book_dict))

with open("Cookbook.txt", "r", encoding="utf-8") as file:
    cook_book_dict = {}
    cook_book_keys = ["ingredient_name", "quantity", "measure"]
    for line in file:
        dish_name = line.strip()
        counter = int(file.readline())
        dish_ingr_list = []
        for _ in range(counter):
            # print("начинается вложенная итерация", _+1)
            ingr = file.readline().strip().split("|")
            # print("pechataem ingridienti", ingr)
            ing_dict = dict(zip(cook_book_keys, ingr))
            # print("pechataem slovar", ing_dict)
            dish_ingr_list.append(ing_dict)
        # print("вот что получилось в списке ингридиентов для блюда " + dish_name, dish_ingr_list)
        file.readline()
        cook_book_dict[dish_name] = dish_ingr_list
        print(cook_book_dict)

    print(cook_book_dict)


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    dishes = input("Введите название блюда: ")
    person_count = input("Введите кол-во человек: ")
        if dishes in dish_name:
            print(cook_book_dict.get(dishes))

# def get_shop_list_by_dishes(dishes, person_count):
#     finish_dict = {}
#     for dish in dishes:
#         if dish in cook_book:
#             for dict_ingred in cook_book[dish]:
#                 if dict_ingred['ingredient_name'] not in finish_dict:
#                     finish_dict[dict_ingred['ingredient_name']] = dict(measure=dict_ingred['measure'], quantity=int(
#                         dict_ingred['quantity']) * person_count)
#                 else:
#                     finish_dict[dict_ingred['ingredient_name']] = dict(measure=dict_ingred['measure'], quantity=int(
#                         dict_ingred['quantity']) * person_count + finish_dict[dict_ingred['ingredient_name']].pop(
#                         'quantity'))
#
#         else:
#             return f'Неверно введено название блюда'
#     return finish_dict
# print(get_shop_list_by_dishes(['Омлет', 'Запеченный картофель'], 2))
#