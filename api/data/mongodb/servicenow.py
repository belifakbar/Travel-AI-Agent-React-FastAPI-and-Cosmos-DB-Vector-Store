from .init import client, vector_store
from langchain.docstore.document import Document
from typing import List, Optional, Union

from model.servicenow import Incident,Incidentmetadata

import locale


def results_to_incidents(result:Document) -> Incident:
    return Incident(number = result.metadata["number"],
                    description = result.metadata["description"],
                    closenote = result.metadata["closenotes"],
                    state = result.metadata["state"],
                    priority = result.metadata["priority"],
                    openedAt = result.metadata["openedAt"],
                    createdOn = result.metadata["createdOn"],
                    updatedOn = result.metadata["updatedOn"])

def metadata_search(name:str) -> list[Incidentmetadata]:
    data = []
    db = client["travel"]
    collection_name = db["itinerary"]
    id = get_ship_by_name(name)
    if id != '':
        print(id)
        cursor  = collection_name.find({'ship.shipid':id})
        locale.setlocale( locale.LC_ALL, '' )
        for item in cursor:
            data.append(Itinerary(ShipID=item['ship']['shipid'],
                                Name=item['name'], 
                                Rooms=[f" room {p['name']} price {locale.currency(p['price'])} " for p in item['prices']],
                                Schedule=[f" day {p['Day']} {p['type']} location {p['location']} " for p in item['itinerary']]
                        ))
        print(data)
    return data


# def get_ship_by_name(name:str)->str:
#     db = client["travel"]
#     collection_name = db["ships"]
#     print(f"-{name}-")
#     ship = collection_name.find_one({'name': name.strip()})
#     #ship = collection_name.find({"$text": {"$search": name.strip()}}).limit(1)
#     if ship == None: return '' 
#     if 'shipid' in ship:
#         return ship['shipid']
#     else:
#         print('ship not found')
#         return ''


# def itnerary_search(name:str) -> list[Itinerary]:
#     data = []
#     db = client["travel"]
#     collection_name = db["itinerary"]
#     id = get_ship_by_name(name)
#     if id != '':
#         print(id)
#         cursor  = collection_name.find({'ship.shipid':id})
#         locale.setlocale( locale.LC_ALL, '' )
#         for item in cursor:
#             data.append(Itinerary(ShipID=item['ship']['shipid'],
#                                 Name=item['name'], 
#                                 Rooms=[f" room {p['name']} price {locale.currency(p['price'])} " for p in item['prices']],
#                                 Schedule=[f" day {p['Day']} {p['type']} location {p['location']} " for p in item['itinerary']]
#                         ))
#         print(data)
#     return data



def similarity_search(query:str)-> list[Incident]:

    docs = vector_store.similarity_search_with_score(query,2)

    # Cosine Similarity:
    #It measures the cosine of the angle between two vectors in an n-dimensional space.
    #The values of similarity metrics typically range between 0 and 1, with higher values indicating greater similarity between the vectors.
    docs_filters = [doc for doc, score  in docs if score >=.78]

    # List the scores for documents
    for doc, score  in docs:
        print(score)

    # Print number of documents passing score threshold
    print(len(docs_filters))
  
    return [results_to_incidents(document) for document in docs_filters]
  

