from pprint import pprint
from copy import deepcopy


# # Functii lambda
#
# # my_lambda = lambda x,y: x + y
# # my_sum = my_lambda(2, 3)
# # print(my_sum)
#
# # a = lambda: 1
# # b = lambda: 2
# # print(a())
# # print(f'id(a) {id(a)}')
# # print(f'id(a) {id(b)}')
# # print(f'unassigned lambda: {id(lambda: 2)}')
# # print(f'id(a) {id(a)}')
# # print(f'unassigned lambda: {id(lambda: 3)}')
# # print(f'id(a) {id(a)}')
# # print(f'unassigned lambda: {id(lambda: 3*3)}')
#
# players = [
#     {
#         'first_name': 'John',
#         'last_name': 'Doe',
#         'rank': 3
#     },
#     {
#         'first_name': 'Kevin',
#         'last_name': 'McDonald',
#         'rank': 2
#     },
#     {
#         'first_name': 'Brad',
#         'last_name': 'Kelvin',
#         'rank': 1
#     }
# ]
#
#
# pprint(players)
# print('.....Sorted List......')
#
#
# # def custom_sort_function(player):
# #     return player['rank']
# # pprint(sorted(players, key=custom_sort_function)) sau:
# pprint(sorted(players, key=lambda player: player['rank']))

# Functia map

# players = [
#     {
#         'first_name': 'John',
#         'last_name': 'Doe',
#         'rank': 3
#     },
#     {
#         'first_name': 'Kevin',
#         'last_name': 'McDonald',
#         'rank': 2
#     },
#     {
#         'first_name': 'Brad',
#         'last_name': 'Kelvin',
#         'rank': 1
#     }
# ]
#
# # d2 = dict(d1) => deepcopy()
#
#
# def check_top_3_player(player):
#     updated_player = deepcopy(player)
#     updated_player['is_top_3'] = True if updated_player['rank'] <= 3 else False
#     return updated_player
#
#
# player_with_top_3 = map(check_top_3_player, players)
# print(list(player_with_top_3))


# Functia filter
#
#
# players = [
#     {
#         'first_name': 'John',
#         'last_name': 'Doe',
#         'rank': 3
#     },
#     {
#         'first_name': 'Kevin',
#         'last_name': 'McDonald',
#         'rank': 2
#     },
#     {
#         'first_name': 'Brad',
#         'last_name': 'Kelvin',
#         'rank': 1
#     }
# ]
#
#
# def filter_all_mcdonalds(player):
#     if player['last_name'] == 'McDonald':
#         return True
#
#     return False
#
# # all_mcdonalds = filter(filter_all_mcdonalds, players) sau:
#
# all_mcdonalds = filter(lambda player: True if player['last_name'] == 'McDonald' else False, players)
# print(list(all_mcdonalds))


# Functia zip

names = ['John', 'Michael', 'Bob']
cities = ['Bucharest', 'Cluj', 'Timisoara']
jobs = ['developer', 'qa', 'business analyst']

for zip_item in zip(names, cities, jobs):
    print(zip_item)
    name, city, job = zip_item # zip_item e un tuplu
    print(f'{name} is a {job} and lives in {city}')