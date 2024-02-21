import os
from langchain.document_loaders.csv_loader import CSVLoader
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain_community.callbacks import get_openai_callback


# setting env variables
load_dotenv()
loader = CSVLoader(file_path="faq.csv")
documents = loader.load()

# print(documents)
# exit()

openai_api_key = os.getenv('OPENAI_API_KEY')
embeddings_model = OpenAIEmbeddings(openai_api_key=openai_api_key)

# print(embeddings_model)
# exit()

# example of text to vectors conversion
# embeddings = embeddings_model.embed_documents(
#     [
#         "Hi there!",
#         "Oh, hello!"
#     ]
# )

# print(embeddings)
# exit()

vectorstore = FAISS.from_documents(documents, embeddings_model)  # store documents/vectors in DB (FAISS)

# print(vectorstore)
# exit()

# example of "similarity search" inside vector store (using text input)
# results = vectorstore.similarity_search('Do you have a free plan?')
# print(results)
# exit()


llm_model = ChatOpenAI(openai_api_key=openai_api_key)
chain = ConversationalRetrievalChain.from_llm(llm=llm_model, retriever=vectorstore.as_retriever())  # 'recuperatore'

# Return 3 most relevant documents
# vectorstore.as_retriever(search_kwargs={"k": 3})

query = "Do you have a team plan?"

with get_openai_callback() as cb:
    response = chain.invoke({"question": query, "chat_history": []})

print(response)
print(cb)


