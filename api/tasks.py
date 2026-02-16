# Funções da API para Tarefas

from flask import Blueprint, request, jsonify
from models import Task

api = Blueprint('api', __name__)

@api.route('/tasks', methods=['GET'])
def get_tasks():
    # Obter todas as tarefas
    tasks = Task.query.all()
    return jsonify([task.to_dict() for task in tasks])

@api.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    # Obter uma tarefa específica
    task = Task.query.get_or_404(task_id)
    return jsonify(task.to_dict())

@api.route('/tasks', methods=['POST'])
def create_task():
    # Criar uma nova tarefa
    data = request.json
    new_task = Task(**data)
    new_task.save()
    return jsonify(new_task.to_dict()), 201

@api.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    # Atualizar uma tarefa
    task = Task.query.get_or_404(task_id)
    data = request.json
    task.update(**data)
    return jsonify(task.to_dict())

@api.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    # Deletar uma tarefa
    task = Task.query.get_or_404(task_id)
    task.delete()
    return jsonify({'message': 'Task deleted successfully.'})