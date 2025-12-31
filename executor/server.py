from flask import Flask, request, jsonify
import sys, io

app = Flask(__name__)

@app.route('/execute', methods=['POST'])
def execute():
    code = request.json.get("code", "")
    stdout_capture = io.StringIO()
    sys.stdout = stdout_capture
    try:
        exec(code, {"__builtins__": __builtins__}, {})
        result = stdout_capture.getvalue()
        return jsonify({"status": "SUCCESS", "output": result})
    except Exception as e:
        return jsonify({"status": "ERROR", "error": str(e)}), 400
    finally:
        sys.stdout = sys.__stdout__

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)