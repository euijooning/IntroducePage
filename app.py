from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.z7lpvbe.mongodb.net/Cluster0?retryWrites=true&w=majority')
db_sang = client.dbsparta

client = MongoClient('mongodb+srv://test:sparta@cluster0.pwqswla.mongodb.net/cluster0?retryWrites=true&w=majority')
db_comment = client.dbsparta


@app.route('/')
def home():


    return render_template('profile.html')

@app.route('/index')
def index():

    return render_template('index.html')


@app.route('/song')
def song():

    return render_template('song.html')
@app.route('/jung')
def jung():

    return render_template('jung.html')
@app.route('/jo')
def jo():

    return render_template('jo.html')
@app.route('/jin')
def jin():

    return render_template('jin.html')
@app.route('/sang')
def sang():

    return render_template('SangHwan.html')


@app.route('/comment')
def comment():

    return render_template('comment.html')




# SangHwan 영역시작 ------------------------------------------------------------------------------------

@app.route('/Sang')
def home_Sang():
    return render_template('SangHwan.html')

@app.route("/introduceData", methods=["POST"])
def introduce_post_Sang():
    img_url_receive = request.form['img_url_give']
    text_title_receive = request.form['text_title_give']
    text_receive = request.form['text_give']

    doc = {
        'img_url': img_url_receive,
        'text_title': text_title_receive,
        'text': text_receive
    }
    db_sang.introduceDatas.insert_one(doc)

    return jsonify({'msg':'기록 저장 완료!'})


@app.route("/introduceData", methods=["GET"])
def introduce_get_Sang():
    introduce_list = list(db_sang.introduceDatas.find({},{'_id':False}))
    return jsonify({'introduceDatas':introduce_list})
    # return jsonify({'msg':'GET 연결 완료!'})

@app.route("/introduceData", methods=["DELETE"])
def introduce_delete_Sang():
    text_title_receive = request.form['text_title_give']
    db_sang.introduceDatas.delete_one({'text_title':text_title_receive})
    return jsonify({'msg':'삭제 완료!'})

    name_receive = request.form['name_give']
    db.mystar.delete_one({'name': name_receive})
    return jsonify({'msg': '삭제 완료!'})

# SangHwan 영역끝 ------------------------------------------------------------------------------------



@app.route("/homework", methods=["POST"])
def homework_post_comment():
    name_receive = request.form["name_give"]
    comment_receive = request.form["comment_give"]

    doc = {
        'name': name_receive,
        'comment': comment_receive
    }
    db_comment.homework.insert_one(doc)
    return jsonify({'msg':'감사합니다 좋은 하루 보내세요!'})

@app.route("/homework", methods=["GET"])
def homework_get_comment():
    comment_list = list(db_comment.homework.find({},{'_id':False}))
    return jsonify({'comments':comment_list})




if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)





