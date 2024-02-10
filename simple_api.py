from flask import Flask, jsonify
import time

app = Flask(__name__)

@app.route('/test', methods=['GET'])
def test():
    start_time = time.time()  
    time.sleep(1)  
    response_time = time.time() - start_time 
    return jsonify({'message': 'Response received', 'response_time': f"{response_time} seconds"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
