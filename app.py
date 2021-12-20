from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


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
    return render_template('assignment8.html',name='raz', last_name='berejik', profile={'hobbies1': 'music',
                                        'hobbies2': 'read books', 'hobbies3': 'take my dog for a walk'})


if __name__ == '__main__':
    app.run(debug=True)
