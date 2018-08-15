import requests, json
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
oessServer = 'localhost'
oessUser = 'oess-test'
oessPasswd = 'changeme'


# -------------------------------------
# ---------NETWORK INFORMATION---------
# -------------@bardini----------------


def getWorkgroups():
    action = '?action=get_workgroups'
    parameters = ''
    return sendInformationRequest(action, parameters)


def getMaps(workgroupId, linkType=None):
    action = '?action=get_maps'
    parameters = "&workgroup_id=" + str(workgroupId)
    if linkType:
        parameters += "&link_type=" + linkType
    return sendInformationRequest(action, parameters)


def getNodes(type=None):
    action = '?action=get_nodes'
    parameters = ''
    if type:
        parameters += "&type=" + str(type)
    return sendInformationRequest(action, parameters)


def getNodeInterfaces(node, workgroupId=None, showDown=None, showTrunk=None, type=None):
    action = '?action=get_node_interfaces'
    parameters = '&node=' + str(node)
    if workgroupId:
        parameters += "&workgroup_id=" + str(workgroupId)
    if showDown:
        parameters += "&show_down=" + str(showDown)
    if showTrunk:
        parameters += "&show_trunk=" + str(showTrunk)
    if type:
        parameters += "&type=" + str(type)
    return sendInformationRequest(action, parameters)


def getInterface(interfaceId):
    action = '?action=get_interface'
    parameters = '&interface_id=' + str(interfaceId)
    return sendInformationRequest(action, parameters)


def getWorkgroupInterfaces(workgroupId):
    action = '?action=get_workgroup_interfaces'
    parameters = "&workgroup_id=" + str(workgroupId)
    return sendInformationRequest(action, parameters)


def getOldShortestPath(node, type, link=None):
    action = '?action=get_shortest_path'
    parameters = '&node=' + str(node) + '&type=' + str(type)
    if link:
        parameters += "&link=" + str(link)
    return sendInformationRequest(action, parameters)


def getShortestPath(nodeOne, nodeTwo, link=None):
    action = '?action=get_shortest_path'
    parameters = '&node=' + str(nodeOne) + '&node=' + str(nodeTwo)
    if link:
        parameters += "&link=" + str(link)
    return sendInformationRequest(action, parameters)


def getExistingCircuits(workgroupId, pathNodeId=None, endpointNodeId=None):
    action = '?action=get_existing_circuits'
    parameters = '&workgroup_id' + str(workgroupId)
    if pathNodeId:
        parameters += "&path_node_id=" + str(pathNodeId)
    if endpointNodeId:
        parameters += "&endpoint_node_id=" + str(endpointNodeId)
    return sendInformationRequest(action, parameters)


def getCircuitsByInterfaceId(interfaceId):
    action = '?action=get_circuits_by_interface_id'
    parameters = '&interface_id=' + str(interfaceId)
    return sendInformationRequest(action, parameters)


def getCircuitDetails(circuitId):
    action = '?action=get_circuit_details'
    parameters = '&circuit_id=' + str(circuitId)
    return sendInformationRequest(action, parameters)


def getCircuitDetailsByExternalIdentifier(externalIdentifier):
    action = '?action=get_circuit_details_by_external_identifier'
    parameters = '&external_identifier=' + str(externalIdentifier)
    return sendInformationRequest(action, parameters)


def getCircuitScheduledEvents(circuitId):
    action = '?action=get_circuit_scheduled_events'
    parameters = '&circuit_id=' + str(circuitId)
    return sendInformationRequest(action, parameters)


def getCircuitHistory(circuitId):
    action = '?action=get_circuit_history'
    parameters = '&circuit_id=' + str(circuitId)
    return sendInformationRequest(action, parameters)


def isVlanTagAvailable(node, interface, vlan, workgroupId=None):
    action = '?action=is_vlan_tag_available'
    parameters = '&node=' + str(node) + \
                 '&interface=' + str(interface) + \
                 '&vlan=' + str(vlan)
    if workgroupId:
        parameters += "&workgroup_id=" + workgroupId
    return sendInformationRequest(action, parameters)


def getWorkgroupMembers(workgroupId):
    action = '?action=get_workgroup_members'
    parameters = "&workgroup_id=" + str(workgroupId)
    return sendInformationRequest(action, parameters)


