from flask import Flask, redirect, url_for, render_template, request, session, Blueprint
from interact_db import interact_db, query_to_json
import requests
import json

app = Flask(__name__)

users = {'user1': {'name': 'Raz', 'email': 'Raz@gmail.com'},
         'user2': {'name': 'Wessly', 'email': 'Wessly@gmail.com'},
         'user3': {'name': 'Tomi', 'email': 'Tomi@hotmail.com'},
         'user4': {'name': 'Mor', 'email': 'Mor@gyahoo.com'},
         'user5': {'name': 'Sigal', 'email': 'Sigal@walla.com'}
         }


@app.route('/home')
@app.route('/')
def main():
    print('first redirect')
    return render_template('homePage.html')


# @app.route('/home')
# def home_func():
#     print('the usage url for')
#     return redirect(url_for('raz_func'))


@app.route('/cvWes')
def cv_func():
    print("instruction for the assignment is in thw pdf file ")
    return render_template('CV.html')

@app.route('/cv2')
def form_Cv2():
    return render_template('CV2.html')

@app.route('/assignment8')
def assignment_8():
    return render_template('assignment8.html',name='', last_name='', profile={'hobbies1': 'music',
                                        'hobbies2': 'read books', 'hobbies3': 'take my dog for a walk'})


@app.route("/assignment9", methods=['GET', 'POST'])
def assignment9_page():
    # search form
    if 'email' in request.args:
        email = request.args['email']
        if email == '':
            return render_template('assignment9.html', user_list=users)
        # search it in users dict
        for key, value in users.items():
            if value.get('email') == email:
                return render_template('assignment9.html', u_name=value.get('name'), u_email=value.get('email'))
    # registration form
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        session['username'] = username
    return render_template('assignment9.html')

@app.route ("/logout", methods=['GET', 'POST'])
def logout_func():
    session['username'] = ''
    return render_template('assignment9.html')

from pages.assignment10.assignment10 import assignment10
app.register_blueprint(assignment10)

#  assignment 11
#  2+3
@app.route("/assignment11/users")
def assignment11_page():
    query = "select * from users"
    query_result = query_to_json(query=query)
    return json.dumps(query_result)

#  4+5
@app.route("/assignment11/outer_source", methods=['GET'])
def assignment11_outer_source_page():
    if 'number' in request.args:
        number = request.args['number']
        res = requests.get(url=f"https://reqres.in/api/users/{number}")
        res = res.json()
        return render_template('assignment11.html', user=res['data'])
    return render_template('assignment11.html')

if __name__ == '__main__':
    app.secret_key = '123'
    app.run(debug=True)
