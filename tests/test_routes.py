from flask import Flask
import json
from ..handlers.routes import configure_routes


  
def test_home():
    app = Flask(__name__, template_folder='../templates')
    configure_routes(app)
    client = app.test_client()
    url = '/'

    response = client.get(url, content_type='html/text')
    
    assert response.status_code == 200
    
 
def test_blog():
    app = Flask(__name__, template_folder='../templates')
    configure_routes(app)
    client = app.test_client()
    url = '/blog'
    response = client.get(url)
    assert response.get_data() == b'blog'
    
def test_blog_content():
    app = Flask(__name__, template_folder='../templates')
    configure_routes(app)
    client = app.test_client()
    url = '/blog'
    response = client.get(url)
    assert response.get_data() != b'blug'
