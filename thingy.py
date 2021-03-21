from flask import Flask
from flask import render_template_string, render_template, request

app = Flask(__name__)


name="William Frederickson, Esq."
level=0
abilities = {
    "STR": [0,"Strength"],
    "END": [0,"Endurance"],
    "AGI": [0,"Agility"],
    "INT": [0,"Intelligence"],
    "CHA": [0,"Charisma"],
    "LCK": [0,"Luck"],
}
bonus_points=0
skills = {
    "passive": ["","Passive"],
    "active": ["","Active"],
}


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/try', methods=['POST', 'GET'])
def tired():
    global level

    if request.method == 'POST':
        level+=1

    page=render_template("stat-template.html.j2",title="GET TO THE SPA-TER!!!", abilities=abilities, skills=skills, uri=request.base_url, level=level, name=name)
    return page

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
