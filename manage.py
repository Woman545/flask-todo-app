# -*- coding: utf-8 -*-
import os
from application import create_app

app = create_app(os.environ.get('APP_CONFIG', 'default'))

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=7345)
