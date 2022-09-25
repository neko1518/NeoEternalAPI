from flask import *
import os
import aminofix
import heroku3
os.system('set FLASK_ENV=development')
app = Flask(__name__)

def restart(key, name):
    heroku_conn = heroku3.from_key(key)
    botapp = heroku_conn.apps()[name]
    botapp.restart()

@app.route('/api/login',  methods = ['POST'])
def get_timezone():
    try:
        data = request.form
        login = data.get("email")
        password = data.get("password")
        device = data.get("device")
        key = "a5451957-d9ee-4114-92e1-66cf55ee9957"
        name = "dhdhdj-a"
        client = aminofix.Client(device)
        client.login(email = login, password = password)
        return f"{client.sid}"
    except:
        try:
            restart(key, name)
            return abort(404)
        except:
            return abort(404)



if __name__ == '__main__':
  app.run("0.0.0.0", 5000)
