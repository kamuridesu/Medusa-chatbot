from flask import Flask, json, request, jsonify, redirect
from bot import Bot
from messages_processor import MessagePreProcessor


app = Flask(__name__)
bot = Bot()
bot.train(MessagePreProcessor("example.log").pre_processed_messages)


@app.route('/', methods=['GET'])
def index():
    if request.args.get('text'):
        response = bot.get_response(request.args.get('text'))
        return jsonify(response)
    else:
        return jsonify({"status": "error", "response": "No text parameter"})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)
