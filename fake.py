from flask import Flask, render_template, url_for, request,jsonify
# from wtforms import Form, FloatField, validators
app = Flask(__name__)

# done

@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/pricing")
def pricing():
    return render_template('pricing.html', title='About')

# class InputForm(Form):
#     q = FloatField(validators=[validators.InputRequired()])
#     r = FloatField(validators=[validators.InputRequired()])
@app.route("/", methods=['GET', 'POST'])
@app.route("/login")

def login():
    return render_template('regLog.html')
    # form = InputForm(request.form)
    #
    # if request.method == 'POST' and form.validate():
    #     print(request.form['firstname'])
    #     return'<h1> I worked </h1>'
    # else:

# print('numbers are:', numbers[ num[0] for num in numbers ])
@app.route("/forgot_pass")
def fogot_pass():
    return render_template('forgot_password.html')

@app.route("/")

@app.route("/loginProcessing",methods=[ 'POST'])
def loginProcessing():
    if request.method == 'POST':
        if request.form['login_form'] == 'Log in':

            username = request.form['username1']
            password = request.form['password1']
            print('i worked ')

            output = 'The username is: ' + str(username) + 'the password is: ' + str(password )
            #    do some processnig with the login information
            #    check to see if they are in the database

            # return jsonify({'output': 'Full Name: ' + output})
            return render_template('loggedin_home.html')

        if request.form['login_form'] == 'Sign-Up':
            firstName = request.form['firstname']
            lastName =  request.form['lastname']
            email = request.form['email']
            password = request.form['confirm_password']
            output = 'name: ' + firstName + lastName,'emiail: ' + email , ' password: ' + password

            # input processing here sot that a new user will be added to the database

            return jsonify({'output':  output})





    # return " <h1> im working i swear</h1>"
    # return '<h1>' + output + ':' +  'Full Name:' + output + '</h1>'






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