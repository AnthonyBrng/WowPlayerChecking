
import requests

class BlizzStats():

    def __init__(self, player_name, player_server, player_region, api_key):
        self.pname = player_name
        self.pserver = player_server
        self.pregion = player_region
        self.baseUrl = self.getBaseUrlFromRegion()
        self.api_key = api_key
        self.classes = self.getClassMapping()
        self.races = self.getRaceMapping()
        self.charInfo = self.buildCharinfo()
        self.pvpInfo = self.buildPvpinfo()

    def getBaseUrlFromRegion(self):
        result = "https://eu.api.battle.net/wow/"
        return result


    def getCharacterProfile(self):
        '''
        {
            "lastModified": 1510262465000,
            "name": "Tink",
            "realm": "Blackhand",
            "battlegroup": "Vengeance / Rache",
            "class": 4,
            "race": 10,
            "gender": 1,
            "level": 110,
            "achievementPoints": 12240,
            "thumbnail": "blackhand/161/101104033-avatar.jpg",
            "calcClass": "c",
            "faction": 1,
            "totalHonorableKills": 12535
        }
        '''
        return  self.get_json(self.baseUrl+"character/{}/{}?fields=pvp&locale=en_GB&apikey={}".format(self.pserver, self.pname, self.api_key))



    def getClassMapping(self):
        '''
        {
            "classes": [{
                "id": 1,
                "mask": 1,
                "powerType": "rage",
                "name": "Warrior"
            }, {
                "id": 2,
                "mask": 2,
                "powerType": "mana",
                "name": "Paladin"
            }
            ...
            ]
        }
        '''
        class_json = self.get_json(self.baseUrl+ "data/character/classes?locale=en_GB&apikey={}".format(self.api_key))
        classes = ["Unknown-Class"]
        for pclass in class_json["classes"]:
            classes.append(pclass["name"])
        return classes


    def getClassById(self, classid):
        return self.classes[classid]

    def getRaceMapping(self):
        '''
        {
            "races": [{
                "id": 1,
                "mask": 1,
                "side": "alliance",
                "name": "Human"
            }, {
                "id": 2,
                "mask": 2,
                "side": "horde",
                "name": "Orc"
            }
            ...
            ]
        }
        '''
        race_json = self.get_json(self.baseUrl+ "data/character/races?locale=en_GB&apikey={}".format(self.api_key))
        races = ["Unknown Race"]
        for race in race_json["races"]:
            races.append(race["name"])
        return races

    def getRaceById(self, raceid):
        return self.races[raceid]


    def get_json(self, url):
        '''
        Gets a JSON-list, downloaded from an URL

        INPUT:  url - string
        OUTPUT: list
        '''
        print("Downloading JSON from {}...".format(url))
        try:
            req = requests.get(url=url)
        except:
            print("Error on pulling from {} !".format(url))
            exit()
        else:
            print("...Done! (Downloading)")
            return req.json()

    def buildCharinfo(self):
        print("Building player stats...")
        charprofile_json = self.getCharacterProfile()
        charprofile_json["race"] = self.getRaceById(charprofile_json["race"])
        charprofile_json["class"] = self.getClassById(charprofile_json["class"])
        print("...Done! (Playerstats)")
        return charprofile_json


    def buildPvpinfo(self):
        print("Calculating pvp stats...")
        result = {}
        pvpinfo_json = self.charInfo["pvp"]["brackets"]
        result["2v2"] = {
            "rating": pvpinfo_json["ARENA_BRACKET_2v2"]["rating"],
            "seasonPlayed": pvpinfo_json["ARENA_BRACKET_2v2"]["seasonPlayed"],
            "seasonWon": pvpinfo_json["ARENA_BRACKET_2v2"]["seasonWon"]
        }
        result["3v3"] = {
            "rating": pvpinfo_json["ARENA_BRACKET_3v3"]["rating"],
            "seasonPlayed": pvpinfo_json["ARENA_BRACKET_3v3"]["seasonPlayed"],
            "seasonWon": pvpinfo_json["ARENA_BRACKET_3v3"]["seasonWon"]
        }
        result["rbg"] = {
            "rating": pvpinfo_json["ARENA_BRACKET_RBG"]["rating"],
            "seasonPlayed": pvpinfo_json["ARENA_BRACKET_RBG"]["seasonPlayed"],
            "seasonWon": pvpinfo_json["ARENA_BRACKET_RBG"]["seasonWon"]
        }
        print("...Done! (pvp stats)")
        return result

    def getPvpHtml(self):
        pass


    def getCharinfoHtml(self):
        return "<div class='player_panel'><p class='player_paragraph'><b><a class='char_link' style='color:{};' href='{}'>{}</a></b> on {} ({})</p><p><i>{} {}</i></p></div>".format(self.getClasscolorByClassname(self.charInfo["class"]),"https://worldofwarcraft.com/de-de/character/"+self.pserver+"/"+ self.pname, self.pname, self.pserver, self.pregion, self.charInfo["class"], self.charInfo["race"])


    def getClasscolorByClassname(self, classname):
        return {
            "Death Knigh": "#C41F3B",
            "Demon Hunter":"#A330C9",
            "Druid":"#FF7D0A",
            "Hunter":"#ABD473",
            "Mage":"#69CCF0",
            "Monk":"#00FF96",
            "Paladin":"#F58CBA",
            "Priest":"#FFFFFF",
            "Rogue":"#FFF569",
            "Shaman":"#0070DE",
            "Warlock":"#9482C9",
            "Warrior":"#C79C6E"
        }[classname]
