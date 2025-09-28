from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
def api_root():
    return 'Hello sdfvsdv'

@app.route('/articles')
def api_articles():
    return 'List of' + url_for('api_articles')

@app.route('/articles/<article_id>')
def api_article(article_id):
    return 'You are currently reading' + article_id

if __name__ == '__main__':
    app.run()