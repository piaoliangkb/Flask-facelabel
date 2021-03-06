from flask import Flask, render_template, request, redirect, url_for, flash
from flask_bootstrap import Bootstrap

import os
import shutil
import random
from datetime import timedelta

pathOfFaceImg = "./static/faceImg/"

app = Flask(__name__)
bootstrap = Bootstrap(app)

# app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=1)


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
        try:
            newName = request.args.get(list[i], None)
        except IndexError:
            break
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
                        filenewpath = newPath + "/" + str(i) + "-" + file
                    shutil.copyfile(fileoldpath, filenewpath)
                shutil.rmtree(oldPath)
                print("Merge two folders.")
            if mergeFlag:
                list.remove(list[i])
            else:
                list[i] = newName
            return redirect(url_for('.hello_world'))
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


@app.route('/adminadminadmin', methods=['GET'])
def enter_admin_page():

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
        try:
            newName = request.args.get(list[i], None)
        except IndexError:
            break
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
                        filenewpath = newPath + "/" + str(i) + "-" + file
                    shutil.copyfile(fileoldpath, filenewpath)
                shutil.rmtree(oldPath)
                print("Merge two folders.")
            if mergeFlag:
                list.remove(list[i])
            else:
                list[i] = newName
            return redirect(url_for('.enter_admin_page'))
    print(list)

    for i in range(numOfPeople):
        try:
            deleteInputValue = list[i] + "-delete"
            deletename = request.args.get(deleteInputValue, None)
        except IndexError:
            break
        if deletename:
            filepath = pathOfFaceImg + list[i]
            shutil.rmtree(filepath)
            list.remove(list[i])


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

    return render_template("admin.html", nameToPicpath=nameToPicpath)

@app.route('/test')
def myTest():
    return "hello,world"



if __name__ == '__main__':
    app.run()
