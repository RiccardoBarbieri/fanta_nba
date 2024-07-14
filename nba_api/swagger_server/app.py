#!/usr/bin/env python3

import connexion

from swagger_server import encoder


def app():
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'Basketball Match-Up and Team Information API'}, pythonic_params=True)
    return app

if __name__ == '__main__':
    app().run(port=8124)

