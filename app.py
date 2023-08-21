from flask import Flask, request, jsonify

app = Flask(__name__)

ip_list = []

@app.route('/api/record_ip', methods=['GET', 'POST'])
def record_ip():
    ip_address = request.remote_addr
    ip_list.append(ip_address)
    return jsonify({"message": "IP recorded successfully."})

@app.route('/api/get_ips', methods=['GET'])
def get_ips():
    return jsonify({"ip_list": ip_list})

if __name__ == '__main__':
    app.run(debug=True)
