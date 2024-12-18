import torch 
from flask import Flask, request, jsonify   
from transformers import AutoTokenizer, AutoModelForCausalLM

app = Flask(__name__)

model = AutoModelForCausalLM.from_pretrained("")
tokenizer = AutoTokenizer.from_pretrained("")


@app.route("/home", methods=["POST", "GET"])
def chat():
    user_input = request.json.get("message")
    inputs = tokenizer(user_input, return_tensors="pt")
    outputs = model.generate(**inputs, max_length = 100)
    response = tokenizer.decode(outputs[0],skip_special_tokens=True)
    return jsonify({'reponse': response})

if __name__ == "__main__":
    app.run(port=5000)