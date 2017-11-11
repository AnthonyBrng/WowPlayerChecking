# WoW player checking 
Checks the performance from a World-of-Warcraft-Player, using the Warcraftlogs-API and the Blizzard-Api.
Sections:
- [Installation requirements](#installation-requirments)
- [Getting API-Keys](#getting-api-keys)
  - [Blizzard API Key](#blizzard-api-key)
  - [Warcraftlogs API Key](#warcraftlogs-api-key)
- [Things to TODO](#things-to-todo)
	
# Installation requirements
Make sure you have performed the following things before running this apllication:
* install Python3.6 or higher	(https://www.python.org/downloads/windows/)
* install the `requests` module for python (`pip3 install requests`)
* you've got a Blizzard-API key			(instructions where to get them below)
* you've got a Warcraftlogs-API key			"

# Running the app
1. Make sure you entered your two API-Keys into the settings.py
2. Open the terminal/commandline
3. change your directory to WowPlayerChecking
4. `python3 check.py --help`

# Getting API Keys
### Blizzard API Key
1. Sign up on https://dev.battle.net/
2. Log into your account
3. Click on the top-right corner on MyAccount
4. Goto Tab key
5. Create API key
6. You have now received your own Blizzard API Key :)

### Warcraftlogs API Key
1. Sign up on https://www.warcraftlogs.com/
2. Log in your account
3. Click on the top right of your profile-image
4. Click settings (gear-icon)
5. Scroll down to the very bottom and create the API Key
6. You have now received your own Warcraftlogs API Key :)

# Things to TODO
- INTENSE testing
- Catching input errors
- Improve Stylemanagement
  - rename tag identifyer and calsses
  - external .css file
- create HTML API
- create CSV API
- GUI
- installer for
  - Windows
  - Mac
- performance optimization
- update Running App section
