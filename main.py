from app.database import instance as database
from app.server import instance as server

database.initialize_db()
app = server.initialize()
print("Gateway " + app.version + " started")
