from class_UserList import UserList


My_App = UserList()
menu_item = 0
# My_App.change_user()
while True:
    print('Here we can:\n', '- 1 Get users list\n', '- 2 Add new user\n',
          '- 3 Change user\n', '- 4 Delete user\n', '- 5 Search user\n',
          '- 6 Put users list to Excel')
    menu_item = int(input('Chose an action from 1 to 6... '))
    if menu_item in range(1, 6):
        print('Ok,', menu_item, 'selected')
    if menu_item == 1:
        print('---------- User List ----------')
        My_App.get_users()
    elif menu_item == 2:
        print('---------- Add a new user ----------')
        My_App.add_user()
    elif menu_item == 3:
        print('---------- Change user ----------')
        My_App.change_user()
    elif menu_item == 4:
        print('---------- Delete user ----------')
        My_App.del_user()
    elif menu_item == 5:
        print('---------- Search user ----------')
        My_App.search_user()
    elif menu_item == 6:
        print('---------- Write to xlsx ----------')
        My_App.write_to_xlsx()