import sys

import face_recognition
import faceclass.TestOne
from flask import Flask
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

@app.route("/")
def hello_world():
    return "<p>Hello, World!"


@app.route("/developer")
def get_developer_name():
    return "Jay Bhavsar is Developer."


@app.route("/user/<int:userid>")
def show_user_profile(userid):
    if userid == 1:
        return "jay"
    else:
        return "paggu"


@app.route('/info', methods=['POST', 'GET'])
def fun():
    print("request hit.")
    return "post request successfull."


@app.route('/check')
def perform_check():
    # image = face_recognition.load_image_file("/home/laitmatus/Desktop/known_people/shahrukh.jpg")
    # face_locations = face_recognition.face_locations(image)
    # print('face_locations', face_locations)
    known_image = face_recognition.load_image_file("/home/laitmatus/Desktop/known_people/shahrukh.jpg")
    unknown_image = face_recognition.load_image_file("/home/laitmatus/Desktop/unknown_pictures")

    known_encoding = face_recognition.face_encodings(known_image)[0]
    unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

    results = face_recognition.compare_faces([known_encoding], unknown_encoding)

    print('result = ', results)

    return "dfd"



