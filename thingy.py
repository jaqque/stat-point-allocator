from flask import Flask
from flask import render_template_string, render_template, request, redirect
import copy

app = Flask(__name__)

# stolen from https://note.nkmk.me/en/python-check-int-float/
def is_integer(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()

## GLOBALS!! we like globals.
level=1
name=""
points_spent=0
saved_abilities = {
    "STR": [0,"Strength"],
    "END": [0,"Endurance"],
    "AGI": [0,"Agility"],
    "INT": [0,"Intelligence"],
    "CHA": [0,"Charisma"],
    "LCK": [0,"Luck"],
}
abilities=copy.deepcopy(saved_abilities)
bonus_points=0
skills = {
    "passive": ["","Passive"],
    "active": ["","Active"],
}

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/new', methods=['POST', 'GET'])
def generation():
    global level
    global name
    # dictionaries:
    global abilities
    global saved_abilities

    if request.method == 'POST':
        valid=True
        for ability in abilities:
            if is_integer(request.form[ability]):
                valid=int(float(request.form[ability])) > 0 and valid
            else:
                valid=False

        if valid:
            name=request.form['name']
            for ability in abilities:
                abilities[ability][0]=int(float(request.form[ability]))
            saved_abilities=copy.deepcopy(abilities)
            return redirect("/try")

    page=render_template("new-character.html.j2",title="Genesis", abilities=abilities, skills=skills, uri=request.base_url, level=level, name=name)
    return page

@app.route('/try', methods=['POST', 'GET'])
def tired():
    global level
    global name
    global points_spent
    # being explicit about the dictionaries
    # python is weird. i don't understand it.
    # what say we ditch this and use Julia?
    global abilities
    global saved_abilities

    points = int((level*level + level )/2 + level - 2)
    points_remaining = (points - points_spent)

    if request.method == 'POST':
        if request.form['submit']=='name':
            name=request.form['name']
        if request.form['submit']=='levelup':
            level+=1
            points = int((level*level + level )/2 + level - 2)
        for ability in abilities:
            if request.form['submit']==f"{ability}up":
                cost= int(abilities[ability][0] / 10 + 1)
                if points_remaining >= cost:
                    abilities[ability][0]+=1
                    points_spent += cost
            if request.form['submit']==f"{ability}down":
                if abilities[ability][0] > saved_abilities[ability][0]:
                    abilities[ability][0]-=1
                    cost= int(abilities[ability][0] / 10 + 1)
                    points_spent -= cost

    # re-calculate points_remaining after above adjustments
    points_remaining = (points - points_spent)

    page=render_template("stat-template.html.j2",title="GET TO THE SPA-TER!!!", abilities=abilities, skills=skills, uri=request.base_url, level=level, name=name, points_remaining=points_remaining)
    return page

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
