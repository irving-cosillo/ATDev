# -*- coding: utf-8 -*-
import requests
from simple_salesforce import Salesforce, SalesforceLogin, SFType

#Salesforce Connection
username = ""
password = ""
security_token = ""
domain = "login"

session_id, instance = SalesforceLogin(username, password, security_token, domain)
sf = Salesforce(instance=instance, session_id=session_id)

#API Connection
url = "https://api.packetfabric.com/v2.1/locations"
request = requests.get(url)
locations = request.json()

siteLocations = []
for location in locations:
    siteLocations.append({
        "POP__c" : location["pop"],
        "Site__c" : location["site"],
        "ExternalID__c" : location["site_code"],
        "Address1__c" : location["address1"],
        "Address2__c" : location["address2"],
        "City__c" : location["city"],
        "Site__c" : location["state"],
        "Postal__c" : location["postal"],
        "Country__c" : location["country"]
    })

#Records insertion
siteLocationsResponse = sf.bulk.SiteLocation__c.insert(siteLocations)

    


