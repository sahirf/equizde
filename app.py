from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def save_ip_to_file(ip_address):
    with open('ip_addresses.txt', 'a') as file:
        file.write(ip_address + '\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/record_ip', methods=['POST'])
def record_ip():
    data = request.get_json()
    ip_address = data.get('ip')
    save_ip_to_file(ip_address)
    return jsonify({"message": "IP recorded successfully."})

@app.route('/api/get_ips', methods=['GET'])
def get_ips():
    with open('ip_addresses.txt', 'r') as file:
        ip_list = file.read().splitlines()
    return jsonify({"ip_list": ip_list})

if __name__ == '__main__':
    app.run(debug=True)

