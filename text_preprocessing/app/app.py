import logging
import os
from flask import Flask, request, jsonify
import yaml
from transformers import AutoTokenizer

log_path = "logs/app.log"
os.makedirs(os.path.dirname(log_path), exist_ok=True)
with open(log_path, "a") as log_file:
    pass

logging.basicConfig(filename=log_path, level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

app = Flask(__name__)

try:
    with open("resources/config.yaml", "r") as config_file:
        config = yaml.safe_load(config_file)
    model_url = config["model_url"]
    tokenizer = AutoTokenizer.from_pretrained(model_url)
except Exception as e:
    logging.exception("Error loading model and tokenizer from config.yaml")

@app.route('/')
def home():
    try:
        return open("index.html").read()
    except Exception as e:
        logging.exception("Error reading index.html file")
        return "Error reading index.html file", 500

@app.route('/process', methods=['POST'])
def process():
    try:
        data = request.get_json()
        text_input = data['text_input']
        context = data['context']

        if context.strip() == "":
            inputs = tokenizer(text_input, truncation=True, padding=True)
        else:
            inputs = tokenizer(text_input, context, truncation=True, padding=True)

        logging.info(f"Tokenized inputs: {inputs}")

        return jsonify(inputs.data)
    except Exception as e:
        logging.exception("Error processing input")
        return "Error processing input", 500

if __name__ == '__main__':
    try:
        app.run(debug=True, host='0.0.0.0')
    except Exception as e:
        logging.exception("Error starting the server")
