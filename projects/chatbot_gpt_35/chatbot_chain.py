import os
from langchain.document_loaders.csv_loader import CSVLoader

loader = CSVLoader(file_path="faq.csv")
documents = loader.load()
print(documents)


