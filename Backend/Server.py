from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from langchain_community.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_groq import ChatGroq
from langchain.chains import create_retrieval_chain
from datetime import datetime, date, timedelta
from langchain_cohere import CohereEmbeddings
from time import time
import json, time
from markdown import markdown
from regex import retrieve_symbol
from web_scrap import search_urls, load_data_from_links, scrap_urls
from fastapi.middleware.cors import CORSMiddleware

groq_api_key = "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"
llm = ChatGroq(groq_api_key=groq_api_key, model_name="llama3-70b-8192", temperature=0.3)
embeddings_obj = CohereEmbeddings(
    model="embed-english-v3.0",
    cohere_api_key="MMOyX4mucyxwoquRR64u6SvoLAVPO75wYzRJJpfh",
)
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Query(BaseModel):
    description: str | None = None


@app.get("/ping")
async def ping():
    return "hi"


def first_response(query):
    loader = WebBaseLoader(
        "https://raw.githubusercontent.com/Ansh-Chamriya/forinstall/main/NSE_EQ.json",
    )
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    json_data = loader.load()
    json_splitted = text_splitter.split_documents(json_data)
    loaded_db = FAISS.load_local(
        "faiss_index", embeddings_obj, allow_dangerous_deserialization=True
    )
    db = loaded_db
    json_prompt = ChatPromptTemplate.from_template(
        """
    Given today's date {date} (which is {day}), answer user questions accurately and set the start and end dates as per the question. If no period is specified, use 'day' from today to the past 30 days. Choose the time frame from [1minute, 30minute, day, week, month].

    Context:
    <context>
    {context}
    </context>

    Generate URLs based on user questions as follows:

    1. For specific days within the past 6 months:
        - url = 'https://api.upstox.com/v2/historical-candle/:instrument_key/1minute/:end_date'
    2. For specific months:
        - url = 'https://api.upstox.com/v2/historical-candle/:instrument_key/30minute/:end_date'
    3. For specific years:
        - url = 'https://api.upstox.com/v2/historical-candle/:instrument_key/day/:end_date/:start_date'
    4. For periods of days, weeks, or months:
        - url = 'https://api.upstox.com/v2/historical-candle/:instrument_key/day/:end_date/:start_date'

    For today's data for Axis Bank:
    - url = 'https://api.upstox.com/v2/historical-candle/intraday/:instrument_key/30minute'

    Example: 
    If the user asks for data of Axis, HDFC, and SBI banks for today, generate:
    [
        'https://api.upstox.com/v2/historical-candle/NSE_EQ|INE238A01034/30minute/{date}',
        'https://api.upstox.com/v2/historical-candle/NSE_EQ|INF179KC1DH4/30minute/{date}',
        'https://api.upstox.com/v2/historical-candle/NSE_EQ|INE123W01016/30minute/{date}'
    ]

    Do not use 1minute or 30minute for data older than 6 months.

    Questions:
    {input}

    Generate URLs in JSON format for each company mentioned in the input. If no company is specified, return None.

    Example: 
    If the prompt is "give the top 5 companies to invest in currently," return None in such type of all cases.

    Notice:
    Output JSON only any like [eg. Since the question is asking for the current stock price of Axis Bank, I will generate a URL for today's data. Here is the output:
    ]
    without extra characters,text or formatting.
    """
    )
    document_chain = create_stuff_documents_chain(llm, json_prompt)
    retriever = loaded_db.as_retriever()
    retrieval_chain = create_retrieval_chain(retriever, document_chain)
    response = retrieval_chain.invoke(
        input={
            "input": query,
            "context": json_splitted,
            "date": date.today(),
            "day": datetime.today().strftime("%A"),
        }
    )
    return db, response


def upstrox_data(data):
    if isinstance(data, list):
        print("Entered in region of list forms data block ..........")
        # url_dict = {"urls": [d["url"] for d in data]}
        links = data
    else:
        print("Entered in region of json forms data block ..........")
        json_object = json.dumps(data, indent=None)
        json_string = json.loads(json_object)
        for key in json_string:
            if key == "url":
                links = data["url"]
            elif key == "urls":
                links = data["urls"]
    return links


