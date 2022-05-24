#this script will run our application
from dbdemo import app

if (__name__ == "__main__"):
    app.run(debug = True, host = "localhost", port = 5000)
