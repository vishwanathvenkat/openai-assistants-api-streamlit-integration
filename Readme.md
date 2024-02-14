<sub><sup>*This readme was auto-generated using LLM prompts*</sup></sub>
# 1. Introduction
This repository contains the code for a web application designed to interact with the OpenAI Assistants API. The application leverages Streamlit for the front end to provide an intuitive user interface where users can input their queries. These queries are then processed by a backend script that communicates with the OpenAI Assistants API to generate responses. This application serves as a bridge between users and powerful language models, enabling a wide range of applications from automated customer support to interactive educational tools.

# 2. Pre-requisites
## Setting Up the OpenAI API Key
To successfully run the code in this repository, you need access to the OpenAI API, which requires an API key. If you don't already have one, you can acquire it by following these steps:

1. Visit OpenAI's API page.
2. Sign up or log in to create a new account or access an existing one.
3. Navigate to the “API” section on the dashboard to find your API keys.
4. Generate a new API key if you haven't done so already.
5. Remember to keep your API key confidential and do not expose it in your codebase.

## Creating an OpenAI Assistant
Although this project's script is designed to work with the general API, personalizing interactions through a specific Assistant can enhance the experience. To create an OpenAI Assistant, follow these steps:

1. Log in to the OpenAI platform.
2. Go to the "Assistants" section in the side menu.
3. Click on "Create new assistant" and follow the on-screen instructions to customize it according to your needs.
4. The system message you enter for the assistant will be the brain behind the whole project.

## Cloning the repository
```
git clone https://github.com/vishwanathvenkat/openai-assistants-api-streamlit-integration
```

## Setting Up the Environment
Navigate to the project directory in your terminal, and run the following command to create a virtual environment named env:

    python -m venv env



For Windows, activation of the virtual environment is different and can be done through:

    .\env\Scripts\activate
On macOS and Linux:

    source env/bin/activate
Install Requirements: With the virtual environment activated, install the required packages using the provided requirements.txt file:

    pip install -r requirements.txt

## Setting up environment variables
Create a `.env` file in the project folder (remember to add it to your .gitignore file) and have the following variables set

1. OPENAI_API_KEY=""
2. ASSISTANT_ID=""


# 3. Flow
The code's flow is designed to be straightforward and user-friendly:

1. User Input: The user enters their query into the Streamlit-based frontend interface. This can be anything from a question to a command intended for the AI.

2. Streamlit Frontend: The frontend captures the user's input and, with a press of a button, sends the request to the backend script for processing.

3. Backend Processing: The backend, written in Python, takes the user’s input and forms a request to the OpenAI Assistants API using the previously acquired API key. If you have a specific Assistant configured, it directs the request to it.

4. OpenAI Assistants API: The API processes the request, leveraging OpenAI’s language models to generate an appropriate response based on the input.

5. Response to User: The generated response is sent back through the flow – from the API to the backend, and finally displayed on the Streamlit frontend for the user to read.

# 4. Demo
A demonstration of the application can be accessible by running the Streamlit application. To get started:


1. Navigate to the project directory in your terminal.
2. Execute streamlit run app.py to start the application.
3. The application should now be running locally on your browser, ready for input.

The video below shows a basic movie recommendation bot in action.
[![](streamlit-seeklogo.svg)](https://youtu.be/6Z6ZcoBW-C0)

# 5. Future Enhancements
While the current version of the application offers a basic functionality to interact with the OpenAI Assistants API, several enhancements are planned for the future to improve user experience and broaden application use cases:

1. UI/UX Improvements: Upgrading the Streamlit interface for a more intuitive and visually appealing interaction.
2. Support for Multiple Languages: Extending the application's capabilities to process input and generate responses in various languages.
3. Advanced Error Handling: Implementing more sophisticated error handling mechanisms to provide users with helpful feedback on how to resolve issues.
4. Analytics Dashboard: Incorporating an analytics feature to monitor usage patterns, frequent queries, and user engagement.
5. Opensource LLMs: The code's flow currently supports only OpenAI assistants. Enable a easy switching mechanism to control the choice of LLMs.