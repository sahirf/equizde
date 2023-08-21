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

@app.route('/api/get_ips', methods=['GET'])
def get_ips():
    return jsonify({"ip_list": ip_list})

if __name__ == '__main__':
    app.run(debug=True)

