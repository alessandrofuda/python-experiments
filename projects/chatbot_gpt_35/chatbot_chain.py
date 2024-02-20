import os
from langchain.document_loaders.csv_loader import CSVLoader
# from langchain.embeddings.openai import OpenAIEmbeddings  #  deprecating
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from langchain.vectorstores import FAISS
# from langchain_community.vectorstores import FAISS


# setting env variables
# dotenv_path = Path('path/to/.env')
load_dotenv()
loader = CSVLoader(file_path="faq.csv")
documents = loader.load()

# print(documents)
# exit(200)

openai_api_key = os.getenv('OPENAI_API_KEY')
embeddings_model = OpenAIEmbeddings(openai_api_key=openai_api_key)

# print(embeddings_model)
# exit()

# example of text to vectors conversion
embeddings = embeddings_model.embed_documents(
    [
        "Hi there!",
        "Oh, hello!"
    ]
)

# print(embeddings)
# exit()

vectorstore = FAISS.from_documents(documents, embeddings_model)

# print(vectorstore)
# exit()

results = vectorstore.similarity_search('Do you have a free plan?')
print(results)
exit()


