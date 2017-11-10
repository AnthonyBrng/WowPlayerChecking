
class HtmlGen():

    def __init__(self, divLst, playername, playerserver, playerregion):
        self.divLst = divLst
        self.pname = playername
        self.pserver = playerserver
        self.pregion = playerregion

    def start(self):
        print("Creating HTML-files...")
        outputfile = open("players/{}_{}_{}.html".format(self.pname, self.pserver, self.pregion), "w")
        result = "<html>"
        result += self.html_header()
        result += "<body>"
        #result += self.html_Playerinfo()
        for htmlString in self.divLst :
            result += htmlString

        result += "</body"
        result += "</html>"
        outputfile.write(result)
        outputfile.close()
        print("...Done! (HTML-files)")

    # def html_Playerinfo(self):
    #     return "<p class='playerInfo' ><b><a style='text-decoration:none' href='{}'>{}</a></b> on {} ({})</p>".format("https://worldofwarcraft.com/de-de/character/"+self.pserver+"/"+ self.pname, self.pname, self.pserver, self.pregion)

    def html_header(self):
        return "<head><style>div{}#number_td{text-align:right}.mplus_panel{ float:right; width: 50%; min-width:400px}.mplus_table{width:400px; margin-left:auto; margin-right:auto; font-family:Arial;border: 5px solid #98bc56;border-radius: 10px; padding: 5px;}.pvp_panel{float:right; width: 50%; min-width:400px}.pve_panel{float:left;width: 50%; min-width:400px}.pvp_table{width:400px; margin-left:auto; margin-right:auto; font-family:Arial;border: 5px solid #98bc56;border-radius: 10px; padding: 5px;}.player_panel{font-family: Arial;border-radius: 20px ;padding: 20px ;background-color: #323a2a;color: white}.char_link{text-decoration:none;}.player_paragraph{font-size: 25px;}.playerInfo{font-family: Arial; font-size:20px;}.raid_link{color: green;text-decoration: none;}.wl_link{text-align: center;}.tablefoot{background-color:#d5d6d4;}p{font-family:Arial;font-size:15px}h3{text-align:center; font-family:Arial;}.raid_table{margin-left:auto; margin-right:auto;font-family:Arial;border: 5px solid #98bc56;border-radius: 10px; padding: 5px;}th{padding:8px;background-color: #d2d6cb ;}td{padding:5px;background-color: #ddeac5 ;}.bossname{text-align: left;}.bracket{text-align: center;}.dps{text-align: right;}</style></head>"
