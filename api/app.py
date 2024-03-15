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

@app.route('/consultar')
def consultar():
    return render_template('consultar.html')

@app.route('/cadastrar/<cotas>/')
def cadastrar(cotas):
    cotas = cotas
    valor = float(cotas)*0.5
    return render_template('cadastrar.html',cotas=cotas,valorreais=valor)

if __name__ == '__main__':
    app.run()