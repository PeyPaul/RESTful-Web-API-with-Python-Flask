from flask import Flask, url_for, request

app = Flask(__name__)

@app.route('/')
def api_root():
    return 'Hello'

@app.route('/articles')
def api_articles():
    return 'List of' + url_for('api_articles')

@app.route('/articles/<article_id>')
def api_article(article_id):
    return 'You are currently reading' + article_id

@app.route('/hello')
def api_hello():
    if 'name' in request.args:
        return 'Hello ' + request.args['name']
    else:
        return 'Hello unknown traveler'

if __name__ == '__main__':
    app.run()