import requests
import pprint
# from config_data.config import settings


def movie_search(film_name):
    url = "https://api.kinopoisk.dev/v1.4/movie/search?page=1&limit=1&query="

    headers = {
        "accept": "application/json",
        # "X-API-KEY": settings.kinopoisk_dev_token
        "X-API-KEY": "2EGH4DD-GX247VQ-Q2XJFHB-X543Z6F"
    }

    try:
        response = requests.get(f"{url + film_name}", headers=headers)
        data = response.json()["docs"][0]
        return data

    except IndexError:
        return "Ничего не найдено, пожалуйста попробуйте еще раз!"
    except KeyError:
        return "Сервер временно не доступен, попробуйте позже!"
    
pprint.pprint(movie_search("avatar"))
pprint.pprint(movie_search("see"))
