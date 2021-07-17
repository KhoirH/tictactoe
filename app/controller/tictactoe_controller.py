from flask import Blueprint, render_template

viewpage = Blueprint('', __name__)

@viewpage.route('/')
def tictactoe_view():
  return render_template('index.html')

@viewpage.route('/menu')
def tictactoe_menu():
  return render_template('menu.html')