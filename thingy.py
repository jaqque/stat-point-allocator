from flask import Flask
from flask import render_template_string, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/try')
def tired():
    name="Fred"
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
        "active": ["","Active Skills"],
        "passive": ["","Passive Skills"],
    }

    header='''
    <html><head><title>{{ title }}</title></head><body>
    '''.strip()
    footer='''
    </body></html>
    '''.strip()
    body="<h1>STUFFY STUFF</h1><p>i am a {{ banana | default(pizza) }}</p>"
    current_abilities='''
    {% for key,value in abilities.items() %}{{ value[1] }}({{ key }})={{ value[0] }}</br>{% endfor %}
    '''.strip()

    banana="apache attack helicopter"
    page=render_template_string(header+ body + current_abilities + footer, title="Spa Treatment", abilities=abilities, pizza="banana")
    page=render_template("stat-template.html.j2")
    return page

