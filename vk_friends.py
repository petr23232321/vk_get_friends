import vk_api
import json


vk_session = vk_api.VkApi(token='vk1.a.QJCbBdyVoCyJlUE6oapVV447ge4-cLcZ0k5smYXdVtbwtin5FQvNCpj96yt5-GzpoYMuqp8O68T4dWEL0AsqWns4tfsQ-uXqIGuCSWRZ0BVlU-_joCT-9XxsEQn3_nXHLE8pcHBNQ5avfSjZNG7mJZvRmwFnmMlBRf7ZtlKS8VQ1R_JFS_kDmyPa8NZZf3fAwwT6-aKYXJnz3ajDpUS-mA')
vk = vk_session.get_api()    

def get_user_friends(user_id):
    friends = vk_session.method("friends.get", {"user_id": user_id})
    users_info = []
    for friend in friends["items"]:
        user = vk_session.method("users.get", {"user_ids": friend, "fields": "country, city, bdate, sex, first_name, last_name"}) #using vk.user.get method and parametrs ->fields and user_ids
        
        
        
        user_info = {                                        #overriting data by order pdf
            "first_name": user[0]["first_name"],
            "last_name": user[0]["last_name"],
            "country": user[0].get("country", {}).get("title"),
            "city": user[0].get("city", {}).get("title"),
            "bdate": user[0].get("bdate"),
            "sex": "male" if user[0]["sex"] == 2 else "female" if user[0]["sex"] == 1 else "unknown"
        }
        users_info.append(user_info)
       
    return users_info
print("Starting...Pls wait ")
user_id = '219800221'
friends_info = get_user_friends(user_id)

# write friends_info to a JSON file
with open(f'{user_id}_friends_info.json', 'w') as f:
    json.dump(friends_info, f, ensure_ascii=False, indent=4, sort_keys=False)
print("Success! Friends info saved to file.")