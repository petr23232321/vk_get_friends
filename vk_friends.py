import vk_api
import json
from datetime import datetime

vk_session = vk_api.VkApi(token='TOKEN_VK')
vk = vk_session.get_api()

def get_user_friends(user_id):
    friends = vk_session.method("friends.get", {"user_id": user_id})
    users_info = []
    for friend in friends["items"]:
        user = vk_session.method("users.get", {"user_ids": friend, "fields": "country, city, bdate, sex, first_name, last_name"})
        
        print( user)
        
        user_info = {
            "first_name": user[0]["first_name"],
            "last_name": user[0]["last_name"],
            "country": user[0].get("country", {}).get("title"),
            "city": user[0].get("city", {}).get("title"),
            "bdate": user[0].get("bdate"),
            "sex": "male" if user[0]["sex"] == 2 else "female" if user[0]["sex"] == 1 else "unknown"
        }
        users_info.append(user_info)
    return users_info

user_id = 'USER_ID'
friends_info = get_user_friends(user_id)

# write friends_info to a JSON file
with open(f'{user_id}_friends_info.json', 'w') as f:
    json.dump(friends_info, f, ensure_ascii=False, indent=4, sort_keys=False)