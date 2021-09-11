from flask import Flask, jsonify ,request
app = Flask(__name__)

@app.route("/")
def api_home():
    return "A simple rest API"

@app.route("/prime/<int:n>")
def prime(n):
    ip = request.remote_addr
    flag = False
    if n > 1:
        for i in range(2, n):
            if (n % i) == 0:
                flag = True
                break
    if flag:
        result = {"Number":n,
        "Prime": False,
        "IP_Address":ip
        }
    else:
        result = {"Number":n,
        "Prime": True,
        "IP_Adress":ip
        }
    return result



if __name__=="__main__":
    app.run(debug=True)