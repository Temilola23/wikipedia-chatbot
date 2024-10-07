from llama_index.core.memory import ChatMemoryBuffer
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.core.agent import ReActAgent
from llama_index.llms.openai import OpenAI
import chainlit as cl
from chainlit.input_widget import Select, TextInput
import openai
from utils import get_apikey
from index_wikipages import create_index

index = None


@cl.on_chat_start
async def on_chat_start():
    global index
    global agent
    # Settings
    
    # These are other models that could be used
    # , "gpt-3.5-turbo-16k", "gpt-4", "gpt-4-32k", "gpt-4o", "gpt-4o-mini", "o1-preview", "o1-mini", "gpt-4-turbo", "dall-e-3"
    settings = await cl.ChatSettings(
        [
            Select(
                id= "MODEL",
                label= "OpenAI - Model",
                values=["gpt-4o", "gpt-3.5-turbo-16k", "gpt-4", "gpt-4-32k", "gpt-4o", "gpt-4o-mini"],
                initial_index=0,
            ),
            
            TextInput(id="WikiPageRequest", label="Request Wikipage"),
        ]
    ).send()


def wikisearch_engine(index):
    query_engine = index.as_query_engine(
        response_mode = "compact",
        verbose = True,
        similarity_top_k = 3
    )
    
    # Add logging to debug the queries and results
    print(f"Query Engine created for index: {index}")
    
    return query_engine


def create_react_agent(MODEL):
    query_engine_tools = [
        QueryEngineTool(
            query_engine=wikisearch_engine(index),
            metadata=ToolMetadata(
                name='Wikipedia', 
                description="Useful for performing searches on Wikipedia knowledgebase"
            ),
        )
    ]

    openai.api_key = get_apikey()
    llm = OpenAI(model=MODEL)
    
    # Create a ChatMemoryBuffer with a token limit (e.g., 1000 tokens)
    memory = ChatMemoryBuffer(token_limit=1000)
    
    # Add detailed logging for the agent's responses and actions
    print("Creating ReActAgent with the following tools:", query_engine_tools)
    # Create a ChatMemoryBuffer with a token limit (e.g., 1000 tokens)
    # memory = ChatMemoryBuffer(token_limit=1000)
    
    # Log the agent creation
    print("ReActAgent is being created with model:", MODEL)
    
    agent = ReActAgent.from_tools(tools=query_engine_tools, llm=llm, verbose=True, memory=memory)
    return agent


@cl.on_settings_update
async def setup_agent(settings):
    global agent
    global index
    query = settings["WikiPageRequest"]
    if not isinstance(query, str):
        query = str(query)
    index = create_index(query)
    print("Index created for query:", query)

    print("on_settings_update", settings)
    MODEL = settings["MODEL"]
    if not isinstance(MODEL, str):
        MODEL = str(MODEL)
    agent = create_react_agent(MODEL)
    await cl.Message(
        author="Agent", content=f"""Wikipage(s) "{query}" successfully indexed"""
    ).send()


@cl.on_message
async def main(message: str):
    global agent
    if agent:
        print("Agent is available, processing message.")
    print("Received message:", message)
    if not isinstance(message, str):
        message = str(message)
    if agent:
        print("Agent is available, processing message.")
        # Log the message being sent to the agent
        print(f"User Query: {message}")
        response = await cl.make_async(agent.chat)(message)
        # Log the response from the agent
        print(f"Agent Response: {response}")

        await cl.Message(author="Agent", content=response).send()
    else:
        print("Agent is not available.")