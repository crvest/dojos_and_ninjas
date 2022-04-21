from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

# displays add ninja page
# done
@app.route('/ninjas')
def ninjas():
    return render_template('ninjas.html', all_dojos = Dojo.get_all_dojos())

@app.route('/create_ninja', methods=['POST'])
def create_ninja():
    Ninja.save_ninja(request.form)
    id = request.form['dojo_id']
    return redirect(f"/dojos/{ id }")