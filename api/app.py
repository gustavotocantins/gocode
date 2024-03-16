from flask import Flask, render_template, url_for, request
from PIL import Image
import numpy as np
from pickle import load
from re import match
from glob import glob
from os import chdir
import os
app = Flask(__name__)
app.static_folder = 'static'
@app.route('/')

def index():
    return render_template('index.html')

@app.route('/BetoLanches')
def BetoLanches():
    return render_template('betolanches.html')

@app.route('/BetoLinks')
def BetoLinks():
    return render_template('betolinks.html')

@app.route('/natanjunior')
def natanjunior():
    return render_template('natanjunior/natanjunior.html')

if __name__ == '__main__':
    app.run()