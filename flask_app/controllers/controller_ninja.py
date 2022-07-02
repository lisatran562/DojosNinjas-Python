from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.model_dojo import Dojo
from flask_app.models.model_ninja import Ninja

@app.route('/ninja/new')
def new_ninja():
    dojo = Dojo.get_all()
    return render_template('ninja_new.html', dojo=dojo)

@app.route('/ninja/add', methods=['POST'])
def add_ninja():
    Ninja.create_one(request.form)

    return redirect('/')