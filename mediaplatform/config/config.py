
import os
from urllib.parse import quote_plus

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL') or \
        'postgresql://postgres:%s@localhost:5432/mydatabase' % quote_plus("Rajat@123")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
