exit#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, abort, request, jsonify

myapp = Flask(__name__)

# 测试数据暂时存放
tasks = [
    {
        'id': '1',
        'v1': '2',
        'v2': '3'
    },
    {
        'id': '2',
        'v1': '3',
        'v2': '4'
    }
]

@myapp.route('/', methods=['GET'])
def index():
    return jsonify({'tasks': tasks})

@myapp.route('/get_task/<task_id>', methods=['GET'])
def get_task(task_id):
    for task in tasks:
        if(task['id']==task_id):
            return jsonify({'tasks': task})
    abort(404)

#curl "http://127.0.0.1:5000/set_task/" -H "Content-Type: application/json" -d "{\"id\":\"3\",\"v1\":\"4\",\"v2\":\"5\"}" -X POST
@myapp.route('/set_task/', methods=['POST'])
def set_task():
    jsdata = request.json
    task = {
        'id': jsdata['id'],
        'v1': jsdata['v1'],
        'v2': jsdata['v2']
    }
    tasks.append(task)
    return jsonify({'result': 'OK'})

#curl "http://127.0.0.1:5000/upd_tasks/2" -H "Content-Type: application/json" -d "{\"title\":\"upd\"}" -X PUT
@myapp.route('/upd_task/<task_id>', methods=['PUT'])
def update_task(task_id):
    for task in tasks:
        if(task['id']==task_id):
            u_task = task
    if u_task:
        u_task['title'] = request.json['title']
        return jsonify({'tasks': u_task})

#curl "http://127.0.0.1:5000/del_tasks/1" -X DELETE
@myapp.route('/del_task/<task_id>', methods=['DELETE'])
def delete_task(task_id):
    for task in tasks:
        if(task['id']==task_id):
            d_task = task
    if d_task:
        tasks.remove(d_task)
        return jsonify({'result': True})
    return jsonify({'result': False})


if __name__ == '__main__':
    myapp.run(debug=True, host='127.0.0.1', port=5000)