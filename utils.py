import json


def load_candidates(filename):
    """Загружает данные из файла"""
    with open(filename, 'r', encoding='utf-8') as file:
        return json.loads(file.read())


def get_all(data):
    """Показывает всех кандидатов"""

    candidates_list = []
    for candidate in data:
        candidates_list.append(candidate["name"])
    return candidates_list


def get_by_pk(pk, data):
    """Вернет кандидата по pk"""
    for line in data:
        if line['pk'] == pk:
            return f'Имя кандидата - {line.name }' \
                   f'Позиция - {line.position }' \
                   f'Навыки - { line.skills }'
        else:
            return "No candidate with such pk"


def get_by_skill(skill_name, data):
    """Возвращает кандидатов по навыку"""
    candidates_by_skill = []
    for line in data:
        if skill_name in line['skills'].lower():
            candidates_by_skill.append(line['name'])
            candidates_by_skill.append(line['position'])
            candidates_by_skill.append(line['skills'])

    return v
