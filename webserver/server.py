

from quart import Quart



app = Quart(__name__)
from .views import *

def run_server(**kwargs):
    app.run(**kwargs)