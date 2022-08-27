from flask import Flask, render_template
from utils import load_candidates_from_json, get_candidate, get_candidates_by_name, get_candidates_by_skill

candidates = 'candidates.json'
data = load_candidates_from_json(candidates)

app = Flask(__name__)


@app.route('/')
def page_main():
    return render_template('list.html', candidates=data)


@app.route('/candidate/<int:x>')
def page_card(x):
    card = get_candidate(x, data)
    return render_template('card.html', user=card)


if __name__ == '__main__':
    app.run()
