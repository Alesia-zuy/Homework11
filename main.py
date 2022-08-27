from flask import Flask, render_template
from utils import load_candidates_from_json, get_candidate, get_candidates_by_name, get_candidates_by_skill

candidates = 'candidates.json'
data = load_candidates_from_json(candidates)

app = Flask(__name__)


@app.route('/')
def page_main():
    pass
