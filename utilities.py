import requests
import confidential_data
from allauth.socialaccount.models import SocialAccount

access_token = confidential_data.key()

# Получение id пользователя
def get_user_id(data):
    return SocialAccount.objects.get(user=data).extra_data['id']

# Получение списка друзей
def friends(data):
    user_id = get_user_id(data)
    response = requests.get(
        'https://api.vk.com/method/friends.get',
        params={
            'access_token': access_token,
            'v': 5.122,
            'user_id': user_id,
            'lang': 0,
            'order': 'random',
            'fields': 'domain, photo_100',
            'count': 5,
        }
    )
    return response.json()['response']['items']
