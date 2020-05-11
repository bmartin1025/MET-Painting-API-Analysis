import requests, json

url = 'https://collectionapi.metmuseum.org/public/collection/v1/objects'
params = {'medium': 'Paintings', 'q': ''} #add in like q=search
r = requests.get('https://collectionapi.metmuseum.org/public/collection/v1/search?medium=Paintings&q=%22%22')#specific link to like sunflowers or paintings

#r = requests.get('https://api.dp.la/v2/items', params=payload)

data = json.loads(r.text)

artist_dict = {}
accessionYear_dict = {}
gender_dict = {'Male': 0, 'Female': 0}


for objectid in data['objectIDs']:
    try:
        objectresponse = requests.get('https://collectionapi.metmuseum.org/public/collection/v1/objects/{}' .format(objectid))

        objectinfo = json.loads(objectresponse.text)
        #print(objectid)
        artist = (objectinfo['artistAlphaSort'])
        if not artist_dict.get(artist):
            artist_dict[artist] = 1
        else:
            artist_dict[artist] = artist_dict.get(artist) + 1 
        #print(artist_dict)

        accessionYear = (objectinfo['accessionYear'])
        if not accessionYear_dict.get(accessionYear):
            accessionYear_dict[accessionYear] = 1
        else:
            accessionYear_dict[accessionYear] = accessionYear_dict.get(accessionYear) + 1

        gender = (objectinfo['artistGender'])
        if gender == 'Male':
            gender_dict['Male'] = gender_dict.get('Male') + 1
        elif gender == 'Female':
            gender_dict['Female'] = gender_dict.get('Female') + 1

        #print(gender_dict)

        #12765 has no info 
    except (TypeError, KeyError): 
        print("Object ID not found")
        pass
    
print('>> total number of unique artists: {}, and works per artist: [{}] \n'.format(len(artist_dict), artist_dict))
print('>> year accessioned: {} \n'.format(accessionYear_dict))
print('>> only {} of total {} had gender recorded'.format(len(data['objectIDs']), len(gender_dict)))
print('>> gender info found: {} \n'.format(gender_dict))
print(accessionYear_dict)
 

    
#add table for clearer layout of data?  
#import plotly.graph_objects as go

#fig = go.Figure(data=[go.Table(header=dict(values=['A Scores', 'B Scores']),
                # cells=dict(values=[[100, 90, 80, 90], [95, 85, 75, 95]]))
                  #   ])
#fig.show()    
    
    
    
    
#data = json.loads(r.text)
#print(data)
#get-asking post-sending
#r = requests.get("https://api.dp.la/v2/items?q=kittens&api_key=a0f432a12693938ad57971e01a27e201")
#turns into dictionary?
#response = requests.get(url, params=params)

#data = json.loads(response.text)
#to write easy2read json file: 
#json.dump(data, open("omdb_response.json", "w"), indent=2)
#for Ratings in data['Ratings']: 
     #print (Ratings['Source'])
    
 