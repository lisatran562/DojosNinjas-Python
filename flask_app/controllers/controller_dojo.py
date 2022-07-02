from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.model_dojo import Dojo
from flask_app.models.model_ninja import Ninja

@app.route('/')
@app.route('/dojos')
def index(): 
    dojo = Dojo.get_all()
    
    return render_template('index.html', dojo=dojo)

@app.route('/dojos/<int:id>')
def dojo_show(id):
    data = {
        'id': id
    }
    dojo = Dojo.get_one(data)
    ninja = Ninja.get_dojo_with_ninjas(data)

    return render_template('show.html', dojo=dojo, ninja=ninja)

@app.route('/dojos/new', methods=['POST'])
def create_dojo():
    Dojo.create_one(request.form)
    return redirect('/')

@app.route('/todo/new')
def todo_new ():
    context = {
        'user': model_user.user.get_one({'id': session['uuid']}),
    }
    return render_template('todo_new.html', **context)) 

