from random import choice

from flask import Flask, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

# route to handle the landing page of a website.
@app.route('/')
def start_here():
    return """
    <!DOCTYPE html>
    <html>
        <head>
            <title>Hi There!</title>
        </head>
        <body>
            <a href="/hello">Hi!</a> 
            This is the home page.
        </body>
    </html>

    """

# route to display a simple web page
@app.route('/hello')
def say_hello():
    return """
    <!DOCTYPE html>
    <html>
        <head>
            <title>Hi There!</title>
        </head>
        <body>
            <h1>Hi There!</h1>
            <form action="/greet">
                <label>What's your name? <input type="text" name="person"></label>
                <div>
                    <label>Select your compliment:
                        <select name="compliment">
                            <option value="awesome">awesome</option>
                            <option value="terrific">terrific</option>
                            <option value="fantastic">fantastic</option>
                            <option value="neato">neato</option>
                            <option value="fantabulous">fantabulous</option>
                            <option value="wowza">wowza</option>
                            <option value="oh-so-not-meh">oh-so-not-meh</option>
                            <option value="brilliant">brilliant</option>
                            <option value="ducky">ducky</option>
                            <option value="coolio">coolio</option>
                            <option value="incredible">incredible</option>
                            <option value="wonderful">wonderful</option>
                            <option value="smashing">smashing</option>
                            <option value="lovely">lovely</option>
                        </select>
                    </label>
                </div>
                <input type="submit">
            </form>
        </body>
    </html>

    """

@app.route('/greet')
def greet_person():
    player = request.args.get("person")

    compliment = request.args.get("compliment")

    return """
    <!DOCTYPE html>
    <html>
        <head>
            <title>A Compliment</title>
        </head>
        <body>
            Hi, %s, I think you're %s!
        </body>
    </html>""" % (player, compliment)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
