from flask import Flask, request, render_template,jsonify
from Array import bubble_sort




app = Flask(__name__, static_url_path='/static')

@app.route('/coucou')
def coucou():
    return 'coucou'

@app.route('/test/result')
def show_array():
    # façon = request.args.get()
    array = [int(x) for x in request.args.get('list').split(',')]
    print(type(array), array)
    return jsonify(

        bubble_sort(array)
        
        
        )

@app.route('/test/')
def liste():
        return render_template('site.html')
@app.route('/index')
def index():
     return render_template('index.html')

    