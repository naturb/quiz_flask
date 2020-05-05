# -*- coding: utf-8 -*-

from flask import Flask
from flask import render_template, request, redirect, url_for, flash

app = Flask(__name__)

app.config.update(dict(
    SECRET_KEY='secret',
))

PYTANIA = [
    {
        'pytanie': u'Stolica Polski to:',
        'odpowiedzi': [u'Kraków', u'Warszawa', u'Gniezno'],
        'odpok': u'Warszawa',
    },
    {
        'pytanie': u'Wynik dzielenia to:',
        'odpowiedzi': [u'iloraz', u'iloczyn', u'suma'],
        'odpok': u'iloraz',
    },
    {
        'pytanie': u'Wynik działania 2*2+2 to:',
        'odpowiedzi': [u'4', u'8', u'6'],
        'odpok': u'6',
    }
]


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        punkty = 0
        odpowiedzi = request.form 
        for pnr, odp_u in odpowiedzi.items():
            if odp_u == PYTANIA[int(pnr)]['odpok']:
                punkty += 1
        flash(u'Liczba poprawnych odpowiedzi, to: {0}'.format(punkty))
        return redirect(url_for('index'))

    return render_template('index.html', pytania=PYTANIA)

if __name__ == '__main__':
    app.run(debug=True)
