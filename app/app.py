from flask import Flask, jsonify, request

app = Flask(__name__)

tasks = [
    {"id": 1, "title": "Complete Day 1 DevOps project", "done": True},
    {"id": 2, "title": "Set up LocalStack container", "done": False}
]

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "ok"}), 200

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({"tasks": tasks}), 200

@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.json
    if not data or 'title' not in data:
        return jsonify({"error": "Missing 'title' field"}), 400
    
    new_task = {
        "id": len(tasks) + 1,
        "title": data['title'],
        "done": False
    }
    tasks.append(new_task)
    return jsonify(new_task), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

