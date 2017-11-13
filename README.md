# WoW player checking
Checks the performance from a World-of-Warcraft-Player, using the Warcraftlogs-API and the Blizzard-Api.
Sections:
- [Installation requirements](#installation-requirments)
- [Getting API-Keys](#getting-api-keys)
  - [Blizzard API Key](#blizzard-api-key)
  - [Warcraftlogs API Key](#warcraftlogs-api-key)
- [Things to TODO](#things-to-todo)

# Installation requirements
**If you want to use the standalone Windows-version:**
* No requirements needed :)
* Just download it
* (its just a bit slower performance-wise)

**If you want to use the python versions:**
* install Python3.6 or higher	(https://www.python.org/downloads/)
* make sure to check the checkbox "add python to PATH", in the installation wizard
* install the `requests` module for python (`pip3 install requests`)

# Running the app
1. Make sure you've got a [Blizzard API Key](#blizzard-api-key)
2. Make sure you've got a [Warcraftlogs API Key](#warcraftlogs-api-key)
3. Make sure you entered your two API-Keys into the settings.cfg (just use an editor to open it)

**For commandline usage:**
4. Open the terminal/commandline
5. change your directory to WowPlayerChecking
6. `python3 check.py --help` or `check.exe --help`

**For GUI-usage:**
4. Open the folder WowPlayerChecking
5. Doubleclick on `check_gui.py` or `check.exe`
6. wait for the GUI to popup, (.exe version is slow)

7. after running the app check the players folder for the output files

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
- improve GUI
  - check inputs
  - calling check.py from the gui
  - improve code quality for check_gui.py
- installer for
  - Windows
  - Mac
- performance optimization
- update Running App section
- Dps Brackets are shown ONLY from specific spec. (currently all specs are shown)
