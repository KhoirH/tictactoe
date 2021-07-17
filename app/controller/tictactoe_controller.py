from flask import Blueprint, render_template, request

viewpage = Blueprint('', __name__)

@viewpage.route('/')
def tictactoe_view():
  data = request.args.get('is')
  return render_template('index.html', data = data)

@viewpage.route('/menu')
def tictactoe_menu():
  return render_template('menu.html')