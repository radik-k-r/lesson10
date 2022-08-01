import json


def load_candidates(filename):
    """Загружает данные из файла"""
    with open(filename, 'r', encoding='utf-8') as file:
        return json.loads(file.read())


# Правильно ли хранить переменные в utils. Или они должны быть main?
# Файл с информацией о кандидатах
filename = "candidates.json"

# вся информация о кандидатах
data = load_candidates(filename)


def get_all():
    """Показывает всех кандидатов"""
    candidates_list = ''
    for person in data:
        candidates_list += (
            f'<pre>\n'
            f'Имя кандидата - {person["name"]}\n'
            f'Позиция - {person["position"]}\n'
            f'Навыки - {person["skills"]}\n'
            f'</pre>'
        )
    return candidates_list


def get_by_pk(pk):
    """Вернет кандидата по pk"""
    for person in data:
        if (person['pk']) == pk:
            return (
                f'<pre>\n'
                f'Имя кандидата - {person["name"]}\n'
                f'Позиция - {person["position"]}\n'
                f'Навыки - {person["skills"]}\n'
                f'</pre>'
            )
    else:
        return f'<pre> No candidate with such pk </pre>'


def get_by_skill(skill):
    """Возвращает кандидатов по навыку"""
    candidates_by_skill = ""
    for person in data:
        if skill in person['skills'].lower():
            candidates_by_skill += (
                f'<pre>\n'
                f'Имя кандидата - {person["name"]}\n'
                f'Позиция - {person["position"]}\n'
                f'Навыки - {person["skills"]}\n'
                f'</pre>'
            )
    if candidates_by_skill:
        return candidates_by_skill
    else:
        return f'<pre>Jet no skilled staff</pre>'

