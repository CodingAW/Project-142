from flask import Flask, jsonify, request
from storage import allArticles, likedArticles, unlikedArticles
from demoFiltering import output
from contentFiltering import get_reccommendations

app = Flask(__name__)

@app.route('/getData')
def getArticleData():
    return jsonify({
        "data": allArticles[0],
        "status": "Success"
    }), 400


@app.route('/getLikedData', methods=['POST'])
def getLikedMovies(allArticles=allArticles):
    article = allArticles[0]
    allArticles = allArticles[1:]
    likedArticles.append(article)
    return jsonify({
        "status": "Success" 
    }), 400 
    
@app.route('/getUnlikedData', methods=['POST'])
def getUnlikedMovies(allArticles=allArticles):
    article = allArticles[0]
    allArticles = allArticles[1:]
    unlikedArticles.append(article)
    return jsonify({
        "status": "Success" 
    }), 400 

@app.route("/getPopularArticles")
def getPopArticles():
    popularData = []
    for article in output:
        aDict = {
            "title": article[0],
            "url": article[1],
            "total_events": article[2]
        }
        popularData.append(aDict)
    return jsonify({
        "data": popularData,
        "status": "Success"
    }), 400


@app.route("/getRecommendations")
def getRecom():
    recommendations = []
    for likedArticle in likedArticles:
        d = get_reccommendations(likedArticle[2])
        for data in d:
            recommendations.append(data)
    recomData = []
    for rec in recommendations:
        aDict = {
            "title": rec[0],
            "url": rec[1],
            "total_events": rec[2]
        }
        recomData.append(aDict)
    return jsonify({
        "data": recomData,
        "status": "Success"
    }), 400

if __name__ == '__main__':
    app.run()