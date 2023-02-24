from flask import Flask
from config.config import *
from router.user_router import *
from flasgger import Swagger
app = Flask(__name__)
init(app)

swagger = Swagger(app, template={
    "swagger": "2.0",
    "info": {
        "title": "Curd Operation Api",
        "version": "1.0.0",
        "description": "Develope By Zaryab Khan"
    },
    "basePath": "/",
    "schemes": [
        "http",
        "https"
    ],
    "securityDefinitions": {},
    "security": [],
    "definitions": {},
    "externalDocs": {},
    "template": {
        "footer": "Powered by Zaryab",
        'navbar_color': 'black',
        'navbar_brand_image': '',
        'docExpansion': 'full',
        'hideTopbar': False,
        'hideModels': True
    }
    
})
app.register_blueprint(user_router)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
