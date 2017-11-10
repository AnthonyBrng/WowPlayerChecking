#--------------------------------------------
# Imports
from src.Warcraftlogs import Warcraftlogs
from src.HtmlGenerator import HtmlGen
from src.CollectorThreads import CollectWlogsStats
from src.BlizzardArsenal import BlizzStats

player_name = 'Horscanigun'
player_server = 'Blackhand'
player_region = 'EU'


#--------------------------------------------
# Warcraftlogs
wlogs_apikey = '6bd918e14d71db254e0603d4bab015fe'
wlogs = Warcraftlogs(player_name, player_server, player_region, wlogs_apikey)

collect_nhc = CollectWlogsStats(wlogs, 3, "damage-done")
collect_hc = CollectWlogsStats(wlogs, 4, "damage-done")
collect_my = CollectWlogsStats(wlogs, 5, "damage-done")

collect_nhc.start()
collect_hc.start()
collect_my.start()

blizz_apikey = "kkaexyh7uw5rwngn8ab9y9ydrpz93vz5"
blizz = BlizzStats(player_name, player_server, player_region, blizz_apikey)


collect_nhc.join()
collect_hc.join()
collect_my.join()
print("...Done! (Warcraftlogs)")
#--------------------------------------------
# output

blizz_apikey = "kkaexyh7uw5rwngn8ab9y9ydrpz93vz5"
blizz = BlizzStats(player_name, player_server, player_region, blizz_apikey)

outputs = [blizz.getCharinfoHtml(), wlogs.getHtml(), blizz.getPvpHtml(), blizz.getMplusHtml()]
gen = HtmlGen( outputs, player_name, player_server, player_region)
gen.start()
