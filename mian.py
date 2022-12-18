<<<<<<< HEAD
from route import app
import route.controller.cover



if __name__ == '__main__':
=======
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
   return render_template('index.html')

if __name__ == '__main__':
>>>>>>> 0484aa6df5ee7520e2f8f38f082674ca36078b33
   app.run(debug=True)