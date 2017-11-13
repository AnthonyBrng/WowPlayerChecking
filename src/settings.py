
import configparser
import os.path
from .stdio import debugPrint
'''
Version number
'''
VERSION = '0.3.4'

'''
Configfile section and entry names.
'''
CONFIG_FILE = "./settings.cfg"
CONFIG_SECTION_API = "apikeys"
CONFIG_API_BLIZZ_EU = "blizzard_key_eu"
CONFIG_API_WARCRAFTLOGS = "warcraftlogs_key"

def createConfigFile():
    if os.path.isfile(CONFIG_FILE):
        return
    debugPrint("No settings.cfg found - creating it...")
    config = configparser.ConfigParser()
    config[CONFIG_SECTION_API] = {}
    config[CONFIG_SECTION_API][CONFIG_API_BLIZZ_EU] = ''
    config[CONFIG_SECTION_API][CONFIG_API_WARCRAFTLOGS] = ''
    with open(CONFIG_FILE, 'w') as configfile:
         config.write(configfile)
    debugPrint("...Done! (Creating cfg)")


createConfigFile()

config = configparser.ConfigParser()
config.read(CONFIG_FILE)

'''
The Warcraftlogs api key to use.
loaded from the configfile
'''
WARCRAFTLOGS_APIKEY = config[CONFIG_SECTION_API][CONFIG_API_WARCRAFTLOGS]

'''
The Blizzard api key to use.
loaded from the configfile
'''
BLIZZARD_APIKEY = config[CONFIG_SECTION_API][CONFIG_API_BLIZZ_EU]
