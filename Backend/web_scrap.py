from googlesearch import search
from time import time
from langchain_community.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

def load_data_from_links(links):
    st_time=time()
    try:
        loader = WebBaseLoader(links)
        web_data = loader.load()
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=500, chunk_overlap=50
        )
        web_splitted = text_splitter.split_documents(web_data)
        print("Total Time is taken for Scrapping is : ", time.time() - st_time)
        return web_splitted
    except Exception as e:
        return None

def search_urls(query):
    st_time=time()
    urls=[]
    for url in search(query, tld="com",safe=True,tbs='qdr:d', num=10, stop=5, pause=1):
        urls.append(url)
    print("Total time for Scraping Urls :",time()-st_time)
    response=load_data_from_links(urls)
    return response

def scrap_urls(query):
    st_time=time()
    urls=[]
    for url in search(query, tld="com",safe=True,tbs='qdr:d', num=10, stop=2, pause=1):
        urls.append(url)
    print("Total time for Scraping Urls :",time()-st_time)
    return urls