from roku import Roku
import configparise as config
from flask import Flask, render_templet, url_from
import threading as td
import subprosses as sub

app=flask(__name__)


@app.route("/")
   def index():
       return render_tempate(index.html)

@app.route("/internet", methods=['Post'])
  def internet():


@app.route("/offon", methods=['GET','Post'])
   def offon():


@app.route("/adddevices", methods=['GET','Post'])
   def adddevices():





if __name__=='__main__':
    app.run(debug=TRUE)
