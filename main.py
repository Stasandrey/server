#! /usr/bin/python3

import os
from flask import Flask, make_response, request
from multiprocessing import Process

app = Flask(__name__)

work = 0




@app.route('/')
def main_page():
    return """
           <html> 
             <head>
                <title>Выберите тип формируемых этикеток:</title>
             </head>
             <body>
              <h1><b>Ознакомительный период истекает 15.03.2021 </b></h1>             
              <p>Выберите тип этикеток</p>
              <p><a href="/ds">Давальческое сырье</a></p>
              <p><a href="/ns">Собственное сырье</a></p>
              <p><a href="/dag">ИП Шаяхметов</a></p>
             </body>
           </html>
           """
@app.route('/dag')
def form_dag():
    if os.path.exists('status_dag.sts'):
        with open('status_dag.sts', 'rt') as f:
            work = f.read(1)
    else:
        with open('status_dag.sts', 'wt') as f:
            f.write('0')
            work = '0'
    print(work)
    res_get = """
            <html>
                <body>
                    <h1>Забрать отформатированные этикетки</h1>
                    <form action="/transform_dag" method="post" enctype="multipart/form-data">
                        <input type="submit" />
                    </form>
                </body>
            </html>
        """
    res_ok =  """
        <html>
            <body>
                <h1>Преобразование этикеток с кодами маркировки ИП Шаяхметов.</h1>
                <form action="/transform_dag" method="post" enctype="multipart/form-data">
                    <input type="file" name="data_file" />
                    <input type="submit" />
                </form>
            </body>
        </html>
    """

    if work == '0':
        res = res_ok
    elif work == '1':
        with open('num_dag.txt') as f:
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

def transform_dag():
    with open('status_dag.sts', 'wt') as f:
        f.write('1')
    with open( 'num_dag.txt', 'wt' ) as f:
        f.write( '0' )

    os.system("rm -f archive_dag.zip")
    os.system("rm -f images_dag/*.png")
    os.system("./make_stickers_dag.py")
    os.system("zip -r archive_dag.zip images_dag/")
    # return text_file_contents.replace("=", ",")
    with open('status_dag.sts', 'wt') as f:
        f.write('2')

@app.route('/transform_dag', methods=["POST"])
def transform_view_dag():
    if os.path.exists('status_dag.sts'):
        with open('status_dag.sts', 'rt') as f:
            work = f.read(1)
    else:
        with open('status_dag.sts', 'wt') as f:
            f.write('0')
            work = '3'
    print(work)
    if work == '0':
        file = request.files['data_file']
        if not file:
            return "No file"
        file.save("flask_tmp_dag.pdf")
        # file_contents = file.stream.read().decode("utf-8")
        thread = Process(target = transform_dag)
        thread.start()
        response = '<script>document.location.href = document.referrer</script>'
        #make_response('OK')

    elif work == '2':
        with open("archive_dag.zip","rb") as f_out:
            result = f_out.read()

        response = make_response(result)
        response.headers["Content-Disposition"] = "attachment; filename=result_ns.zip"
        with open('status_dag.sts', 'wt') as f:
            f.write('0')
    if work == '3':
        response = make_response('OK')
    return response

# *************************************************************************
@app.route('/ns')
def form_ns():
    if os.path.exists('status_ns.sts'):
        with open('status_ns.sts', 'rt') as f:
            work = f.read(1)
    else:
        with open('status_ns.sts', 'wt') as f:
            f.write('0')
            work = '0'
    print(work)
    res_get = """
            <html>
                <body>
                    <h1>Забрать отформатированные этикетки</h1>
                    <form action="/transform_ns" method="post" enctype="multipart/form-data">
                        <input type="submit" />
                    </form>
                </body>
            </html>
        """
    res_ok =  """
        <html>
            <body>
                <h1>Преобразование этикеток с кодами маркировки собственного сырья.</h1>
                <form action="/transform_ns" method="post" enctype="multipart/form-data">
                    <input type="file" name="data_file" />
                    <input type="submit" />
                </form>
            </body>
        </html>
    """

    if work == '0':
        res = res_ok
    elif work == '1':
        with open('num_ns.txt') as f:
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

def transform_ns():
    with open('status_ns.sts', 'wt') as f:
        f.write('1')
    with open( 'num_ns.txt', 'wt' ) as f:
        f.write( '0' )

    os.system("rm -f archive_ns.zip")
    os.system("rm -f images_ns/*.png")
    os.system("./make_stickers_ns.py")
    os.system("zip -r archive_ns.zip images_ns/")
    # return text_file_contents.replace("=", ",")
    with open('status_ns.sts', 'wt') as f:
        f.write('2')

@app.route('/transform_ns', methods=["POST"])
def transform_view_ns():
    if os.path.exists('status_ns.sts'):
        with open('status_ns.sts', 'rt') as f:
            work = f.read(1)
    else:
        with open('status_ns.sts', 'wt') as f:
            f.write('0')
            work = '3'
    print(work)
    if work == '0':
        file = request.files['data_file']
        if not file:
            return "No file"
        file.save("flask_tmp_ns.pdf")
        # file_contents = file.stream.read().decode("utf-8")
        thread = Process(target = transform_ns)
        thread.start()
        response = '<script>document.location.href = document.referrer</script>'
        #make_response('OK')

    elif work == '2':
        with open("archive_ns.zip","rb") as f_out:
            result = f_out.read()

        response = make_response(result)
        response.headers["Content-Disposition"] = "attachment; filename=result_ns.zip"
        with open('status_ns.sts', 'wt') as f:
            f.write('0')
    if work == '3':
        response = make_response('OK')
    return response


# ***************************************************************************

@app.route('/ds')
def form_ds():
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
                    <form action="/transform_ds" method="post" enctype="multipart/form-data">
                        <input type="submit" />
                    </form>
                </body>
            </html>
        """
    res_ok =  """
        <html>
            <body>
                <h1>Преобразование этикеток с кодами маркировки давальческого сырья.</h1>
                <form action="/transform_ds" method="post" enctype="multipart/form-data">
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
def transform_ds():
    with open('status.sts', 'wt') as f:
        f.write('1')
    with open( 'num.txt', 'wt' ) as f:
        f.write( '0' )

    os.system("rm -f archive.zip")
    os.system("rm -f images/*.png")
    os.system("./make_stickers_ds.py")
    os.system("zip -r archive.zip images/")
    # return text_file_contents.replace("=", ",")
    with open('status.sts', 'wt') as f:
        f.write('2')

@app.route('/transform_ds', methods=["POST"])
def transform_view_ds():
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
        thread = Process(target = transform_ds)
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
