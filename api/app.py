from flask import Flask, jsonify, request
app = Flask(__name__)
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import os
import json

@app.route("/", methods=["POST"])
def imprimir():
  response = {"status": 200}
  return jsonify(response)

@app.route('/instituicao')
def print_data():
    try:
        firebase_admin.delete_app(firebase_admin.get_app())
    except:
        pass
    
    firebase_credentials = os.getenv('CREDENCIAL')
    cred_dict = json.loads(firebase_credentials)
    cred_obj = firebase_admin.credentials.Certificate(cred_dict)
    default_app = firebase_admin.initialize_app(cred_obj, {
        'databaseURL':'https://fpi-app-ca719-default-rtdb.firebaseio.com/'
        })
    ref = db.reference()
    
    usuarios_ref = ref.child('instituicoes')
    nomeInstituicoes = []
    for user_key, user_data in usuarios_ref.get().items():
        nome = user_data.get('nome')
        nomeInstituicoes.append(nome)
    
    text=""
    for nomesResposta in nomeInstituicoes:
        text += nomesResposta+";"
    return text

@app.route('/CadastrarLogin', methods=['POST'])
def CadastrarLogin():
    def VerificarEmailExistente(email):
          cursor = ref.child('usuarios')
          for key, checkemail in cursor.get().items():
              if (checkemail.get('email') == email):
                  return True
          return False
    data = request.get_json()
    
    try:
        firebase_admin.delete_app(firebase_admin.get_app())
    except:
        pass
    
    firebase_credentials = os.getenv('CREDENCIAL')
    cred_dict = json.loads(firebase_credentials)
    cred_obj = firebase_admin.credentials.Certificate(cred_dict)
    default_app = firebase_admin.initialize_app(cred_obj, {
        'databaseURL':'https://fpi-app-ca719-default-rtdb.firebaseio.com/'
        })
    ref = db.reference()
    
    usuarios_ref = ref.child('usuarios')

    if VerificarEmailExistente(data['email']):
        return "E-mail existente"
    else:
        usuarios_ref.push(data)
        return "Cadastrado"

@app.route('/Login', methods=['POST'])
def Login():
    data = request.get_json()
    try:
        firebase_admin.delete_app(firebase_admin.get_app())
    except:
        pass
    firebase_credentials = os.getenv('CREDENCIAL')
    cred_dict = json.loads(firebase_credentials)
    cred_obj = firebase_admin.credentials.Certificate(cred_dict)
    default_app = firebase_admin.initialize_app(cred_obj, {
        'databaseURL':'https://fpi-app-ca719-default-rtdb.firebaseio.com/'
        })
    ref = db.reference()
    
    usuarios_ref = ref.child('usuarios')
    for user_key, usuario in usuarios_ref.get().items():
        if (usuario.get('email') == data["email"]):
            if (usuario.get("senha") == data['senha']):
                return "Login Aceito"
            else:
                pass
    return "Senha/Usuário incorretos"

@app.route('/CheckEmail', methods=['POST'])
def CheckEmail():
    data = request.get_json()
    try:
        firebase_admin.delete_app(firebase_admin.get_app())
    except:
        pass
    firebase_credentials = os.getenv('CREDENCIAL')
    cred_dict = json.loads(firebase_credentials)
    cred_obj = firebase_admin.credentials.Certificate(cred_dict)
    default_app = firebase_admin.initialize_app(cred_obj, {
        'databaseURL':'https://fpi-app-ca719-default-rtdb.firebaseio.com/'
        })
    ref = db.reference()
    cursor = ref.child('usuarios')
    for key, checkemail in cursor.get().items():
        if (checkemail.get('email') == data['email']):
            return "E-mail já foi cadastrado!"
    return "Não existe"
  
if __name__ == "__main__":
  app.run(host='0.0.0.0')

