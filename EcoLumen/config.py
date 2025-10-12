import os

class Config:
    SECRET_KEY = os.urandom(24)
    DB_HOST = "dpg-d3lfa6ogjchc73cc9j90-a.virginia-postgres.render.com"
    DB_NAME = "hotel_sustentavel_fyw4"
    DB_USER = "root"
    DB_PASSWORD = "yDRGhuENnf7CmBIJdVK0Quvu06iAx7PE"
    DB_PORT = "5432"
