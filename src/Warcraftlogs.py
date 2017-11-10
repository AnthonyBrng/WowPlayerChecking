# pip install requests
import requests
class Warcraftlogs():

    baseUrl = "https://www.warcraftlogs.com:443/v1/"
    wlUrl = "https://www.warcraftlogs.com/"

    '''
    [
        {
        "difficulty": integer
        "bosses" : [
                        {
                            "bossName": string
                            "bracket" : integer
                            "DPS":  integera
                            "report_id": string
                            "fight_id" : integer
                        }
                    ]
        }
    ]
    '''
    output = []

    def __init__(self, player_name, player_server, player_region, api_key):
        self.pname = player_name
        self.pserver = player_server
        self.pregion = player_region
        self.api_key = api_key
        self.classes = self.get_json(self.baseUrl + "classes?api_key={}".format(api_key))
        self.zones = self.get_json(self.baseUrl + "zones?api_key={}".format(api_key))
        self.ranking = self.get_json(self.baseUrl + "rankings/character/{}/{}/{}?api_key={}".format(self.pname, self.pserver, self.pregion, self.api_key))

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
            print("Error on pulling from Warcraftlogs!")
            exit()
        else:
            print("...Done! (Downloading)")
            return req.json()



    def get_classname(self, class_id):
        '''
        Get the class-name-lable from an class_id

        INPUT:  class_id - integer
        OUTPUT: string
        '''
        return classes[class_id-1]["name"]


    def get_bossname(self, boss_id):
        '''
        Returns the Boss-Name of a boss-id.
        INPUT: boss_id - integera
        OUTPUT: string
        '''
        for zone in zones:
            for encounter in zone["encounters"]:
                if encounter["id"] == boss_id:
                    return encounter["name"]


    def get_Stats(self, difficulty, role):
        '''
        Gets all stats we want, for a specific difficulty id.
        nhc = 3, hc = 4, mythic = 5
        '''
        result = []
        '''
        Model Schema for encounter
            [
                {
                    "encounter": 2032,
                    "class": 6,
                    "spec": 3,
                    "guild": "Donut Care",
                    "rank": 5120,
                    "outOf": 13475,
                    "duration": 295770,
                    "startTime": 1507231241675,
                    "reportID": "8gwAKG9JLCtMNv4R",
                    "fightID": 28,
                    "difficulty": 5,
                    "size": 20,
                    "itemLevel": 940,
                    "total": 1243790,
                    "estimated": true
                }
            ]
        '''
        for encounter in self.ranking:
            boss_dict = {}  # return value
            if encounter["difficulty"] == difficulty:
                report_id = encounter["reportID"]
                boss_id = encounter["encounter"]
                bracket = round((1-encounter["rank"]/encounter["outOf"])*100)
                '''
                Model Schema for fights
                    {
                          "id": 1,
                          "start_time": 268763,
                          "end_time": 516888,
                          "boss": 2032,
                          "size": 20,
                          "difficulty": 5,
                          "kill": true,
                          "partial": 3,
                          "bossPercentage": 0,
                          "fightPercentage": 0,
                          "lastPhaseForPercentageDisplay": 0,
                          "name": "Goroth"
                    }
                '''
                fights = self.get_json(self.baseUrl + "report/fights/{}?api_key={}".format(report_id, self.api_key))
                for fight in fights["fights"]:
                    if fight["boss"] == boss_id and fight["kill"] and fight["difficulty"] == difficulty:
                        '''
                        - Table view reports
                        Model Schema for playerInfo
                        {
                            "name": "Kesanna",
                            "id": 26,
                            "guid": 101104115,
                            "type": "Monk",
                            "itemLevel": 938,
                            "icon": "Monk-Brewmaster",
                            "total": 2835344293,
                            "activeTime": 3819687,
                            "activeTimeReduced": 3819687,
                            "blocked": 25327745,
                            "abilities": [],
                            "gear": []
                        }
                        '''
                        entries =  self.get_json(self.baseUrl + "report/tables/{}/{}?start={}&end={}&api_key={}".format( role,report_id, fight["start_time"], fight["end_time"], self.api_key ))
                        for playerInfo in entries["entries"]:
                            if playerInfo["name"] == self.pname:
                                duration = (fight["end_time"] - fight["start_time"]) / 1000
                                dps = round(playerInfo["total"] / duration, 2)
                                boss_dict["bossName"] = fight["name"]
                                boss_dict["bracket"] = bracket
                                boss_dict["dps"] = dps
                                boss_dict["report"] = report_id
                                boss_dict["fight_id"] = fight["id"]
                result.append(boss_dict)
        self.output.append({"difficulty" : difficulty, "bosses": result})
        pass




    def getHtml(self):
        result = "<div class='pve_panel'>"
        for entry in self.output: # entr = dict
            result += "<h3>{}</h3>".format(self.getDifficultyName(entry["difficulty"]))
            result += "<table class=raid_table>"
            result += "<tr><th>Boss</th><th>Todays Bracket</th><th>Max. Output</th><th>Link</th></tr>"
            bracket_counter = 0
            dps_counter = 0

            for boss in entry["bosses"]:
                result += self.html_tableRow(boss["bossName"], boss["bracket"], round(boss["dps"]), boss["report"], boss["fight_id"])
                bracket_counter += boss["bracket"]
                dps_counter += boss["dps"]

            result += self.html_tableFoot("Durchschnitt", round(bracket_counter/len(entry["bosses"])), round(dps_counter/len(entry["bosses"])) )
            result += "</table>"

        result += "</div>"
        return result


    def html_tableRow(self, bossname, bracket, dps,report_id, fight_id):
        return "<tr><td class='bossname'>{}</td><td class='bracket'>{}</td><td class='dps'>{}</td><td class=wl_link><b><a class='raid_link' href='{}'>*</a></b></td></tr>".format(bossname, bracket, dps, self.wlUrl+"/reports/"+report_id+"#fight="+str(fight_id))

    def html_tableFoot(self, bossname, bracket, dps):
        return "<tr class='tablefoot'><td class='bossname'><b>{}</b></td><td class='bracket'><b>{}</b></td><td class='dps'><b>{}</b></td><td> </td></tr>".format(bossname, bracket, dps)

    def getDifficultyName(self, id):
        return ["Unknown difficulty","Unknown difficulty","Unknown difficulty","Normal","Heroic","Mythic"][id]
