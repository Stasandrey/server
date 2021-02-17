#! /usr/bin/python3

import os
from flask import Flask, make_response, request

app = Flask(__name__)


def transform():
    os.system("rm -f archive.zip")
    os.system("rm -f images/*.png")
    os.system("./make_stickers.py")
    os.system("zip -r archive.zip images/")
    # return text_file_contents.replace("=", ",")


@app.route('/')
def form():
    return """
        <html>
            <body>
                <h1>Преобразование этикеток с кодами маркировки.</h1>
                <form action="/transform" method="post" enctype="multipart/form-data">
                    <input type="file" name="data_file" />
                    <input type="submit" />
                </form>
            </body>
        </html>
    """


@app.route('/transform', methods=["POST"])
def transform_view():
    file = request.files['data_file']
    if not file:
        return "No file"
    file.save("flask_tmp.pdf")
    # file_contents = file.stream.read().decode("utf-8")
    transform()

    with open("archive.zip","rb") as f_out:
        result = f_out.read()

    response = make_response(result)
    response.headers["Content-Disposition"] = "attachment; filename=result.zip"
    return response


if __name__ == '__main__':
    app.run()
