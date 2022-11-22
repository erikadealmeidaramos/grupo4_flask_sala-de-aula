from flask import Flask, jsonify, request

app = Flask(__name__)

class Aluno():
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome

class Professor():
    def __init__(self, id, matricula):
        self.id = id
        self.matricula = matricula

database = dict()
database['ALUNO'] = []
database['PROFESSOR'] = []

@app.route('/')
def all():
    return jsonify(database)

@app.route('/alunos')
def alunos():
    return jsonify(database['ALUNO'])

@app.route('/professores')
def professores():
    return jsonify(database['PROFESSOR'])

@app.route('/alunos', methods=['POST'])
def novo_aluno():
    novo_aluno = request.get_json()
    database['ALUNO'].append(novo_aluno)
    return jsonify(database['ALUNO'])

@app.route('/alunos/<int:id_aluno>', methods=['GET'])
def localiza_aluno(id_aluno):
    for aluno in database['ALUNO']:
        if aluno['id'] == id_aluno:
            return jsonify(aluno)
        return '', 404

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)


# curl -X POST http://127.0.0.1:5000/alunos --header "Content-Type: application/json" --data '{"id": 1, "nome": "Erika"}'
# curl -X GET http://127.0.0.1:5000/alunos/1