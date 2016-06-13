from flask import Flask,render_template
from models import User
app = Flask(__name__)

@app.route('/users')
def user_list():
    users=[]
    for i in range(1,11):
        user=User(i,"jikexueyuan"+str(i))
        users.append(user)
    return render_template("user_list.html",users=users)

@app.route('/one')
def one_base():
    return render_template("one_base.html")
@app.route('/two')
def two_base():
    return render_template("two_base.html")
@app.route('/')
def hello_world():
    content="hello nihaoya"
    return render_template("index.html",content=content)

@app.route('/user',methods=['GET'])
def user_index():
    user=User(1,'jikexueyuan')
    return render_template("user_index.html",user=user)
@app.route('/query_user/<user_id>')
def query_user(user_id):
    user=None
    if int(user_id)==1:
        user=User(1,'jiekxueyuan')
    return render_template("user_id.html",user=user)




if __name__ == '__main__':
    app.run()
