from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap

import os
import shutil
import random
from datetime import timedelta

pathOfFaceImg = "D:/ffmpeg/facelabel/static/faceImg/"

app = Flask(__name__)
bootstrap = Bootstrap(app)

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=1)


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
        mergeFlag = False
        if newName:
            oldPath = pathOfFaceImg + list[i]
            newPath = pathOfFaceImg + newName
            try:
                os.rename(oldPath, newPath)
            except FileExistsError:
                mergeFlag = True
                # list the files in old folders
                files = os.listdir(oldPath)
                for file in files:
                    fileoldpath = oldPath + "/" + file
                    filenewpath = newPath + "/" + file
                    # if exists the file name
                    if os.path.exists(fileoldpath):
                        filenewpath = newPath + "/" + str(random.random()) + '.jpg'
                        print(filenewpath)
                    shutil.copyfile(fileoldpath, filenewpath)
                shutil.rmtree(oldPath)
                print("Merge two folders.")
            if mergeFlag:
                list.remove(list[i])
            else:
                list[i] = newName
    print(list)


    for i in range(len(list)):
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