def generateClr(circuitId, raw=None):
    action = '?action=generate_clr'
    parameters = "&circuit_id=" + str(circuitId)
    if raw:
        parameters += "&raw=" + str(raw)
    return sendInformationRequest(action, parameters)


def getAllNodeStatus(type=None):
    action = '?action=get_all_node_status'
    parameters = ''
    if type:
        parameters += "&type=" + str(type)
    return sendInformationRequest(action, parameters)


def getAllLinkStatus(type=None):
    action = '?action=get_all_link_status'
    parameters = ''
    if type:
        parameters += "&type=" + str(type)
    return sendInformationRequest(action, parameters)


def getAllResourcesForWorkgroups(workgroupId):
    action = '?action=get_all_resources_for_workgroups'
    parameters = '&workgroup_id=' + str(workgroupId)
    return sendInformationRequest(action, parameters)


def sendEmail(subject, body):
    action = '?action=send_email'
    parameters = '&subject=' + str(subject) + \
                 '&body=' + str(body)
    return sendInformationRequest(action, parameters)


def getLinkByName(name):
    action = '?action=get_link_by_name'
    parameters = '&name=' + str(name)
    return sendInformationRequest(action, parameters)


def isWithinMacLimit(workgroupId, node, interface, macAddress):
    action = '?action=is_within_mac_limit'
    parameters = '&workgroup_id=' + str(workgroupId) + \
                 '&node=' + str(node) + \
                 '&interface=' + str(interface) + \
                 '&mac_address=' + str(macAddress)
    return sendInformationRequest(action, parameters)


def isWithinCircuitEndpointLimit(workgroupId, endpointNum):
    action = '?action=is_within_circuit_endpoint_limit'
    parameters = '&workgroup_id=' + str(workgroupId) + '&endpoint_num=' + str(endpointNum)
    return sendInformationRequest(action, parameters)


def isWithinCircuitLimit(workgroupId):
    action = '?action=is_within_circuit_limit'
    parameters = '&workgroup_id=' + str(workgroupId)
    return sendInformationRequest(action, parameters)


def getVlanTagRange(workgroupId, node, interface):
    action = '?action=get_vlan_tag_range'
    parameters = '&workgroup_id=' + str(workgroupId) + '&node=' + str(node) + '&interface=' + str(interface)
    return sendInformationRequest(action, parameters)


# -------------------------------------
# ------------PROVISIONING-------------
# -------------@bardini----------------


def provisionCircuit(workgroupId, provisionTime, removeTime, description, node, interface, tag, \
                     externalIdentifier=None, bandwidth=None, restoreToPrimary=None, staticMac=None, link=None, \
                     backupLink=None, endpointMacAddressNum=None, macAddress=None, loopNode=None, state=None, \
                     remoteNode=None, remoteTag=None, remoteUrl=None, remoteRequester=None, circuitId=None):
    action = '?action=provision_circuit'
    parameters = \
        "&workgroup_id=" + str(workgroupId) + \
        "&provision_time=" + str(provisionTime) + \
        "&remove_time=" + str(removeTime) + \
        "&description=" + str(description)
    nodeList = node.split('%')
    for instance in nodeList:
        parameters += "&node=" + str(instance)
    interfaceList = interface.split('%')
    for instance in interfaceList:
        parameters += "&interface=" + str(instance)
    tagList = tag.split('%')
    for instance in tagList:
        parameters += "&tag=" + str(instance)
    if externalIdentifier:
        parameters += "&external_identifier=" + str(externalIdentifier)
    if bandwidth:
        parameters += "&bandwidth=" + str(bandwidth)
    if restoreToPrimary:
        parameters += "&restore_to_primary=" + str(restoreToPrimary)
    if staticMac:
        parameters += "&static_mac=" + str(staticMac)
    if link:
        pathList = link.split('%')
        for instance in pathList:
            parameters += "&link=" + str(instance)
    if backupLink:
        pathList = backupLink.split('%')
        for instance in pathList:
            parameters += "&backup_link=" + str(instance)
    if endpointMacAddressNum:
        parameters += "&endpoint_mac_address_num=" + str(endpointMacAddressNum)
    if macAddress:
        parameters += "&mac_address=" + str(macAddress)
    if loopNode:
        parameters += "&loop_node=" + str(loopNode)
    if state:
        parameters += "&state=" + str(state)
    if remoteNode:
        parameters += "&remote_node=" + str(remoteNode)
    if remoteTag:
        parameters += "&remote_tag=" + str(remoteTag)
    if remoteUrl:
        parameters += "&remote_url=" + str(remoteUrl)
    if remoteRequester:
        parameters += "&remote_requester=" + str(remoteRequester)
    if circuitId:
        parameters += "&circuid_id=" + str(circuitId)
    return sendProvisioningRequest(action, parameters)


