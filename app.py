import glob
import sys

import face_recognition
import faceclass.TestOne
from flask import Flask
from flask_cors import CORS, cross_origin
import json

from pathlib import Path
from PIL import Image
import os
import os.path
from flask import request
# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

app = Flask(__name__)
CORS(app)


@app.route("/")
@cross_origin()
def hello_world():
    return "<h3>Welcome To FaceApp</h3>"


@app.route("/developer")
@cross_origin()
def get_developer_name():
    return "<h1>Laitmatus Software Pvt Ltd</h1>"


def create_app():
    return app
#
#
# @app.route("/user/<int:userid>")
# def show_user_profile(userid):
#     if userid == 1:
#         return "jay"
#     else:
#         return "paggu"
#
#
# @app.route('/info', methods=['POST', 'GET'])
# def fun():
#     print("request hit.")
#     return "post request successfull."


# @app.route('/check', methods=['POST'])
# def perform_check():
#     # image = face_recognition.load_image_file("/home/laitmatus/Desktop/known_people/shahrukh.jpg")
#     # face_locations = face_recognition.face_locations(image)
#     # print('face_locations', face_locations)
#
#     print('request.method', request.method)
#     print('request.form', request.form)
#     print('request.args', request.args)
#
#     known_image = face_recognition.load_image_file("/home/laitmatus/Desktop/known_people/shahrukh.jpg")
#     unknown_image = face_recognition.load_image_file("/home/laitmatus/Desktop/unknown_pictures")
#
#     known_encoding = face_recognition.face_encodings(known_image)[0]
#     unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
#
#     results = face_recognition.compare_faces([known_encoding], unknown_encoding)
#
#     print('result = ', results)
#
#     return "dfd"


@app.route('/getimages', methods=['POST'])
@cross_origin()
def get_image():
    knownfolder = request.form['knowns'] + '/*.jpg'
    image_to_find = request.form['findimg']

    # print('request = ', request)
    #
    # print('knownfolder', knownfolder)
    # print('image_to_find', image_to_find)

    response = {}
    for img in glob.glob(knownfolder):
        # print('img data ', img)
        known_image = face_recognition.load_image_file(img)
        unknown_image = face_recognition.load_image_file(image_to_find)

        known_encoding = face_recognition.face_encodings(known_image)[0]
        unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

        results = []
        results = face_recognition.compare_faces([known_encoding], unknown_encoding, 0.5)

        # print('result = ', results)
        # print(results[0] is True)
        # print(type(results[0]))

        if results[0]:
            response['status'] = True
            response['path'] = img
            return json.dumps(response)
            break

    response['status'] = False
    response['path'] = ""
    return json.dumps(response)
