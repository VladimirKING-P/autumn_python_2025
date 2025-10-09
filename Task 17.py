all_users = {'id3', 'id5', 'id9', 'id8', 'id2', 'id1', 'id4', 'id6', 'id7', 'id10'}
offline_users = {'id3', 'id9', 'id7', 'id2', 'id4', 'id6'}

online_users = all_users - offline_users
print("В сети", online_users)
print("Колличество пользователей", len(online_users))