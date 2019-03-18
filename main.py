import os
from random import randint
import requests
from dotenv import load_dotenv


GROUP_ID = 179723123


def load_image(url):
    response = requests.get(url)
    file_name = os.path.split(url)[-1]
    with open(file_name, "wb") as f:
        f.write(response.content)
    return file_name


def get_comics_num():
    api_url = "https://xkcd.com/info.0.json"
    response = requests.get(api_url)
    return response.json()['num']


def get_comics_info(id):
    api_url = f"https://xkcd.com/{id}/info.0.json"
    response = requests.get(api_url)
    return response.json()


def get_upload_server_url(token):
    api_url = "https://api.vk.com/method/photos.getWallUploadServer"
    params = {
        "group_id": GROUP_ID,
        "access_token": token,
        "v": 5.92
    }
    response = requests.post(api_url, data=params)
    return response.json()['response']['upload_url']


def upload_image(url, image_name):
    with open(image_name, "rb") as file_descriptor:
        files = {
            "photo": file_descriptor,
            "group_id": GROUP_ID
        }
        response = requests.post(url, files=files)
    return response.json()


def save_image_to_album(token, photo_object):
    api_url = "https://api.vk.com/method/photos.saveWallPhoto"
    params = {
        "access_token": token,
        "v": 5.92,
        "group_id": GROUP_ID,
        "photo": photo_object['photo'],
        "server": photo_object['server'],
        "hash": photo_object["hash"]
    }
    response = requests.post(api_url, data=params)
    return response.json()['response']


def post_image_to_wall(token, media_id, owner_id, message):
    api_url = "https://api.vk.com/method/wall.post"
    params = {
        "access_token": token,
        "v": 5.92,
        "owner_id": -179723123,
        "from_group": 1,
        "message": message,
        "attachments": [
            f"photo{owner_id}_{media_id}"
        ]
    }
    response = requests.post(api_url, data=params)
    return response.json()['response']


if __name__ == '__main__':
    load_dotenv()
    access_token = os.getenv("access_token")

    comics_num = get_comics_num()
    random_comics_id = randint(0, comics_num)
    comics_info = get_comics_info(random_comics_id)
    comics_comment = comics_info['alt']
    image_url = comics_info['img']
    loaded_image = load_image(image_url)
    upload_url = get_upload_server_url(access_token)
    photo_object = upload_image(upload_url, loaded_image)
    saved_image = save_image_to_album(access_token, photo_object)
    uploaded_media_idx = 0
    media_id = saved_image[uploaded_media_idx]['id']
    owner_id = saved_image[uploaded_media_idx]['owner_id']
    result = post_image_to_wall(access_token, media_id, owner_id, comics_comment)
    if result.get('post_id'):
        print('Запись успешно добавлена!')
    os.remove(loaded_image)

