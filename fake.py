from flask import Flask, render_template, url_for, request,jsonify
import random
import requests
import json
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

@app.route("/register")
def register():
    return "<h1> Im at the Registeration page</h1>"
        # render_template('about.html', title='About')

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

            # generate orginal moveis on the first page

            # random movies
            letters = ['the Dark Knight',
                       'Inception',
                       'Interstellar',
                       'The Intouchables',
                       'La La Land',
                       'Inglourious Basterds',
                       'The Hunt',
                       'Broke back mountian',
                       'The notebook'
                       'Twilight'
                       'Up']

            # choose a random movie
            letter_random = random.choice(letters)


            key = 'e2a46779'

            api_url = 'http://www.omdbapi.com/?s=' + letter_random + '&apikey=' + key

            response = requests.get(api_url)

            movies = json.loads(response.content)
            print(movies)
            return render_template('loggedin_home.html', movies = movies)

        if request.form['login_form'] == 'Sign-Up':
            firstName = request.form['firstname']
            lastName =  request.form['lastname']
            email = request.form['email']
            password = request.form['confirm_password']
            output = 'name: ' + firstName + lastName,'emiail: ' + email , ' password: ' + password

            # input processing here sot that a new user will be added to the database

            return jsonify({'output':  output})

@app.route("/SearchedMovies",methods=[ 'POST'])
def searchedMovie():
#     get the information from the form
#   put the information together to make an api call
#   test to see that the informtation was goood
#   send back the loggin page

    if requests == 'Post':
        if requests.form[''] ==


#app.route("/movieChoice",methods=[ 'POST'])
# def movieChoice():
# #     take in the movie name
# #       make the api call



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