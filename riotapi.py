import requests

URL = {
'base':'https://{proxy}.api.pvp.net/{url}',
'summoner_by_name':'/api/lol/{region}/{version}/summoner/by-name/{summonerNames}',
'champion_by_id':'/api/lol/static-data/{region}/{version}/champion/{id}',
'retrieve_champion_list':'/api/lol/static-data/{region}/{version}/champion'
}

API_VERSIONS = {'summoner':'v1.4','static':'v1.2'}

HOTKEYS = {'q':0, 'w':1, 'e':2, 'r':3}

REGIONS = {'north_america':'na','global':'global'}

API_KEY = ''   #enter a key

class RiotAPI():

    def __init__(self, api_key, region = REGIONS['north_america']):
        self.api_key = api_key
        self.region = region

    def request(self, api_url, params={}):
        args = {'api_key':self.api_key}
        for key, value in params.items():
            if key not in args:
                args[key] = value
        response = requests.get(URL['base'].format(proxy=self.region, url=api_url),params=args)
        # print response.url
        return response.json()

    def get_summoner_by_name(self, name):
        api_url = URL['summoner_by_name'].format(region=self.region, version=API_VERSIONS['summoner'],summonerNames=name)
        return self.request(api_url)

    def get_champion_list(self):
        api_url = URL['retrieve_champion_list'].format(region=self.region, version=API_VERSIONS['static'])
        return self.request(api_url)

    def get_champion_data(self, my_id):
        api_url = URL['champion_by_id'].format(region=self.region, version=API_VERSIONS['static'], id=my_id)
        return self.request(api_url,{'champData':'all'})

class Champion():
    def __init__(self,api,champion):
        self.data = api.get_champion_data(champion_list['data'][champion]['id'])
        #self.info

    def get_spells(self):
        return self.data['spells']

    def get_spell(self, hotkey):
        return self.data['spells'][HOTKEYS[hotkey]]

    def print_spells(self):
        for key, values in HOTKEYS.items():
            self.print_spell(key)
            print '\n'

    def print_spell(self, hotkey, params = ['name','description','range','cooldown']):
        for value in params:
            print value + ':', self.get_spell(hotkey)[value]

    def print_me(self, me = {}):
        if me == {}:
            me = self.data
        if type(me) == dict:
            for key, value in me.items():
                print key+":"
                if type(value) == list or type(value) == dict:
                    self.print_me(value,tabs)
                else:
                    print '\t', value

        elif type(me) == list:
            for value in me:
                if type(value) == dict:
                    self.print_me(value, tabs)
                else:
                    print '\t', value

#print tryndamere.data.keys()

api=RiotAPI(API_KEY)
champion_list = api.get_champion_list()

tryndamere = Champion(api,'Tryndamere')
tryndamere.print_spells()
#tryndamere.print_me()
