#!/usr/bin/env python
# encoding: utf-8

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return "hello, topaz-bi" 
