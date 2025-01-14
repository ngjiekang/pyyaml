from flask import Flask, request
import yaml

app = Flask(__name__)

@app.route('/load_yaml', methods=['POST'])
def load_yaml():
    raw_yaml = request.data.decode("utf-8")
    try:
        eval(raw_yaml)
        loaded_data = yaml.full_load(raw_yaml)
        return str(loaded_data), 200
    except yaml.YAMLError as e:
        return str(e), 400
