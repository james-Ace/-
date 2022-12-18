from .. import app
from flask import request,render_template
from pdf2docx import Converter

@app.route('/cover', methods=['GET','POST'])
def pdf2word():
    if(request.method == "GET"):
        return render_template('cover.html')
    elif (request.method ==   "POST"):
        return 'd'