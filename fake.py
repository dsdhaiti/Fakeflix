from flask import Flask, render_template, url_for, request
# from wtforms import Form, FloatField, validators
app = Flask(__name__)

# done

@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/about")
def about():
    return render_template('about.html', title='About')

# class InputForm(Form):
#     q = FloatField(validators=[validators.InputRequired()])
#     r = FloatField(validators=[validators.InputRequired()])
@app.route("/", methods=['GET', 'POST'])
@app.route("/login")

def login():

    # form = InputForm(request.form)
    #
    # if request.method == 'POST' and form.validate():
    #     print(request.form['firstname'])
    #     return'<h1> I worked </h1>'
    # else:
    return render_template('regLog.html')
# print('numbers are:', numbers[ num[0] for num in numbers ])

# def loginProcessing():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']







@app.route("/register")
def register():
    return "<h1> Im at the Registeration page</h1>"
        # render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)

################################################
# List of to do
################################################
# todo[Done]: finish home home pages
# todo[Done]: Generate login page
# todo[]: create a forgot password process
# todo[]: generate registration page
# todo[]: Generate an about us page
# todo[]: Generate already logged in page
# todo[]: generate Admin page
# todo[]: create personal user page users
# todo[]: Generate movie title page
# todo[]: Generate movie search page
# todo[]: generate Checkout page