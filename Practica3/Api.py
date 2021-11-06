#!/usr/bin/env python
#-*- coding: utf-8 -*-
import requests

def api_poke(url='http://pokeapi.co/api/v2/pokemon-form/', offset=0):
    args = {'offset' : offset} if offset else {}

    response = requests.get(url, params=args)

    if response.status_code == 200:

        payload = response.json()
        results = payload.get('results', [])

        if results:
            for pokemon in results:
                name = pokemon ['name']
                print(name)

        next = input("¿quieres mas pokemons? [S/N]").lower()
        if next == 's':
            api_poke(offset=offset+20)
            
if __name__ == '__main__':
    url='http://pokeapi.co/api/v2/pokemon-form/'
    api_poke()
