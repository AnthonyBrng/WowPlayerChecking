import sys
import requests

DEBUG = False

def debugPrint(msg):
    '''
    DESCRIPTION:    Print if debug flag is set.
    INPUT:          msg - string
    OUTPUT:         None
    '''
    if DEBUG:
        print(msg)


def get_json(url):
    '''
    DESCRIPTION:    Gets a JSON-list, downloaded from an URL
    INPUT:          url - string
    OUTPUT:         json
    '''
    debugPrint("Downloading JSON from {}...".format(url))
    try:
        req = requests.get(url=url)
    except:
        sys.stderr.write("Error: Cant pull JSON from {} !\n".format(url))
        sys.stderr.write
        exit()
    else:
        debugPrint("...Done! (Downloading)")
        return req.json()
