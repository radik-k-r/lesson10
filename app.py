from flask import Flask, render_template

from utils import load_candidates, get_all, get_by_pk, get_by_skill

app = Flask(__name__)

# файл с информацией о кандидатах
filename = "candidates.json"

# вся информация о кандидатах
data = load_candidates(filename)


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', data=data)


@app.route('/candidates/<int:pk>')
def candidates(pk):
    return render_template('candidate.html', data=data, pk=pk)


@app.route('/skills/<skill>')
def skills_info(skill):
    return render_template('skills.html', data2=get_by_skill(skill, data))


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5001)
