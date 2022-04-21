from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.dojo import Dojo

# index route
# done
@app.route('/')
def index():
    return redirect('/dojos')

# create user route
# done
@app.route('/create_dojo', methods=['POST'])
def create_dojo():
    # sends form data to model for insertion in db
    Dojo.save_dojo(request.form)
    return redirect('/dojos')

# displays dojos
@app.route('/dojos')
def dojos():
    # renders dojos template passing information for all dojos
    return render_template('dojos.html', all_dojos = Dojo.get_all_dojos())

# displays one dojo
@app.route('/dojos/<int:id>')
def one_dojo(id):
    id_data = {
        'id' : id
    }
    return render_template('show_dojo.html', dojo = Dojo.get_one_dojo_with_ninjas(id_data))
