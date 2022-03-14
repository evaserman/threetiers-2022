# import package flask
from flask import Flask

# ----------------------------------- 
#           YOUR CODE
# ----------------------------------- 

app = Flask(__name__)

@app.route('/')
def hellow_world():
        return 'Hello World!'

if __name__ == '__main__':
    app.run(debug=True, port=3000)

