import os
from langchain.document_loaders.csv_loader import CSVLoader
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory


def get_chatbot_chain():
    # setting env variables
    load_dotenv()
    loader = CSVLoader(file_path="faq.csv")
    documents = loader.load()

    openai_api_key = os.getenv('OPENAI_API_KEY')
    embeddings_model = OpenAIEmbeddings(openai_api_key=openai_api_key)

    # example of text to vectors conversion
    # embeddings = embeddings_model.embed_documents(["Hi there!", "Oh, hello!"])

    vectorstore = FAISS.from_documents(documents, embeddings_model)  # store documents/vectors in DB (FAISS)
    # results=vectorstore.similarity_search('Do you have free plan?') -> "similarity search" in vectorstore (with txt input)
    llm_model = ChatOpenAI(openai_api_key=openai_api_key)
    memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)

    # -------------- MAIN ------------------------------------------------------------------------------
    chain = ConversationalRetrievalChain.from_llm(llm=llm_model,  # OpenAI
                                                  retriever=vectorstore.as_retriever(),  # FAISS
                                                  memory=memory)  # langchain lib.
    # --------------------------------------------------------------------------------------------------

    # Return 3 most relevant documents
    # vectorstore.as_retriever(search_kwargs={"k": 3})

    return chain