def failOverCircuit(circuitId, workgroupId, force=None):
    action = '?action=fail_over_circuit'
    parameters = "&circuit_id=" + str(circuitId) + \
                 "&workgroup_id=" + str(workgroupId)
    if force:
        parameters += "&force=" + str(force)
    return sendProvisioningRequest(action, parameters)


def reprovisionCircuit(circuitId, workgroupId, type=None):
    action = '?action=reprovision_circuit'
    parameters = "&circuit_id=" + str(circuitId) + "&workgroup_id=" + str(workgroupId)
    if type:
        parameters += "&type=" + str(type)
    return sendProvisioningRequest(action, parameters)


def removeCircuit(circuitId, workgroupId, removeTime, type=None, force=None):
    action = '?action=remove_circuit'
    parameters = \
        "&circuit_id=" + str(circuitId) + \
        "&workgroup_id=" + str(workgroupId) + \
        "&remove_time " + str(removeTime)
    if type:
        parameters += "&type=" + str(type)
    if force:
        parameters += "&force=" + str(force)
    return sendProvisioningRequest(action, parameters)

# -------------------------------------
# ------------MEASUREMENT--------------
# -------------@bardini----------------

def getCircuitData(circuitId, start, end, node=None,
                   interface=None, link=None):
    action = '?action=get_circuit_data'
    parameters = \
        "&circuit_id=" + str(circuitId) + \
        "&start=" + str(start) + \
        "&end " + str(end)
    if node:
        parameters += "&node=" + str(node)
    if interface:
        parameters += "&interface=" + str(interface)
    if link:
        parameters += "&link=" + str(link)
    return sendMeasurementRequest(action, parameters)

# -------------------------------------
# ------------MONITORING---------------
# -------------@bardini----------------

def getNodeStatus(node):
    action = '?action=get_node_status'
    parameters = '&node=' + str(node)
    return sendMonitoringRequest(action, parameters)

def getMplsNodeStatus(node):
    action = '?action=get_mpls_node_status'
    parameters = '&node=' + str(node)
    return sendMonitoringRequest(action, parameters)

def getRulesOnNode(node):
    action = '?action=get_rules_on_node'
    parameters = '&node=' + str(node)
    return sendMonitoringRequest(action, parameters)

# -------------------------------------
# ------------TRACEROUTE---------------
# -------------@bardini----------------

def initCircuitTraceroute(circuit, workgroupId, node, interface):
    action = '?action=init_circuit_traceroute'
    parameters = '&circuit=' + str(circuit) + '&workgroup_id=' + str(workgroupId) + '&node=' + str(node) + '&interface=' + str(interface)
    return sendTracerouteRequest(action, parameters)

def getCircuitTraceroute(circuit, workgroupId):
    action = '?action=get_circuit_traceroute'
    parameters = '&circuit=' + str(circuit) + '&workgroup_id=' + str(workgroupId)
    return sendTracerouteRequest(action, parameters)

# -------------------------------------
# ------WORKGROUP/ACL MANAGEMENT-------
# -------------@bardini----------------

def getAllWorkgroups():
    action = '?action=get_all_workgroups'
    parameters = ''
    return sendWorkgroupManagementRequest(action, parameters)

def getAcls(interfaceId=None, interfaceAclId=None):
    action = '?action=get_acls'
    parameters = ''
    if interfaceId:
        parameters += "&interface_id=" + str(interfaceId)
    if interfaceAclId:
        parameters += "&interface_acl_id=" + str(interfaceAclId)
    return sendWorkgroupManagementRequest(action, parameters)

