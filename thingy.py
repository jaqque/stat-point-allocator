from flask import Flask
from flask import render_template_string

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
    body="<h1> STUFFY STUFF </h1><p>i am a {{ banana | default(pizza) }}</p>"
    current_abilities='''
    {% for key,value in abilities.items() %}{{ value[1] }}={{ value[0] }}</br>{% endfor %}
    '''

    banana="apache attack helicopter"
    page=render_template_string(header+ body + current_abilities + footer, title="Spa Treatment", abilities=abilities)
    return page
