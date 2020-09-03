import requests
import confidential_data
from allauth.socialaccount.models import SocialAccount

access_token = confidential_data.key()


def get_user_id(friends_data):
    return SocialAccount.objects.get(user=friends_data).extra_data['id']


def friends(request_data):
    user_id = get_user_id(request_data)
    response = requests.get(
        'https://api.vk.com/method/friends.get',
        params={
            'access_token': access_token,
            'v': 5.122,
            'user_id': user_id,
            'lang': 0,
            'order': 'random',
            'fields': 'nickname',
            'count': 5,
        }
    )
    return response.json()
