#! /usr/bin/python3

import os
from flask import Flask, make_response, request
from multiprocessing import Process

app = Flask(__name__)

work = 0

def transform():
    with open('status.sts', 'wt') as f:
        f.write('1')
    with open( 'num.txt', 'wt' ) as f:
        f.write( '0' )

    os.system("rm -f archive.zip")
    os.system("rm -f images/*.png")
    os.system("./make_stickers.py")
    os.system("zip -r archive.zip images/")
    # return text_file_contents.replace("=", ",")
    with open('status.sts', 'wt') as f:
        f.write('2')

@app.route('/')
def form():
    if os.path.exists('status.sts'):
        with open('status.sts', 'rt') as f:
            work = f.read(1)
    else:
        with open('status.sts', 'wt') as f:
            f.write('0')
            work = '0'
    print(work)
    res_get = """
            <html>
                <body>
                    <h1>Забрать отформатированные этикетки</h1>
                    <form action="/transform" method="post" enctype="multipart/form-data">
                        <input type="submit" />
                    </form>
                </body>
            </html>
        """
    res_ok =  """
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


    if work == '0':
        res = res_ok
    elif work == '1':
        with open('num.txt') as f:
            num = f.read()
        res_error = (
            f"<html>                                                    "
            f"    <body>                                                "
            f"        <h1>Извините в данный момент идет обработка</h1>  "
            f"        <h1>Обработано {num} кодов.</h1>                        "
            f"    </body>                                               "
            f"</html>                                                   "
        )
        res = res_error
    elif work == '2':
        res = res_get
    return res

@app.route('/transform', methods=["POST"])
def transform_view():
    if os.path.exists('status.sts'):
        with open('status.sts', 'rt') as f:
            work = f.read(1)
    else:
        with open('status.sts', 'wt') as f:
            f.write('0')
            work = '3'
    print(work)
    if work == '0':
        file = request.files['data_file']
        if not file:
            return "No file"
        file.save("flask_tmp.pdf")
        # file_contents = file.stream.read().decode("utf-8")
        thread = Process(target = transform)
        thread.start()
        response = '<script>document.location.href = document.referrer</script>'
        #make_response('OK')

    elif work == '2':
        with open("archive.zip","rb") as f_out:
            result = f_out.read()

        response = make_response(result)
        response.headers["Content-Disposition"] = "attachment; filename=result.zip"
        with open('status.sts', 'wt') as f:
            f.write('0')
    if work == '3':
        response = make_response('OK')
    return response


if __name__ == '__main__':
    app.run()
