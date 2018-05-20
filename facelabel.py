from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap

import os

pathOfFaceImg = "D:/ffmpeg/facelabel/static/faceImg/"

app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route('/', methods=['GET'])
def hello_world():

    # list[i] :the name of the sequence
    try:
        list = os.listdir(pathOfFaceImg)
    except OSError:
        list = []
    # numOfPeople :number of sequence
    numOfPeople = len(list)
    # nameToPicpath :name to filename of this people's picture
    nameToPicpath = {}

    for i in range(numOfPeople):
        newName = request.args.get(list[i], None)
        if newName:
            os.rename(pathOfFaceImg + list[i], pathOfFaceImg + newName)
            list[i] = newName

    for i in range(numOfPeople):
        pathOfPeople = pathOfFaceImg + list[i]
        try:
            filename = os.listdir(pathOfPeople)
        except OSError:
            filename = []
        picpath = []
        numOfpic = len(filename)
        if numOfpic > 8:
            numOfpic = 8
        for indexOfPic in range(0, numOfpic):
            filepath = "faceImg/" + list[i] + "/" + filename[indexOfPic]
            # print the path of picture
            # print(filepath)
            picpath.append(filepath)
        nameToPicpath[list[i]] = picpath

    return render_template("index.html", nameToPicpath=nameToPicpath)

@app.route('/test')
def myTest():
    return "hello,world"

if __name__ == '__main__':
    app.run()
