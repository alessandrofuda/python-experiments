import os
from langchain.document_loaders.csv_loader import CSVLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from dotenv import load_dotenv


# setting env variables
# dotenv_path = Path('path/to/.env')
load_dotenv()
loader = CSVLoader(file_path="faq.csv")
documents = loader.load()
# print(documents)

openai_api_key = os.getenv('OPENAI_API_KEY')
embeddings_model = OpenAIEmbeddings(openai_api_key=openai_api_key)


# example of text to vectors conversion
embeddings = embeddings_model.embed_documents(
    [
        "Hi there!",
        "Oh, hello!"
    ]
)
print(embeddings)
# exit()

