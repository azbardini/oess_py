from oessPy_actions import *
import json
from pprint import pprint

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
    return data#=======================================


# -------------------------------------
# ---------------TESTS-----------------
# -------------@bardini----------------


#jsonReturn = getWorkgroups()
#printJson(jsonReturn)

#jsonReturn = getAllWorkgroups()
#printJson(jsonReturn)

#jsonReturn = isWithinCircuitLimit(1)
#printJson(jsonReturn)

#jsonReturn = getWorkgroupMembers(1)
#printJson(jsonReturn)

#jsonReturn = getMaps(1)
#printJson(jsonReturn)

#jsonReturn = getShortestPath('unnamed-16','unnamed-32')
#printJson(jsonReturn)


# -------------------------------------
# --------------TODO-TESTS
# ---------------@bardini--------------


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


jsonReturn = getMaps(1)
jsonData = json_loads_byteified(jsonReturn)
printJson(jsonReturn)
counter=0
result=''
for instance in jsonData["results"][0]['links']['swt1'][counter]['link_name']:
    result = result + instance
print(result)


#print (getJsonParsedStringNew(jsonReturn,'links', 1 ))
#printAllJsonParsedString(workgroupMembers,'links')

#counter=0
#result=''
#for instance in jsonData["results"][0]['links']['swt1'][counter]['link_name']:
#    result = result + instance
#print(result)