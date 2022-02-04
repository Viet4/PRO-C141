from flask import Flask, jsonify, request
import csv

with open("articles.csv", encoding="utf-8") as f:
    reader = csv.reader(f)
    data = list(reader)
    all_articles = data[1:]

liked_articles = []
disliked_articles = []

app = Flask(__name__)
@app.route("/get-articles")

def get_articles():
    return jsonify({
        "data": all_articles[0],
        "status": "success"
    })

@app.route("/liked-articles",methods=["POST"])

def like_articles():
    article = all_articles[0]
    other_articles = all_articles[1:]
    liked_articles.append(article)
    
    return jsonify({
        "status": "success"
    }),201

@app.route("/disliked-articles",methods=["POST"])

def dislike_articles():
    article = all_articles[0]
    other_articles = all_articles[1:]
    disliked_articles.append(article)
    
    return jsonify({
        "status": "success"
    }),201
    
app.run()