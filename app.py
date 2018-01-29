import random, os, json, datetime, time
import sys
import pandas as pd

from pymongo import MongoClient
from bson import json_util
from utils.Request import Request
from utils.Colors import Colors

def get_heroes(db):
    if db.heroes.count() != 115:
        for hero in heroes:
            heroes_coll.insert_one(hero).inserted_id

def get_selected_hero():
    selected_hero = heroes_coll.find_one({ "localized_name": hero_name })
    if selected_hero == None:
        print Colors.FAIL + "No Hero Found" + Colors.ENDC
    else:
        return selected_hero

def get_hero_benchmark():
    selected_hero_benchmark = benchmarks_coll.find_one({ "hero_id": selected_hero_id })
    if selected_hero_benchmark == None:
        print Colors.FAIL + "No Hero Benchmark found. Fetching Benchmarks and adding to DB." + Colors.ENDC
        benchmark_data = scrapper.getHeroBenchmarks(selected_hero_id)
        hdbId = benchmarks_coll.insert_one(benchmark_data).inserted_id
        print Colors.OKBLUE + "Inserted Benchmark for " + hero_name + " with id: " + str(hdbId) + Colors.ENDC

        selected_hero_benchmark = benchmarks_coll.find_one({ "hero_id": selected_hero_id })
        print Colors.OKGREEN + "\nDisplaying Hero Benchmark Data: " + Colors.ENDC;
        print pd.DataFrame(selected_hero_benchmark['result'])
    else:
        print Colors.OKGREEN + "\nDisplaying Hero Benchmark Data: " + Colors.ENDC;
        print pd.DataFrame(selected_hero_benchmark['result'])

def get_hero_matchups():
    selected_hero_matchups = matchups_coll.find_one({ "hero_id": selected_hero_id })
    if selected_hero_matchups == None:
        print Colors.FAIL + "No Hero Matchups found. Fetching Matchups and adding to DB." + Colors.ENDC
        matchups_data = scrapper.getHeroMatchups(selected_hero_id)
        hdmId = matchups_coll.insert_one({ 'hero_id': selected_hero_id, 'matchups': matchups_data }).inserted_id
        print Colors.OKBLUE + "Inserted Benchmark for " + hero_name + " with id: " + str(hdmId) + Colors.ENDC

        selected_hero_matchups = matchups_coll.find_one({ "hero_id": selected_hero_id })
        print Colors.OKGREEN + "\nDisplaying Hero Matchup Data: " + Colors.ENDC;
        print pd.DataFrame(selected_hero_matchups['matchups'])
    else:
        print Colors.OKGREEN + "\nDisplaying Hero Matchup Data: " + Colors.ENDC;
        print pd.DataFrame(selected_hero_matchups['matchups'])

if len(sys.argv) < 2:
    print Colors.FAIL + "Please enter a hero name. Eg. 'Faceless Void'" + Colors.ENDC
else:
    hero_name = sys.argv[1]

    client = MongoClient('localhost', 27017)
    print Colors.OKGREEN + "Connected to MongoDB." + Colors.ENDC
    db = client.assignment_1

    heroes_coll = db.heroes
    benchmarks_coll = db.hero_benchmarks
    matchups_coll = db.hero_matchups

    # time.sleep(5) # hack for the mongoDb database to get running

    scrapper = Request()
    heroes = scrapper.getHeroes()

    get_heroes(db)
    
    selected_hero = get_selected_hero()
    if selected_hero != None:
        print Colors.OKGREEN + "\nDisplaying Hero Data for " + hero_name + ": " + Colors.ENDC;
        print pd.DataFrame(selected_hero)
        selected_hero_id = selected_hero['id']

        get_hero_benchmark()
        get_hero_matchups()
