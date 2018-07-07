#!flask/bin/python
from flask import Flask, jsonify, make_response, request, abort, url_for
from flask_httpauth import HTTPBasicAuth

import maps
import database


auth = HTTPBasicAuth()
db = database.Database()
@auth.get_password
def get_password(username):
    if username == 'booligan':
        return 'python'
    return None

@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)

app = Flask(__name__)


@app.route('/bool/get', methods=['GET'], strict_slashes=False)
def get_tasks():
    #return jsonify({'tasks': tasks})
    #return jsonify({'tasks': [make_public_task(task) for task in tasks]})
    return jsonify({'table': str(db.getTableSnapshot("Test1"))})

@app.route('/bool/get/locations', methods=['GET'], strict_slashes=False)
def get_history():
    #return jsonify({'tasks': tasks})
    #return jsonify({'tasks': [make_public_task(task) for task in tasks]})
    return jsonify({'table': str(db.getTableSnapshot("LocationHistory"))})

@app.route('/bool/location/', methods=['POST'], strict_slashes=False)
def setLocation():
    if not request.json or not 'latitude' in request.json or not 'longitude' in request.json:
        abort(400)
    db.insert("LocationHistory", request.json['latitude'], request.json['longitude'])
    print(request.json['latitude'] + " : " + request.json['longitude'])
    return jsonify("SUCCESS! YOU SENT A LOCATION: " + request.json['latitude'] + " : " + request.json['longitude'])

@app.route('/bool/post/', methods=['POST'], strict_slashes=False)
@auth.login_required
def create_task():
    if not request.json or not 'title' in request.json:
        abort(400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({'task': task}), 201

@app.route('/bool/connection', methods=['POST'], strict_slashes=False)
def connectionRequest():
    if not request.json:
        abort(400)
    if request.json['command'] == "start":
        db.connect()
        return jsonify(["Connection started"]), 201
    elif request.json['command'] == "stop":
        db.closeConn()
        return jsonify(["Connection closed"]), 201
    else:
        db.customCmd(request.json['command'])
        return jsonify(["Command executed"]), 201


@app.route('/bool/put/<int:task_id>', methods=['PUT'], strict_slashes=False)
def update_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'title' in request.json and type(request.json['title']) != unicode:
        abort(400)
    if 'description' in request.json and type(request.json['description']) is not unicode:
        abort(400)
    if 'done' in request.json and type(request.json['done']) is not bool:
        abort(400)
    task[0]['title'] = request.json.get('title', task[0]['title'])
    task[0]['description'] = request.json.get('description', task[0]['description'])
    task[0]['done'] = request.json.get('done', task[0]['done'])
    return jsonify({'task': task[0]})

@app.route('/bool/delete/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    tasks.remove(task[0])
    return jsonify({'result': True})

def make_public_task(task):
    new_task = {}
    for field in task:
        if field =='id':
            new_task['uri'] = url_for('get_tasks', task_id=task['id'], _external=True)
        else:
            new_task[field] = task[field]
    return new_task

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not Found'}), 404)

@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Invalid post'}), 400)

@app.errorhandler(500)
def errorFunc(error):
    return make_response(jsonify({'error': 'Something with wrong'}), 500)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5558)
    #app.run(debug=True)

