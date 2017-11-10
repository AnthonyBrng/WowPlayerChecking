
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
        self.mplusInfo = self.buildMplusInfo()

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
        '''
        {
            "pvptype" :
                {
                    "rating": string
                    "seasonPlayed": integer
                    "seasonWon": integer
                }
        }
        '''
        print("Calculating pvp stats...")
        result = {}
        pvpinfo_json = self.charInfo["pvp"]["brackets"]
        result["2v2"] = {
            "rating": pvpinfo_json["ARENA_BRACKET_2v2"]["rating"],
            "seasonWon": pvpinfo_json["ARENA_BRACKET_2v2"]["seasonWon"],
            "seasonPlayed": pvpinfo_json["ARENA_BRACKET_2v2"]["seasonPlayed"]
        }
        result["3v3"] = {
            "rating": pvpinfo_json["ARENA_BRACKET_3v3"]["rating"],
            "seasonWon": pvpinfo_json["ARENA_BRACKET_3v3"]["seasonWon"],
            "seasonPlayed": pvpinfo_json["ARENA_BRACKET_3v3"]["seasonPlayed"]

        }
        result["rbg"] = {
            "rating": pvpinfo_json["ARENA_BRACKET_RBG"]["rating"],
            "seasonWon": pvpinfo_json["ARENA_BRACKET_RBG"]["seasonWon"],
            "seasonPlayed": pvpinfo_json["ARENA_BRACKET_RBG"]["seasonPlayed"]

        }
        print("...Done! (pvp stats)")
        return result


    def buildMplusInfo(self):
        print("Calculating Mythic+ stats...")
        url = self.baseUrl+"/character/{}/{}?fields=achievements&locale=en_GB&apikey={}".format(self.pserver, self.pname, self.api_key)
        mplus_json = self.get_json(url)

        mplus_crits = {
            "2": 33096,
            "5": 33097,
            "10": 33098,
            "15": 32028
        }

        # mythic plus quantities
        quants = {
            "2": 0,
            "5": 0,
            "10": 0,
            "15": 0
        }

        lst_criteria = mplus_json["achievements"]["criteria"]       # from Api
        lst_quants = mplus_json["achievements"]["criteriaQuantity"] # from Api
        for critname, criteria in mplus_crits.items():
            quants[critname] = lst_quants[lst_criteria.index(criteria)]

        print("...Done!")
        return quants

    def getMplusHtml(self):
        result = "<div class='mplus_panel'>"
        result += "<h3>{}</h3>".format("Mythic+ in time")
        result += "<table class='mplus_table'>"
        result += "<tr> <th>Level</th> <th>Finished</th><tr>"
        for level, quant in self.mplusInfo.items():
            result += "<tr><td>Mythic {}</td><td id='number_td'>{}</td></tr>".format(level, quant)
        result += "</table>"
        result += "</div>"
        return result


    def getPvpHtml(self):
        result = "<div class='pvp_panel'>"
        result += "<h3>{}</h3>".format("Rated-PvP")
        result += "<table class='pvp_table'>"
        result += "<tr> <th>Type</th> <th>Rating</th> <th>Won</th> <th>played</th> <th>Win-Ratio %</th> <tr>"
        for pvptype in self.pvpInfo:
            result += self.getTableRow(pvptype, self.pvpInfo[pvptype])
        result += "</table>"
        result += "</div>"
        return result

    def getTableRow(self, pvptype, stats):
        result = "<tr><td>{}</td>".format(pvptype)
        for stat in stats:
            result += "<td class='{0}' id='number_td'>{0}</td>".format(stats[stat]) #result += "<td>{}</td><td>{}</td><td>{}</td><td>{}%</td>".format(rating, seasonWon, seasonPlayed, (seasonWon/seasonPlayed) * 100)
        result +="<td id='number_td'>{:05.2f}%</td>".format(stats["seasonWon"] / stats["seasonPlayed"]*100)
        result += "</tr>"
        return result

    def getCharinfoHtml(self):
        return "<div class='player_panel'><p class='player_paragraph'><b><a class='char_link' style='color:{};' href='{}'>{}*</a></b> on {} ({})</p><p><i>{} {}</i></p></div>".format(self.getClasscolorByClassname(self.charInfo["class"]),"https://worldofwarcraft.com/de-de/character/"+self.pserver+"/"+ self.pname, self.pname, self.pserver, self.pregion, self.charInfo["class"], self.charInfo["race"])


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
