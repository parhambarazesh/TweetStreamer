import time
from flask import Flask, render_template, request
import threading
from flask_cors import CORS,cross_origin
from waitress import serve

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

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route("/search",methods=['GET', 'POST'])
@cross_origin()
def search():
    if request.method == 'POST':      
        rule=request.get_data().decode('utf-8').split("&")[0].replace("keyword=","")

        # while 1:
        #     print(2)
        #     time.sleep(1)
        t1=threading.Thread(target=main(rule))
        t1.start()

        return rule

if __name__ == '__main__':
    serve(app, host="0.0.0.0", port=3000)
# app.run(port="3000",debug=True)