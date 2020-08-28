
# TODO: Follow the assignment instructions to complete the required routes!
# (And make sure to delete this TODO message when you're done!)
from flask import Flask

app = Flask(__name__)

@app.route('/')
def homepage():
    """Shows a greeting to the user."""
    return 'Are you there, world? It\'s me, Ducky!'

@app.route('/penguins')
def favoriteAnimal():
    'show user my favorite animal'
    return 'Penguins are cute!'

@app.route('/animal/<users_animal>')
def favorite_animal(users_animal):
    """Display a message to the user that changes based on their favorite animal."""
    return f'Wow, {users_animal} is my favorite animal, too!'


@app.route('/dessert/<users_dessert>')
def favorite_dessert(users_dessert):
    """show users favorite dessert"""
    return f'How did you know I {users_dessert}?'

@app.route('/madlibs/<adjective>/<noun>')
def madlib(adjective,noun):
    """mad lib"""
    return f'roses are {adjective}, violets are are blue and you are {noun}'

@app.route('/multiply/<number1>/<number2>')
def multiply(number1,number2):
    """multiply page
    this page takes two arguments then multiplys and displays the result 
    """
    if number1.isdigit() == False or number2.isdigit() == False:
       return 'Invalid inputs. Please try again by entering 2 numbers!'
    elif number1.isdigit() and number2.isdigit():
        number1 = int(number1)
        number2 = int(number2)
        sum = number1 * number2
        return f'{number1} times {number2} equals {sum}'


if __name__ == '__main__':
    app.run(debug=True)
