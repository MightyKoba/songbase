from flask import Flask, render_template
app = Flask(__name__, template_folder='templates')


@app.route('/')
def idex():
    return render_template('index.html')

@app.route('/form-demo')
def form_demo():
    return render_template('form-demo.html')


@app.route('/user/<string:name>')
def get_user(name):
    return render_template('user.html', user_name=name)

@app.route('/users')
def show_all_users():
    return '<h2> this is the page for all users </h2>'

if __name__ == '__main__':
    app.run()
