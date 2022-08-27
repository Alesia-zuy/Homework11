from flask import Flask, render_template
from utils import load_candidates_from_json, get_candidate, get_candidates_by_name, get_candidates_by_skill

candidates = 'candidates.json'
data = load_candidates_from_json(candidates)

app = Flask(__name__)


@app.route('/')
def page_main():
    """
    Главная страница со всеми кандидатами
    """
    return render_template('list.html', candidates=data)


@app.route('/candidate/<int:x>')
def page_card(x):
    """
    Страница по индексу кандидата
    """
    card = get_candidate(x, data)
    return render_template('card.html', user=card)


@app.route('/search/<candidate_name>')
def page_name(candidate_name):
    """
    Страница поиска по имени
    """
    name_list = get_candidates_by_name(candidate_name, data)
    return render_template('search.html', candidates=name_list, len_=len(name_list))


@app.route('/skill/<skill_name>')
def page_skill(skill_name):
    skill_list = get_candidates_by_skill(skill_name, data)
    return render_template('skill.html', candidates=skill_list, skill=skill_name, len_=len(skill_list))


if __name__ == '__main__':
    app.run()
