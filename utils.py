import json
candidates = 'candidates.json'


def load_candidates_from_json(path):
    """
    Возвращает список всех кандидатов
    """
    with open(path, encoding='utf-8') as file:
        data_candidates = json.load(file)
        return data_candidates


def get_candidate(candidate_id, list_):
    """
    Возвращает одного кандидата по его id
    """
    for item in list_:
        if item["id"] == candidate_id:
            return item


def get_candidates_by_name(candidate_name, list_):
    """
    Возвращает кандидатов по имени
    """
    for item in list_:
        if candidate_name.lower() in item["name"].lower():
            return item


def get_candidates_by_skill(skill_name, list_):
    """
    Возвращает кандидатов по навыку
    """
    result = []
    for item in list_:
        skills = (item["skills"]).lower().split(', ')
        if skill_name.lower() in skills:
            result.append(item)
    return result
