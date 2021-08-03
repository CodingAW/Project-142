import csv
from os import read

allArticles = []

with open('articles.csv') as f:
    reader = csv.reader(f)
    data = [reader]   
    allArticles = data[1:]

likedArticles = []
unlikedArticles = []