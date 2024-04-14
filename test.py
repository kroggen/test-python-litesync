import litesync
import time
print("import worked")

conn = litesync.connect('file:app.db?node=primary&bind=tcp://0.0.0.0:1234')
print("connection opened!")

while not conn.is_ready():
    time.sleep(0.100)
print("the db is ready!")
