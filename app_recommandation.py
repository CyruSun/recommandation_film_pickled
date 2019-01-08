# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 10:56:31 2019

@author: Mahery Andrianavonimiarina
"""

import pickle

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('pages/home.html')


@app.route('/recommend')  # décorateur
def about():
    return render_template('pages/recommend.html')


@app.route('/recommend/<int:idtf_dtfrm_entr>', methods=['GET', 'POST'])
def show_recommendation(idtf_dtfrm_entr):
    # unpickling
    with open("./data/dct_idtf_nghbrg", "rb") as f:
        dct_idtf_nghbrg = pickle.load(f)
    return str(dct_idtf_nghbrg[idtf_dtfrm_entr])


@app.errorhandler(404)
def not_found(error):
    return render_template('errors/404.html'), 404


# Fonctionnement pour exécution en ligne de commande
if __name__ == '__main__':
    app.run(debug=True, port=3000)
