import pytest
import requests 
 
def test_status_code():
    url = "https://api.pokemonbattle.me:9104/trainers"

    response = requests.get(url)
    assert response.status_code == 200


def test_piece_body():
    response = requests.get("https://api.pokemonbattle.me:9104/trainers", params= {'trainer_id': '2607'})
    assert response.json()['trainer_name'] =='Мой лучший тренер'