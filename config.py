import json

def getGameConfig():
    with open('config.json') as f:
        data = json.load(f)
        return data['game']
    
def getInfoConfig():
    return getGameConfig()['info']
    
def getIngameConfig():
    return getGameConfig()['ingame']

def getWindowConfig():
    return getGameConfig()['window']

def getBlockSize():
    return getIngameConfig()['blockSize']

def getWindowSize():
    return [getWindowConfig()['width'], getWindowConfig()['height']]