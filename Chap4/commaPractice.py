user_list = []

def comma_code(user_list):
    for item in range(len(user_list) - 2):
        print(user_list[item], end=', ')
    print(user_list[-2] + ' and ' + user_list[-1])

while True:
    print('Enter a list item (Or enter nothing to stop.):')
    user_item = input()
    if user_item == '':
        print('Here is your list: ')
        comma_code(user_list)
        break
    user_list = user_list + [user_item]
