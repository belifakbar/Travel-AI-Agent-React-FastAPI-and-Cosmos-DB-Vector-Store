from langchain_core.tools import tool
from langchain.docstore.document import Document
from data.mongodb import servicenow
from api.model.servicenow import Incident , Incidentmetadata


@tool
def incident_lookup(input:str) -> list[Document]:
    """find information on Incident detail"""
    incidents: list[Incident] = servicenow.similarity_search(input)
    content = ""

    for incident in incidents:
        content += f"Incident number {incident.number} \
                    description: {incident.description} \
                    close note : {incident.closenote} \
                    current state : {incident.state} \
                    having Priority level : {incident.priority}\
                    Open at : {incident.openedAt} \
                    Created on :{incident.createdOn} \
                    Updated on : {incident.updatedOn}"
    return content

@tool
def latestincident_lookup(number:str) -> str:
    """find information on Incident detail"""
    it = servicenow.Incidentmetadata(number)

    for i in it:
        results += f"Find the Incident number {i.number} with Latest Updated on : {i.updatedOn}"
    return results


# @tool
# def latestincident_lookup(number:str) -> str:
#     """find ship itinerary, cruise packages and destinations by ship name"""
#     it = servicenow.Incident(number)
#     results = ""

#     for i in it:
#         # results += f" Cruise Package {i.Name} room prices: {'/n-'.join(i.Rooms)} schedule: {'/n-'.join(i.Schedule)}"
#         results += f" Incident number {i.number} room prices: {'/n-'.join(i.Rooms)} schedule: {'/n-'.join(i.Schedule)}"

#     return results


# @tool
# def closenoteSuggestion(package_name:str, passenger_name:str, room: str )-> str:
#     """book cruise using package name and passenger name and room """
#     print(f"Package: {package_name} passenger: {passenger_name} room: {room}")

#     # LLM defaults empty name to John Doe 
#     if passenger_name == "John Doe":
#         return "In order to book a cruise I will need to know your name."
#     else:
#         if room == '':
#             return "which room would you like to book"            
#         return "Cruise has been booked, ref number is 343242"