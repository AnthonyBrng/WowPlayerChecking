class Player():
    '''
    DESCRIPTION:    Simple Player object containing the few important values for
                    a worldofwarcraft player.
    INPUT:          player_name - string
                    player_server - string
                    player_region - string (default = "EU")
    '''

    supportedRegions = ["EU", "US"]
    supportedRoles = ["damage-done", "healing"]

    def __init__(self, player_name, player_server, player_region="EU", player_role="damage-done"):
        self.name = player_name
        self.server = player_server
        self.region = ""
        self.role = ""
        self.setRegion(player_region)
        self.setRole(player_role)

    def setRole(self, newRole):
        '''
        DESCRIPTION:    Sets the role for a player. Only supported roles allowed
        INPUT:          newRegion - string
        OUTPUT:         None
        EXCEPTIONS:     ValueError
        '''
        if newRole in self.supportedRoles:
            self.role = newRole
        else:
            raise ValueError("Unsupported Role '{}'. Please select one of the following below\n{}".format(newRole, self.supportedRoles))

    def printSupportedRegions(self):
        '''
        DESCRIPTION:    prints the Supported Regions
        INPUT:          None
        OUTPUT:         None
        '''
        result = "Supported regions: ("
        for region in self.supportedRoles:
            result += region + " "
        result += ")\n"
        sys.stdout.write(result)
        sys.stdout.flush()

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
            raise ValueError("Unsupported Region '{}'. Please select one of the following below\n{}".format(newRegion, self.supportedRegions))

    def printSupportedRegions(self):
        '''
        DESCRIPTION:    prints the Supported Regions
        INPUT:          None
        OUTPUT:         None
        '''
        result = "Supported regions: ("
        for region in self.supportedRegions:
            result += region + " "
        result += ")\n"
        sys.stdout.write(result)
        sys.stdout.flush()
