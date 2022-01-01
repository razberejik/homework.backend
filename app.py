from flask import Flask, redirect, url_for, render_template, request, session, Blueprint
from interact_db import interact_db

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

change_message = ""

assignment10 = Blueprint('assignment10', __name__, static_folder='static', static_url_path='/', template_folder='templates')

@app.route("/assignment10", methods=['GET', 'POST'])
def assignment10_page():
    global message_has_been_changed
    message_has_been_changed = ""
    return render_template('assignment10.html')


app.register_blueprint(assignment10)

# insert user
@app.route('/insert_user', methods=['POST'])
def insert_user_func():
    name = request.form['name']
    email = request.form['email']
    query = "INSERT INTO users(name, email) VALUES ('%s', '%s')" % (name, email)
    interact_db(query=query, query_type='commit')
    global message_has_been_changed
    message_has_been_changed = "The user "+name+" is inserted"
    return redirect('/user_list')

# update user
@app.route('/update_user', methods=['POST'])
def update_user_func():
    name = request.form['name']
    new_email = request.form['new_email']
    query = "update users set email = '%s' where name = '%s'" % (new_email, name)
    interact_db(query=query, query_type='commit')
    global message_has_been_changed
    message_has_been_changed = "The email of the user "+name+" is updated"
    return redirect('/user_list')

# delete user
@app.route('/delete_user', methods=['POST'])
def delete_user_func():
    name = request.form['name']
    query = "DELETE FROM users WHERE name='%s'" % name
    interact_db(query, query_type='commit')
    global message_has_been_changed
    message_has_been_changed = "The user "+name+" was deleted"
    return redirect('/user_list')

# display user
@app.route('/user_list')
def user_list_func():
    query = "select * from users"
    query_result = interact_db(query=query, query_type='fetch')
    return render_template('assignment10.html', user_list=query_result, message_has_been_changed=message_has_been_changed)


if __name__ == '__main__':
    app.secret_key = '123'
    app.run(debug=True)
