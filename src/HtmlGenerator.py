import pathlib
import datetime

class HtmlGen():
    '''
    AUTHOR:         Anthony Bruening
    DESCRIPTION:    Generating a HTML file from a giving list of html-objects
    INPUT:          divLst - list of strings
                    playername - string
                    playerserver - string
                    playerregion - string
                    role - string
    '''

    def __init__(self, divLst, playername, playerserver, playerregion, role):
        self.divLst = divLst
        self.pname = playername
        self.pserver = playerserver
        self.pregion = playerregion
        self.role = role

    def start(self):
        '''
        DESCRIPTION:    Create final html-file.
        INPUT:          None
        OUTPUT:         None
        '''
        print("Creating HTML-files...")
        content = self.buildFileContent()
        outputdir = "players"
        pathlib.Path(outputdir).mkdir(parents=True, exist_ok=True)
        outputpath = "{}/{}_{}_{}_{}.html".format(outputdir, self.pname, self.pserver, self.pregion, self.role.split("-")[0])
        outputfile = open(outputpath, "w")
        outputfile.write(content)
        outputfile.close()
        print("...Done! (HTML-files)")


    def buildFileContent(self):
        '''
        DESCRIPTION:    Build file-content from HtmlGen() inputs.
        INPUT:          None
        OUTPUT:         string
        '''
        # now = datetime.datetime.now()

        result = "<html>"
        result += self.html_header()
        result += "<body style='margin:14px; padding:14px'>"
        result += "<div>"
        for htmlString in self.divLst :
            result += htmlString
        result += "</div>"
        result += "</body"
        result += "</html>"
        return result

    def html_header(self):
        '''
        DESCRIPTION:    Returning a html-string containing the header and style information.
        INPUT:          None
        OUTPUT:         string
        TODO:           den inhalt dieser hässlichen methode vernünftig auslagern.
        '''
        return "<head><style>div{}#number_td{text-align:right}.mplus_panel{ float:right; width: 50%; min-width:400px}.mplus_table{width:400px; margin-left:auto; margin-right:auto; font-family:Arial;border: 5px solid #98bc56;border-radius: 10px; padding: 5px;}.pvp_panel{float:right; width: 50%; min-width:400px}.pve_panel{float:left;width: 50%; min-width:400px}.pvp_table{width:400px; margin-left:auto; margin-right:auto; font-family:Arial;border: 5px solid #98bc56;border-radius: 10px; padding: 5px;}.player_panel{font-family: Arial;border-radius: 20px ;padding: 10px ;background-color: #323a2a;color: white}.char_link{text-decoration:none;}.player_paragraph{font-size: 25px;}.playerInfo{font-family: Arial; font-size:20px;}.raid_link{color: green;text-decoration: none;}.wl_link{text-align: center;}.tablefoot{background-color:#d5d6d4;}p{font-family:Arial;font-size:15px}h3{text-align:center; font-family:Arial;}.raid_table{margin-left:auto; margin-right:auto;font-family:Arial;border: 5px solid #98bc56;border-radius: 10px; padding: 5px;}th{padding:8px;background-color: #d2d6cb ;}td{padding:5px;background-color: #ddeac5 ;}.bossname{text-align: left;}.bracket{text-align: center;}.dps{text-align: right;}</style></head>"
