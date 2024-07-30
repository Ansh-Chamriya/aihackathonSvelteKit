# Stock Saarthi

## Demo 

[![Watch the video](https://img.youtube.com/vi/eAKuxP3CdH8/0.jpg)](https://youtu.be/eAKuxP3CdH8)


This project provides a FastAPI-based locally hosted web-application to analyze and predict stock market trends using historical and real-time data. The API leverages various tools such as the LangChain library, FAISS for similarity search, and the Groq language model for generating responses based on the context.



## Note :

- Before Using the **Server.py** as backend please create your own **Groq api key** for good inferencing of llama-70b model ,which we are using in this.

- Also create the **Cohere api key** for faster embedding generation

  OR

  can be done with **OllamaEmbeddings** as well ,but it's taking too much time for generation of same.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Endpoints](#endpoints)
- [License](#license)

## Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/Ansh-Chamriya/aihackathonSvelteKit
    ```

    **Installing npm for UI-frontend**

    npm (Node Package Manager) is included with Node.js. You can verify the installation and version of npm by running the following command in your terminal:

      ```bash
      npm -v
      ```

    Install all the packages by using the following command

    ```bash
    npm i
    ```

    if it there then run following for starting UI :

    ```bash
    npm run dev
    ```

- **Optional:**

    ```bash
    python -m venv env
    source env/bin/activate
    ```

  On Windows use
  `   env\Scripts\activate
`

2. **Installing Dependencies :**

   ```bash
   pip install -r requirements.txt
   ```

Once all the dependencies are installed and your environments are good then go for next steps:

## Usage :

1. **Run the FastAPI Based Backend :**

   ```bash
   uvicorn Server:app --host localhost --port 8000
   ```

## Endpoints :

**GET /ping :**

- Description: Health check endpoint to verify that the API is running.
- Response: Returns a simple "hi" message.

**POST /company :**

- Description: Retrieve information about a specific company based on the query description.
- Request Body (JSON):
  ```json
  {
    "description": "Your String to  Query"
  }
  ```
- Response: Returns the company information based on the query.

**POST /predict :**

- Description: Predict stock market trends based on the query description.
- Request Body (JSON):

  ```json
  {
    "description": "Your String to  Query"
  }
  ```

- Response: Returns the predicted stock market data along with context and references.

## License

This project is licensed under the **MIT License**. See the **LICENSE** file for details.
