from os import environ
import urllib
from dotenv import load_dotenv
from pymongo import MongoClient, database
from jsondataloader import JSONDataLoader
from langchain_openai import OpenAIEmbeddings , AzureOpenAIEmbeddings
from langchain_community.vectorstores.azure_cosmos_db import AzureCosmosDBVectorSearch, CosmosDBSimilarityType


load_dotenv(override=True)


class CosmosDBLoader():
    def __init__(
    self, DB_Name):
        # self.MONGO_CONNECTION_STRING = environ.get("MONGO_CONNECTION_STRING")
        self.MONGO_PWD = environ.get("MONGO_PWD")
        self.MONGO_CONNECTION_STRING = "mongodb+srv://upmadmin:" + urllib.parse.quote(self.MONGO_PWD) + "@cosmos-upmaisearch-dev-002.mongocluster.cosmos.azure.com/?tls=true&authMechanism=SCRAM-SHA-256&retrywrites=false&maxIdleTimeMS=120000"
        self.DB_NAME = DB_Name


    def __collection_exists(self,db:database, collection_name:str)->bool:
        collections = db.list_collection_names()
        if collection_name in collections: return True
        return False
    
    def __drop_collection(self,db:database, collection_name:str):
        if self.__collection_exists(db,collection_name):
            db.drop_collection(collection_name)
    

    
    def load_data(self,data:list,collection_name:str):
        """load documents into Cosmos DB Collection"""

        print(f"--load {collection_name}--")
        client = MongoClient(self.MONGO_CONNECTION_STRING)
        db = client[self.DB_NAME]

        self.__drop_collection(db,collection_name)
        collection = db[collection_name]
        
        collection.insert_many(data)

        return collection


    def load_vectors(self,data:list,collection_name:str):
        """load embeddings  into Cosmos DB vector store"""
      

        INDEX_NAME = "vectorSearchIndex"
        print(f"--load vectors {collection_name}--")
        client = MongoClient(self.MONGO_CONNECTION_STRING)
        db = client[self.DB_NAME]
        self.__drop_collection(db,collection_name)
        collection = db[collection_name]

        loader = JSONDataLoader( )

        docs = None
        if collection_name == 'incidents':
            docs = loader.load_incident(data)
        elif collection_name == 'requests':
                docs = loader.load_destination(data)
        

        if docs != None:
            # OpenAI Settings
            model_deployment = environ.get("OPENAI_EMBEDDINGS_DEPLOYMENT", "text-embedding-ada-002")
            model_name       = environ.get("OPENAI_EMBEDDINGS_MODEL_NAME", "text-embedding-ada-002")
            #load documents into Cosmos DB Vector Store
            vector_store = AzureCosmosDBVectorSearch.from_documents(
                docs,
                # OpenAIEmbeddings(disallowed_special=()),
                AzureOpenAIEmbeddings(azure_deployment=model_deployment,openai_api_version="2023-05-15"),
                collection=collection,
                index_name=INDEX_NAME)        

            if vector_store.index_exists() == False:
                #Create an index for vector search
                num_lists = 1 #for a small demo, you can start with numLists set to 1 to perform a brute-force search across all vectors.
                dimensions = 1536
                similarity_algorithm = CosmosDBSimilarityType.COS

                vector_store.create_index(num_lists, dimensions, similarity_algorithm)

        return collection
