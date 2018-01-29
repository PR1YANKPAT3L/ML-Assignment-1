import requests

class Request:
    def __init__(self):
        ''' Constructor for this class. '''
        # Configuration for the API calls
        self.baseURI = 'https://api.opendota.com/api/'
        self.HEADERS = {}

    def getHeroes(self):
        uri = self.baseURI + 'heroes'
        response = requests.get(uri, headers=self.HEADERS)
        while response.status_code != 200:
            response = requests.get(self.baseURI)
        
        if response.status_code == 200:
            return response.json()
        else:
            print "Response Status: " + response.status_code
            return None
 
 
    def getHeroBenchmarks(self, hero_id):
        uri = self.baseURI + 'benchmarks?hero_id=' + str(hero_id)
        response = requests.get(uri, headers=self.HEADERS)
        while response.status_code != 200:
            response = requests.get(self.baseURI)
        
        if response.status_code == 200:
            return response.json()
        else:
            print "Response Status: " + response.status_code
            return None

    def getHeroMatchups(self, hero_id):
        uri = self.baseURI + 'heroes/' + str(hero_id) + '/matchups'
        response = requests.get(uri, headers=self.HEADERS)
        while response.status_code != 200:
            response = requests.get(self.baseURI)
        
        if response.status_code == 200:
            return response.json()
        else:
            print "Response Status: " + response.status_code
            return None