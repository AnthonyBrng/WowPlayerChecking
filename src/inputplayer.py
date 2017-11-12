class Player():
    '''
    DESCRIPTION:    Simple Player object containing the few important values for
                    a worldofwarcraft player.
    INPUT:          player_name - string
                    player_server - string
                    player_region - string (default = "EU")
    '''

    supportedRegions = ["EU", "US"]

    def __init__(self, player_name, player_server, player_region="EU"):
        self.name = player_name
        self.server = player_server
        self.region = ""
        self.setRegion(player_region)

    def setRegion(self, newRegion):
        '''
        DESCRIPTION:    Sets the region for a player. Only supportedregions allowed
        INPUT:          newRegion - string
        OUTPUT:         None
        EXCEPTIONS:     ValueError
        '''
        if newRegion in self.supportedRegions:
            self.region = newRegion
        else:
            raise ValueError("Unsupported Region '{}'. Please select one of the following below\n{}".format(newRegion, supportedRegions))

    def printSupportedRegions(self):
        '''
        DESCRIPTION:    prints the Supported Regions
        INPUT:          None
        OUTPUT:         None
        '''
        result = "Supported regions: ("
        for region in self.supportedRegions:
            result += region + " "
        result += ")"
        print(result)