def addAcl(interfaceId, allowDeny, vlanStart, evalPosition=None, workgroupId=None, vlanEnd=None, notes=None):
    action = '?action=add_acl'
    parameters = "&interface_id=" + str(interfaceId) + "&allow_deny=" + str(allowDeny) + "&vlan_start=" + str(vlanStart)
    if evalPosition:
        parameters += "&eval_position=" + str(evalPosition)
    if workgroupId:
        parameters += "&workgroup_id=" + str(workgroupId)
    if vlanEnd:
        parameters += "&vlan_end=" + str(vlanEnd)
    if notes:
        parameters += "&notes=" + str(notes)
    return sendWorkgroupManagementRequest(action, parameters)

def updateAcl(interfaceAclId, interfaceId, allowDeny, vlanStart, evalPosition=None, workgroupId=None, vlanEnd=None, notes=None):
    action = '?action=update_acl'
    parameters = "&interface_acl_id=" + str(interfaceAclId) + "&interface_id=" + str(interfaceId) + "&allow_deny=" + str(allowDeny) + "&vlan_start=" + str(
        vlanStart)
    if evalPosition:
        parameters += "&eval_position=" + str(evalPosition)
    if workgroupId:
        parameters += "&workgroup_id=" + str(workgroupId)
    if vlanEnd:
        parameters += "&vlan_end=" + str(vlanEnd)
    if notes:
        parameters += "&notes=" + str(notes)
    return sendWorkgroupManagementRequest(action, parameters)

def removeAcl(interfaceAclId):
    action = '?action=remove_acl'
    parameters = "&interface_acl_id=" + str(interfaceAclId)
    return sendWorkgroupManagementRequest(action, parameters)

# -------------------------------------
# ----------MAIN FUNCTIONS-------------
# -------------@bardini----------------


def sendInformationRequest(action, parameters):
    response = requests.get('https://' + oessServer + '/oess/services/data.cgi' + action + parameters,
                            auth=(oessUser, oessPasswd), verify=False)
    print('\n\nRequest sent: '+ 'https://' + oessServer + '/oess/services/data.cgi' + action + parameters)
    response = str(response.text)
    return response

def sendProvisioningRequest(action, parameters):
    response = requests.get('https://' + oessServer + '/oess/services/provisioning.cgi' + action + parameters,
                            auth=(oessUser, oessPasswd), verify=False)
    print('\n\nRequest sent: '+ 'https://' + oessServer + '/oess/services/provisioning.cgi' + action + parameters)
    response = str(response.text)
    return response

def sendMeasurementRequest(action, parameters):
    response = requests.get('https://' + oessServer + '/oess/services/measurement.cgi' + action + parameters,
                            auth=(oessUser, oessPasswd), verify=False)
    print('\n\nRequest sent: '+ 'https://' + oessServer + '/oess/services/measurement.cgi' + action + parameters)
    response = str(response.text)
    return response

def sendMonitoringRequest(action, parameters):
    response = requests.get('https://' + oessServer + '/oess/services/monitoring.cgi' + action + parameters,
                            auth=(oessUser, oessPasswd), verify=False)
    print('\n\nRequest sent: '+ 'https://' + oessServer + '/oess/services/monitoring.cgi' + action + parameters)
    response = str(response.text)
    return response

def sendTracerouteRequest(action, parameters):
    response = requests.get('https://' + oessServer + '/oess/services/traceroute.cgi' + action + parameters,
                            auth=(oessUser, oessPasswd), verify=False)
    print('\n\nRequest sent: '+ 'https://' + oessServer + '/oess/services/traceroute.cgi' + action + parameters)
    response = str(response.text)
    return response

def sendWorkgroupManagementRequest(action, parameters):
    response = requests.get('https://' + oessServer + '/oess/services/workgroup_manage.cgi' + action + parameters,
                            auth=(oessUser, oessPasswd), verify=False)
    print('\n\nRequest sent: '+ 'https://' + oessServer + '/oess/services/workgroup_manage.cgi' + action + parameters)
    response = str(response.text)
    return response

def printJson(string):
    jsonFile = json.loads(string)
    print 'Json returned:'
    print json.dumps(jsonFile, indent=3, sort_keys=True)

def main():
    return 0

if __name__ == "__main__":
    main()