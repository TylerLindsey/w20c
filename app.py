# python –m flask run
from flask import Flask, jsonify, request
# import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

animals=[
  'shark',
  'tiger',
  'bear',
  'komodo dragon',
  'orca',
  'wolf',
  'crocodile',
  'lion'
]

@app.get('/api/animals')
def animals_get():
  args = request.args
  animal_id = args.get('animalId')
  if animal_id == None:
    return jsonify(animals), 200
  else:
    return jsonify(animals[animal_id]), 200

@app.post('/api/animals')
def animals_post():
  animal_type = request.jsons
  print(animal_type)
  # if upload is successful then
  # print("upload to list success")
  # else:
  # print("error, upload failed")


# @app.patch('/api/animals')
# def animals_patch():


# @app.delete('/api/animals')
# def animals_delete():