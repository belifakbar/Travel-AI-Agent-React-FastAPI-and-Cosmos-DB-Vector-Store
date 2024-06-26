# AI Travel Agent Powered by Azure Cosmos DB and LangChain

## Overview
This repository explores the implementation of a LangChain Agent using Azure Cosmos DB for MongoDB vCore to handle traveler inquiries and bookings. The project provides detailed instructions for setting up the environment and loading travel data, aiming to empower developers to integrate similar agents into their solutions. To gain a comprehensive understanding of the project, refer to the article: [Empower your AI Agent with Azure Cosmos DB](https://stochasticcoder.com/2024/05/05/empower-your-ai-agent-with-azure-cosmos-db/).

## Objectives

- Develop a conversational AI agent capable of understanding natural language input.
- Implement a robust backend system using Python FastAPI for handling user requests and interactions.
- Utilize LangChain for natural language understanding and processing, enabling the AI agent to comprehend user intents and context.
- Integrate Azure Cosmos DB as the database solution for storing conversation history, user preferences, and other relevant data.
- Design a user-friendly front-end interface using React JS, providing an intuitive platform for users to interact with the AI agent.

![travel agent chat](images/travel_agent_chat.PNG)

## Requirements
- Azure subscription for deploying Azure Cosmos DB for MongoDB vCore.
- Python environment with LangChain installed.
- Basic knowledge of MongoDB and natural language processing concepts.

## Usage
1. Follow the steps provided in the README file.

## Steps
1. [Step 1](loader) - Load  Cosmos DB for Mongo DB Vector Store using sample dataset
2. [Step 2](api) - Create FastAPI to integrate LangChain RAG pattern with web front-end.
3. [Step 3](web) - Build the React web front-end to ask 'grounded' questions of your data and view relevant documents. 
4. Follow the setup instructions provided in the README file.
5. Run the demo application and explore the RAG pattern in action.

## License
This project is licensed under the [MIT License](MIT.md), granting permission for commercial and non-commercial use with proper attribution.

## Support
For any questions or issues, please [open an issue](https://github.com/jonathanscholtes/Travel-AI-Agent-React-FastAPI-and-Cosmos-DB-Vector-Store/issues) on GitHub or reach out to the project maintainers.

## Disclaimer
This demo application is provided for educational and demonstration purposes only. Use at your own risk.