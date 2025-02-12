from flask import Flask
app=Flask(__name__)


@app.route('/hello',methods=['GET','POST'])
def hello_world():
    return "Hello world!"

if __name__=='__main__':
    app.run()