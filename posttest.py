exit#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, abort, request, jsonify

myapp = Flask(__name__)

# 测试数据暂时存放
tasks = [
    {
        'id': 1,
        'title': 'id1',
        'done': True
    },
    {
        'id': 2,
        'title': 'id2',
        'done': False
    }
]

@myapp.route('/', methods=['GET'])
def index():
    return jsonify({'tasks': tasks})

@myapp.route('/get_task/<task_id>', methods=['GET'])
def get_task(task_id):
    for task in tasks:
        if(task['id']==int(task_id)):
            return jsonify({'tasks': task})
    abort(404)

#curl "http://127.0.0.1:5000/post_tasks/" -H "Content-Type: application/json" -d "{\"title\":\"id\"}" -X POST
@myapp.route('/post_tasks/', methods=['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        abort(400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title']+str(tasks[-1]['id'] + 1),
        'done': False
    }
    tasks.append(task)
    return jsonify({'task': task}), 201

#curl "http://127.0.0.1:5000/upd_tasks/2" -H "Content-Type: application/json" -d "{\"title\":\"upd\"}" -X PUT
@myapp.route('/upd_tasks/<task_id>', methods=['PUT'])
def update_task(task_id):
    for task in tasks:
        if(task['id']==int(task_id)):
            u_task = task
    if u_task:
        u_task['title'] = request.json['title']
        return jsonify({'tasks': u_task})

#curl "http://127.0.0.1:5000/del_tasks/1" -X DELETE
@myapp.route('/del_tasks/<task_id>', methods=['DELETE'])
def delete_task(task_id):
    for task in tasks:
        if(task['id']==int(task_id)):
            d_task = task
    if d_task:
        tasks.remove(d_task)
        return jsonify({'result': True})
    return jsonify({'result': False})


# if __name__ == '__main__':
#     myapp.run(debug=True, host='127.0.0.1', port=5000)