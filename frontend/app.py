from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    # Replace with the actual URL or Cloud Run endpoint of your backend
    backend_url = 'http://backend-service-url/posts'
    response = requests.get(backend_url)
    posts = response.json() if response.status_code == 200 else []
    return render_template('index.html', posts=posts)

@app.route('/create', methods=['POST'])
def create_post():
    # Replace with the actual URL or Cloud Run endpoint of your backend
    backend_url = 'http://backend-service-url/posts'
    content = request.form.get('content', '')
    requests.post(backend_url, json={'content': content})
    return 'Post created!', 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

