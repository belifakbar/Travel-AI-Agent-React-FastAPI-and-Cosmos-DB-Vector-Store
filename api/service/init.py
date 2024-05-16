from dotenv import load_dotenv
from os import environ , getenv
import urllib
from langchain.globals import set_llm_cache
from langchain_openai import ChatOpenAI,AzureChatOpenAI
from langchain_mongodb.chat_message_histories import MongoDBChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain.agents import AgentExecutor, create_openai_tools_agent
from service import TravelAgentTools as agent_tools

load_dotenv(override=True)


chat : ChatOpenAI | None=None
agent_with_chat_history : RunnableWithMessageHistory | None=None

def LLM_init():
    global chat,agent_with_chat_history
    # chat = ChatOpenAI(model_name="gpt-3.5-turbo-16k",temperature=0)
    
    # LANGSMITH
    environ['LANGCHAIN_TRACING_V2'] = getenv("LANGCHAIN_TRACING_V2")
    environ['LANGCHAIN_ENDPOINT']   = getenv("LANGCHAIN_ENDPOINT")
    environ['LANGCHAIN_API_KEY']    = getenv("LANGCHAIN_API_KEY")
    environ['LANGCHAIN_PROJECT']    = getenv("LANGCHAIN_PROJECT")

    environ["AZURE_OPENAI_API_VERSION"]     = "2023-05-15"
    environ["AZURE_OPENAI_ENDPOINT"]        = getenv("AZURE_OPENAI_ENDPOINT")
    environ["AZURE_OPENAI_API_KEY"]         = getenv("AZURE_OPENAI_API_KEY")
    environ["AZURE_OPENAI_CHAT_DEPLOYMENT_NAME"] = getenv("AZURE_OPENAI_CHAT_DEPLOYMENT_NAME")  # the deployment model name

    chat = AzureChatOpenAI(openai_api_version=environ.get("AZURE_OPENAI_API_VERSION"),azure_deployment=environ.get("AZURE_OPENAI_CHAT_DEPLOYMENT_NAME"),temperature=0)
    tools = [agent_tools.vacation_lookup, agent_tools.itinerary_lookup, agent_tools.book_cruise ]

    prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful and friendly travel assistant for a cruise company. Answer travel questions to the best of your ability providing only relevant information. In order to book a cruise you will need to capture the person's name.",
        ),
        MessagesPlaceholder(variable_name="chat_history"),
        ("user", "Answer should be embedded in html tags. {input}"),
         MessagesPlaceholder(variable_name="agent_scratchpad"),
    ]
    )

    #Answer should be embedded in html tags. Only answer questions related to cruise travel, If you can not answer respond with \"I am here to assist with your travel questions.\". 


    agent = create_openai_tools_agent(chat, tools, prompt)
    agent_executor  = AgentExecutor(agent=agent, tools=tools, verbose=True)
    MONGO_PWD = environ.get("MONGO_PWD")
    
    agent_with_chat_history = RunnableWithMessageHistory(
        agent_executor,
        lambda session_id: MongoDBChatMessageHistory( database_name="travel",
                                                collection_name="history",
                                                #    connection_string=environ.get("MONGO_CONNECTION_STRING"),
                                                connection_string= "mongodb+srv://upmadmin:" + urllib.parse.quote(MONGO_PWD) + "@cosmos-upmaisearch-dev-002.mongocluster.cosmos.azure.com/?tls=true&authMechanism=SCRAM-SHA-256&retrywrites=false&maxIdleTimeMS=120000"
                                                session_id=session_id),
        input_messages_key="input",
        history_messages_key="chat_history",
)

LLM_init()