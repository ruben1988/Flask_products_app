from flask import Flask, escape, request, url_for, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    name = request.args.get("name", "Page")
    return f'<h1>Home {escape(name)}!</h1>'

@app.route('/about')
def about():
    name = request.args.get("name", "Page")
    return f'<h1>About {escape(name)}!</h1>'

@app.route('/sayhi')
@app.route('/sayhi/<hi>')
def sayhi(hi=''):
    return f'Hi! {hi}'

@app.route('/first_html')
@app.route('/first_html/<name>')
def first_html(name='Ruben'):
   return '''
    <html>
        <body>
        <h1>Hi Flask2</h1>
        <p>Hello %s</p>
        <url>
            <li>Item 1</li>
            <li>Item 2</li>
        </url>
        </body>
    </html>
   '''%name

@app.route('/static_file')
def static_file():
    return "<img src='"+url_for("static",filename="static/img/Flask.png")+"'>"
   #return "<img src='/static/img/Flask.png'>"
   
@app.route('/my_first_template')
@app.route('/my_first_template/<name>')
def my_first_template(name='Ruben'):
   return render_template('view.html', name=name)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
