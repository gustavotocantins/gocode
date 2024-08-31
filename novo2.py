from flask import Flask, jsonify, request
import firebase_admin
from firebase_admin import credentials, firestore
import os
import json

app = Flask(__name__)

# Carregando as credenciais do Firebase
with open('/home/gustavo/Downloads/fpi-app-ca719-firebase-adminsdk-smxbt-075b5e54b1.json') as f:
    firebase_credentials = json.load(f)

# Passando o dicionário diretamente para a função Certificate
cred_obj = credentials.Certificate(firebase_credentials)
default_app = firebase_admin.initialize_app(cred_obj, {
    'databaseURL':'https://fpi-app-ca719-default-rtdb.firebaseio.com/'
})

# Inicializando o Firestore
db = firestore.client()

def adicionar_professor(professor_id, nome, email, telefone, escola):
    professor_ref = db.collection('professores').document(professor_id)
    professor_ref.set({
        'nome': nome,
        'email': email,
        'telefone': telefone,
        'escola': escola
    })

def adicionar_aluno(professor_id, aluno_id, nome, idade, turma):
    aluno_ref = db.collection('professores').document(professor_id).collection('alunos').document(aluno_id)
    aluno_ref.set({
        'nome': nome,
        'idade': idade,
        'turma': turma
    })

def adicionar_atividade(professor_id, aluno_id, atividade_id, titulo, data, nota):
    atividade_ref = db.collection('professores').document(professor_id).collection('alunos').document(aluno_id).collection('atividades').document(atividade_id)
    atividade_ref.set({
        'titulo': titulo,
        'data': data,
        'nota': nota
    })

def verificar_email_professor(email):
    professores = db.collection('professores').where('email', '==', email).stream()
    for professor in professores:
        return True
    return False

def obter_alunos_por_professor(email):
    professores = db.collection('professores').where('email', '==', email).stream()
    for professor in professores:
        professor_id = professor.id
        alunos = db.collection('professores').document(professor_id).collection('alunos').stream()
        alunos_info = []
        for aluno in alunos:
            alunos_info.append(aluno.to_dict())
        return alunos_info
    return None

# Exemplo de uso
adicionar_professor('prof1', 'João Silva', 'joao@example.com', '123456789', 'Escola XYZ')
adicionar_aluno('prof1', 'aluno1', 'Maria Souza', 14, '8A')
adicionar_atividade('prof1', 'aluno1', 'atividade1', 'Matemática - Prova 1', '2024-08-30', 8.5)

# Verificar se o email já está cadastrado
print(verificar_email_professor('joao@example.com'))  # True

# Obter informações dos alunos de um professor pelo email
alunos_info = obter_alunos_por_professor('joao@example.com')
print(alunos_info)