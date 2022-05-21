from audioop import cross
from distutils.log import error
from http.client import OK
from flask import Flask, render_template, request, jsonify
from requests import Response
import threading
from flask_cors import CORS,cross_origin

from tweet_streamer import main

def stream_template(template_name, **context):
    # http://flask.pocoo.org/docs/patterns/streaming/#streaming-from-templates
    app.update_template_context(context)
    t = app.jinja_env.get_template(template_name)
    rv = t.stream(context)
    # uncomment if you don't need immediate reaction
    ##rv.enable_buffering(5)
    return rv

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# Additional code goes here #
@app.route('/')
def home_page():
    return render_template('index.html')


@app.route("/search",methods=['GET', 'POST'])
@cross_origin()
def search():
    if request.method == 'POST':
        global t1
        print("SEARCH")
        rule=request.get_data().decode('utf-8').split('&')[0].replace("keyword=","")
        ReqNo=request.get_data().decode('utf-8').split('&')[1].replace("ReqNo=","")
        print("RULE",rule)
        # rule=request.form["keyword"]
        # if ReqNo!="0":
        #     t1.raise_exception()
        #     t1.join()
        # t1=threading.Thread(target=main(rule))
        # t1.start()
        return rule
        return render_template('index.html',data=rule)

app.run(host="127.0.0.1",port="3000",debug=True)