@app.post("/company")
async def company(query: Query):
    data = []
    loaded_db = FAISS.load_local(
        "faiss_index", embeddings_obj, allow_dangerous_deserialization=True
    )
    company = loaded_db.similarity_search(query.description)
    for comp in company:
        data.append(comp.page_content)
    data_string = str(data)
    response = retrieve_symbol(data_string)
    print(response)
    return response


@app.post("/predict")
async def predict(query: Query):
    news_splitted = None
    links = []
    db, response = first_response(query.description)
    print("first res is loaded.....")
    try:
        print("Entered in fisrt try block..........")
        print(data)
        data = response["answer"]
        if isinstance(data, str):
            data = json.loads(response["answer"])
            print(data)
        try:
            links = upstrox_data(data)
            print(links)
            web_splitted = load_data_from_links(links)
        except Exception as e:
            print("##" * 50)
            web_splitted = search_urls(query.description)
            print("Web data is updated of google.")

        try:
            news_links = [
                f"https://newsapi.org/v2/everything?q=(NSE%20AND%20BSE)&from={date.today()}&to={date.today()}&sortBy=popularity&apiKey=d1858fd8650743deb697aea90617d602",
                f"https://newsapi.org/v2/everything?&from={date.today()}&to={date.today()}domains=moneycontrol.com,cnbc.com,bloomberg.com,thehindubusinessline.com/topic/nse,nseindia.com/resources/exchange-communication-media-center&apiKey=d1858fd8650743deb697aea90617d602",
            ]
            loader = WebBaseLoader(news_links)
            news_web_data = loader.load()
            text_splitter = RecursiveCharacterTextSplitter(
                chunk_size=1000, chunk_overlap=200
            )
            news_splitted = text_splitter.split_documents(news_web_data)
        except Exception as e:
            news_splitted = None

        st_time = time()
        db = FAISS.from_documents(web_splitted, embeddings_obj)
        print("Time taken for Generating the Embeddings : ", time() - st_time)
        print("--" * 60)

    except Exception as e:
        web_splitted = None

    edited_prompt = ChatPromptTemplate.from_template(
        """
        By Using the Context as reference given below give the appropriate answer of the user question:

        <context>
        {context}
        </context>
        Question of user should be answered properly with the actual values within the context. If the data of today is not there, then if yesterday's date's data is there also use it for generation of response along with articles data but not significantly.

        If values have to predict, then use the context to analyze stock data variation trend properly and based on it predict the values with proper reasons. Also, mention the reasons along with some numerical data for predicting the values from data of context. Use the news for stock-market
        <News>
        {news}
        </News>
        as a reference for knowing about external factors affecting the market only but do not use the numeric values significantly for predicting and generation on response. use the overview of the news data. Include the title of the articles and the URLs of the news as well which you use.

        Questions:
        {input}

        Give the answer without commenting anything about the context and who is providing the data with response size almost around 1500-10,000 tokens and behave like you are a stocks advisor. If the prompt is general talks like [e.g., "hi", "what can you do for me"...] then respond according to your role.
        """
    )
    document_chain = create_stuff_documents_chain(llm, edited_prompt)
    retriever = db.as_retriever()
    retrieval_chain = create_retrieval_chain(retriever, document_chain)
    response = retrieval_chain.invoke(
        input={
            "input": query.description,
            "context": web_splitted,
            "news": news_splitted,
            "date": date.today(),
            "day": datetime.today().strftime("%A"),
        }
    )
    print("**" * 50)
    # response = response['answer'].replace("\n\n","\n")
    # response = response.replace("\n","")
    # print(response)
    # response=response['answer'].replace("\n","<br>")
    # response=response.replace("(",'<a>')
    # response=response.replace(")",'</a>')
    # response=response.replace('\"','*')
    # response=response.replace('/"','*')
    print(type(response))
    return response

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
