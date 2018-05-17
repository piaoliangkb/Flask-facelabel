from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap

import os

pathOfFaceImg = "D:/ffmpeg/facelabel/static/faceImg/"

app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route('/', methods=['GET'])
def hello_world():

    # list[i] :the name of the sequence
    list = os.listdir(pathOfFaceImg)
    # numOfPeople :number of sequence
    numOfPeople = len(list)
    # nameToPicpath :name to filename of this people's picture
    nameToPicpath = {}

    for i in range(numOfPeople):
        newName = request.args.get(list[i], None)
        print(newName)
        if newName:
            print("newName is not None")
            os.rename(pathOfFaceImg + list[i], pathOfFaceImg + newName)
            list[i] = newName

    for i in range(numOfPeople):
        pathOfPeople = pathOfFaceImg + list[i]
        filename = os.listdir(pathOfPeople)
        picpath = []
        for indexOfPic in range(0, 6):
            filepath = "faceImg/" + list[i] + "/" + filename[indexOfPic]
            picpath.append(filepath)
        nameToPicpath[list[i]] = picpath

    return render_template("index.html", nameToPicpath=nameToPicpath)

@app.route('/test')
def myTest():
    return "hello,world"

if __name__ == '__main__':
    app.run()
