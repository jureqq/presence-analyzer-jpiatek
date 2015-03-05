# -*- coding: utf-8 -*-
"""
Presence analyzer web app.
"""
import os.path
import logging.config

from presence_analyzer.main import app
from presence_analyzer import views

if __name__ == "__main__":
    INI_FILENAME = os.path.join(os.path.dirname(__file__),
                                '..', 'runtime', 'debug.ini')
    logging.config.fileConfig(INI_FILENAME, disable_existing_loggers=False)
    app.run(host='0.0.0.0')
