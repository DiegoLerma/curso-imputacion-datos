def online_counter(dict):
    online_users_counter=0
    for status in dict.values():
        if status=='online':
            online_users_counter+=1
    return online_users_counter

print(online_counter({'user1': 'online', 'user2': 'offline', 'user3': 'offline', 'user4': 'online'}))