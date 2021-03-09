import requests
import json


def makeApiRequestForIndianStates(states_name):
        url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api_india"

        headers = {
            'x-rapidapi-key': "455ca3453dmshb8986f5a379f1dap136e13jsn59e42c7243d8",
            'x-rapidapi-host': "corona-virus-world-and-india-data.p.rapidapi.com"
            }
        querystring=states_name    
        response = requests.request("GET", url, headers=headers)
        # print(response.text)
        js = json.loads(response.text)
        #print("******", js)
        query=js.get('state_wise').get(querystring)
        print(query)
        #result = js.get('list')
        return query


raj="Rajasthan"        
makeApiRequestForIndianStates(raj)