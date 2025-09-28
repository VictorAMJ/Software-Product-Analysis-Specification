import os

class Config:
    SECRET_KEY = os.urandom(24)
    DB_HOST = "dpg-d30rmj7diees7389bb50-a.virginia-postgres.render.com"
    DB_NAME = "hotel_sustentavel"
    DB_USER = "root"
    DB_PASSWORD = "7SaJncuFQpFZvsL7bO8v3dS3zJc2accC"
    DB_PORT = "5432"
