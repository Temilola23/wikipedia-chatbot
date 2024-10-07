
# Wikipedia-Enhanced Conversational AI

## Overview

This project is an AI-powered chatbot built using **LlamaIndex**, **Chainlit**, and **OpenAI GPT models**. The chatbot is designed to perform intelligent retrievals from Wikipedia to answer user queries with high accuracy. By integrating **Retrieval-Augmented Generation (RAG)**, it allows users to query specific Wikipedia pages and get real-time responses based on the content of those pages.

## Features

- **Wikipedia Indexing:** Index Wikipedia pages and create a knowledge base from them.
- **RAG System:** Utilizes a Retrieval-Augmented Generation approach for more accurate and context-aware answers.
- **LLM-Powered Responses:** Uses OpenAI GPT models for generating natural language responses.
- **Custom Search Engine:** Implements a search engine that retrieves relevant information from indexed Wikipedia pages.
- **Chat Memory Buffer:** Maintains context throughout the conversation to provide coherent answers.

## Tech Stack

- **LlamaIndex** for indexing and querying Wikipedia pages.
- **Chainlit** for building a conversational user interface.
- **OpenAI GPT Models** for natural language understanding and generation.
- **Python** for backend development.
- **Pydantic** for handling structured data and validation.

## Getting Started

### Prerequisites

- Python 3.8+
- Install required dependencies by running:

```bash
pip install -r requirements.txt
```

### Setting Up API Keys

To use this project, you'll need your own OpenAI API key. Store your key in an `apikeys.yml` file in the following format:

```yaml
openai:
  api_key: "your_openai_api_key_here"
```

Make sure this file is not included in your repository to avoid exposing your API key.

### How to Run

1. Clone the repository:

```bash
git clone https://github.com/yourusername/wikipedia-chatbot.git
```

2. Navigate to the project directory:

```bash
cd wikipedia-chatbot
```

3. Start the Chainlit server:

```bash
chainlit run chat_agent.py
```

### Project Structure

```plaintext
├── chainlit folder
  '── translations folder
    '── config.toml
├── .gitignore
├── apikeys.yml
├── chat_agent.py
├── index_wikipages.py
├── README.md
├── requirements.txt
├── utils.py
```
