from flask import Flask
from utils import load_candidates, get_all, get_by_pk, get_by_skill, data

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return get_all()


@app.route('/candidates/<int:pk>')
def candidate(pk):
    return get_by_pk(pk)


@app.route('/skills/<skill>')
def skills_info(skill):
    return get_by_skill(skill.lower())


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5001)
