from cosmosdbloader import CosmosDBLoader
# from itinerarybuilder import ItineraryBuilder
import json


# cosmosdb_loader = CosmosDBLoader(DB_Name='travel')
cosmosdb_loader = CosmosDBLoader(DB_Name='servicenow')

#read in ship data
with open('loader/documents/incidents.json') as file:
        incidents_json = json.load(file)

#read in destination data
with open('loader/documents/requests.json') as file:
        requests_json = json.load(file)

# builder = ItineraryBuilder(ship_json['ships'],destinations_json['destinations'])

# Create five itinerary pakages
# itinerary = builder.build(5)

# Save itinerary packages to Cosmos DB
# cosmosdb_loader.load_data(itinerary,'itinerary')

# Save destinations to Cosmos DB
# cosmosdb_loader.load_data(requests_json['destinations'],'destinations')

# Save ships to Cosmos DB, create vector store
collection = cosmosdb_loader.load_vectors(incidents_json['incident'],'incidents')

# Add text search index to incident number
collection.create_index([('number', 'text')])

# collection = cosmosdb_loader.load_vectors(requests_json['requests'],'requests')

# Add text search index to request number
# collection.create_index([('number', 'text')])