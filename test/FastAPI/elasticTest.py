import elasticsearch
import csv

import os
from dotenv import load_dotenv

load_dotenv()

es = elasticsearch.Elasticsearch(
    cloud_id = 'seek_crawl:dXMtZWFzdC0yLmF3cy5lbGFzdGljLWNsb3VkLmNvbTo0NDMkNTI3NzdlMTc4OGU3NDczODk4ZDdiNTNlMTJlYWJjNjEkNWJiODBjM2Q0ZWMxNDg2Y2I4YWJiOTNlOTQ5M2UyODQ=',
    http_auth=("elastic", "GK8mFwq1WQHStaWHN1FrulJx"),
)

with open("seek_data.csv") as file:
    reader = csv.reader(file)
    for i, row in enumerate(reader):
        # Create a dictionary for each row with default column names
        document = {f"column{j}": value for j, value in enumerate(row)}
        # Save each row as a separate document in Elasticsearch
        res = es.index(index="my_index", id=i, body=document)
        print(res)