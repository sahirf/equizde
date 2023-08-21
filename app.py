from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

ip_list = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/record_ip', methods=['POST'])
def record_ip():
    data = request.get_json()
    ip_address = data.get('ip')
    ip_list.append(ip_address)
    return jsonify({"message": "IP recorded successfully."})

if __name__ == '__main__':
    app.run(debug=True)

