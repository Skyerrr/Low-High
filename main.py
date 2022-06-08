import random
from flask import Flask, render_template, request, redirect, url_for
import datetime

current_year = datetime.datetime.now()
current_year = current_year.strftime("%m/%d/%Y")

def rand_numb():
    global random_numb
    random_numb = random.randint(0, 9)

rand_numb()
print(random_numb)

app = Flask(__name__)
@app.route('/')
def homepage():
    return redirect(url_for('home', current_year=current_year))

@app.route('/home', methods=('GET', 'POST'))
def home():
    if request.method == 'POST':

        guess = request.form["guess"]
        try:
            guess = int(guess)
        except:
            return render_template('error.html', current_year=current_year)
        if guess > random_numb:
            return render_template('high.html', current_year=current_year)
        if guess < random_numb:
            return render_template('low.html', current_year=current_year)
        if guess == random_numb:
            return redirect(url_for('correct', current_year=current_year))

    else:
        return render_template('mainpage.html', current_year=current_year)
        rand_numb()

@app.route('/correct')
def correct():
    rand_numb()
    return render_template('correct.html', current_year=current_year)



if __name__ == "__main__":
    app.run(debug=True)

