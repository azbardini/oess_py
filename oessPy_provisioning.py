from oessPy_actions import *
import json
from pprint import pprint


# -------------------------------------
# ------------PROVISIONING-------------
# --------------@bardini---------------

#Tree functions to return json string without unicode characters
def json_load_byteified(file_handle):
    return _byteify(
        json.load(file_handle, object_hook=_byteify),
        ignore_dicts=True
    )
def json_loads_byteified(json_text):
    return _byteify(
        json.loads(json_text, object_hook=_byteify),
        ignore_dicts=True
    )
def _byteify(data, ignore_dicts = False):
    # if this is a unicode string, return its string representation
    if isinstance(data, unicode):
        return data.encode('utf-8')
    # if this is a list of values, return list of byteified values
    if isinstance(data, list):
        return [ _byteify(item, ignore_dicts=True) for item in data ]
    # if this is a dictionary, return dictionary of byteified keys and values
    # but only if we haven't already byteified it
    if isinstance(data, dict) and not ignore_dicts:
        return {
            _byteify(key, ignore_dicts=True): _byteify(value, ignore_dicts=True)
            for key, value in data.iteritems()
        }
    # if it's anything else, return it in its original form
    return data


#TODO Tests
#Returns one only information of a simple json string
def getJsonParsedString(jsonString, param, id):
    jsonData = json_loads_byteified(jsonString)
    parsed = jsonData["results"][id][str(param)]
    return parsed

#TODO Tests
#Prints all instances of json parameter
def printAllJsonParsedString(jsonString, param):
    jsonData = json_loads_byteified(jsonString)
    counter = 0
    while (counter < str(jsonData["results"]).count('{')):
        pprint(jsonData["results"][counter][str(param)])
        counter += 1

#TODO Tests
#Returns one only information on a json string
def getJsonParsedStringNew(jsonString, paramOne, idOne, paramTwo=None, idTwo=None, paramThree=None, idThree=None):
    jsonData = json_loads_byteified(jsonString)
    flag = 0;
    if (paramThree):
        parsed = jsonData["results"][idOne][str(paramOne)][idTwo][str(paramTwo)][idThree][str(paramThree)]
    if (paramTwo):
        parsed = jsonData["results"][idOne][str(paramOne)][idTwo][str(paramTwo)]
    if flag:
        return parsed
    else:
        return jsonData["results"][idOne][str(paramOne)]


#Returns the path between 2 nodes with all links separated by %
def getShortestPathString(nodeOne, nodeTwo, link=None):
    jsonString = getShortestPath(nodeOne, nodeTwo)
    jsonData = json_loads_byteified(jsonString)
    result = ''
    for counter in range(0, jsonString.count('link')):
        result = result + '%'
        for instance in jsonData["results"][counter]['link']:
            result = result + instance
    return result[1:]


#Provision a circuit and returns json String
def makeCircuit(nodeOne, interfaceOne, nodeTwo, interfaceTwo, vLan):
    shortestPath = getShortestPathString(nodeOne, nodeTwo)
    jsonReturn = provisionCircuit(
        1, -1, -1, 'circuitBetween'+nodeOne+'and'+nodeTwo, nodeOne+'%'+nodeTwo,
        interfaceOne+'%'+interfaceTwo, str(vLan)+'%'+str(vLan), link=shortestPath, backupLink=shortestPath
    )
    return jsonReturn


nodeOne = 'unnamed-16'
interfaceOne = 'swt1-eth1'
nodeTwo = 'unnamed-64'
interfaceTwo = 'swt4-eth1'
vLan = 3
jsonString = makeCircuit(nodeOne, interfaceOne, nodeTwo, interfaceTwo, vLan)
printJson(jsonString)