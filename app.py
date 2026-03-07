from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify(
            status="Success",
        message="Hello Mansour! Your DevOps Pipeline is working perfectly.",
        version="1.0"
    )

if __name__ == '__main__':
    # التطبيق سيعمل على المنفذ 5000 ويستقبل الاتصالات من أي IP
    app.run(host='0.0.0.0', port=5000)
