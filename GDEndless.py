import requests
import webbrowser
import time
import sys


blank = ""


print(" ████ ████        █████ █   █ ████  █     █████ █████ █████       █   █  ███  ████  █████ ")
print("█     █   █       █     ██  █ █   █ █     █     █     █           ██ ██ █   █ █   █ █     ")
print("█  ██ █   █       ████  █ █ █ █   █ █     ████  █████ █████       █ █ █ █   █ █   █ ████  ")
print("█   █ █   █       █     █  ██ █   █ █     █         █     █       █   █ █   █ █   █ █     ")
print(" ███  ████        █████ █   █ ████  █████ █████ █████ █████       █   █  ███  ████  █████ ")

print("")
print("")

print("█▀▀ ▄▀▄ █▄ ▄█ █▀▀    █▀▀ █▀▀ ▀█▀ █ █ █▀█ ")
print("█▄█ █▀█ █ ▀ █ ██▄    ▄██ ██▄  █  █▄█ █▀▀ ")

print("")

print("1. Type in ID")
print("2. Use GDUtils mod")

levelOpen = int(input("Choose level open type: "))

print("1. Easy")
print("2. Hard")
print("3. Expert")

typedDiff = int(input("Choose difficulty: "))

if typedDiff == 1:
    levelDiff = "3"

if typedDiff == 2:
    levelDiff = "4"
    
if typedDiff == 3:
    levelDiff = "5"


lives = 30
skips = 3




# header stuff
headers = {
    "User-Agent": ""
}

 # data for rob
data = {
    "total": 20,
    "noStar": 1,
    "type": 4,
    "secret": "Wmfd2893gb7",
    "len": 5,
    "diff":levelDiff,

}

url = "http://www.boomlings.com/database/getGJLevels21.php"

# actually sends the request
req = requests.post(url=url, data=data, headers=headers)

# saves the response
output = (req.text)

levelIDX = 0


# creates an array of levels
levelList = output.split('|')

while True:
    # gets the current level's data
    currentLevel = levelList[levelIDX].split(':')
    likeCount = int(currentLevel[19])
    levelID = str((currentLevel[1]))

    # checks if the likes are in the negatives, indicating it is bad and is skipped
    if likeCount < 0:
        # skips bad level
        levelIDX += 1
    else:
        # plays good level
        webbrowser.open("https://lostshadowgd.github.io/gd-endless-run/c/" + "?diff=" + str(typedDiff) + "&lives=" + str(lives) + "&levels=" + str(levelIDX))
        time.sleep(16)
        if levelOpen == 2:
            gdLink = "https://gdutils.com/" + levelID
            webbrowser.open(gdLink)
        else:
            print("The ID for level " + str(levelIDX) + " is " + currentLevel[1])
    
    time.sleep(4)
    complete = input("Type the 'Attempts' number on the end screen when level has been completed. Press enter to skip. You have " + str(skips) + " skips left. ")
    
    if complete == "" and skips >= 1:
        skips -= 1
    else:
        lives -= int(complete) - 1

    if lives <= 0:
        print("█▀█ █ █ ▀█▀   █▀█ █▀▀   █   ▀█▀ █ █ █▀▀ █▀▀")
        print("█▄█ █▄█  █    █▄█ █▀    █▄▄ ▄█▄ ▀▄▀ ██▄ ▄██")
        time.sleep(2.5)
        sys.exit()
    
    print("You have " + str(lives) + " lives and " + str(skips) + " skips left.")
    levelIDX += 1
    time.sleep(1)
    print("Loading next level.")
    time.sleep(1)
    print("Loading next level..")
    time.sleep(1)
    print("Loading next level...")
    time.sleep(1)
