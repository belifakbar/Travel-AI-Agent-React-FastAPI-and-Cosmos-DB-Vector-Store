from os import environ
import urllib
from dotenv import load_dotenv
from pymongo import MongoClient
from langchain_openai import OpenAIEmbeddings , AzureOpenAIEmbeddings
from langchain_community.vectorstores.azure_cosmos_db import AzureCosmosDBVectorSearch



load_dotenv(override=True)


client: MongoClient | None = None
vector_store: AzureCosmosDBVectorSearch | None=None


def mongodb_init():
    # MONGO_CONNECTION_STRING = environ.get("MONGO_CONNECTION_STRING")
    MONGO_PWD = environ.get("MONGO_PWD")
    MONGO_CONNECTION_STRING = "mongodb+srv://upmadmin:" + urllib.parse.quote(MONGO_PWD) + "@cosmos-upmaisearch-dev-002.mongocluster.cosmos.azure.com/?tls=true&authMechanism=SCRAM-SHA-256&retrywrites=false&maxIdleTimeMS=120000"
    DB_NAME = "travel"
    COLLECTION_NAME = "ships"
    INDEX_NAME = "vectorSearchIndex"

    model_deployment = environ.get("OPENAI_EMBEDDINGS_DEPLOYMENT", "smart-agent-embedding-ada")
    model_name       = environ.get("OPENAI_EMBEDDINGS_MODEL_NAME", "text-embedding-ada-002")
    
    global client, vector_store
    client = MongoClient(MONGO_CONNECTION_STRING)
    vector_store = AzureCosmosDBVectorSearch.from_connection_string(MONGO_CONNECTION_STRING,
                                                                    DB_NAME + "." + COLLECTION_NAME,
                                                                    # OpenAIEmbeddings(disallowed_special=()),
                                                                    AzureOpenAIEmbeddings(azure_deployment=model_deployment,openai_api_version="2023-05-15"),
                                                                    index_name=INDEX_NAME )                                                                  


mongodb_init()

