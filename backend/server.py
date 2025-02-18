from flask import Flask, jsonify, request
from backend.langgraph_agent import MasterAgent

backend_app = Flask(__name__)

# Example of an API endpoint
@backend_app.route('/', methods=['GET'])
def index():
    return jsonify({"status": "Running"}), 200

@backend_app.route('/generate_newspaper', methods=['POST'])
def generate_newspaper():
    data = request.json
    queries = data["topics"]
    layout = data["layout"]
    master_agent = MasterAgent()
    newspaper = master_agent.run(queries, layout)
    return jsonify({"path": newspaper}), 200

