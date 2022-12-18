from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__, template_folder="../templates")
bootstrap = Bootstrap(app)
