import os
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from prometheus_flask_exporter import PrometheusMetrics  # السطر الأول المضاف

app = Flask(__name__)
metrics = PrometheusMetrics(app) # السطر الثاني المضاف: تفعيل المراقبة فوراً!
# إعداد رابط الاتصال بقاعدة البيانات
# السحر هنا: نستخدم اسم الحاوية 'db' بدلاً من 'localhost'
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'postgresql://devops_user:devops_password@db:5432/portfolio_db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# إنشاء جدول بسيط في قاعدة البيانات
class Visit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(100), nullable=False)

# دالة لإنشاء الجدول عند تشغيل التطبيق
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    try:
        # تسجيل زيارة جديدة في قاعدة البيانات
        new_visit = Visit(message="Hello from PostgreSQL!")
        db.session.add(new_visit)
        db.session.commit()
        
        # معرفة عدد الزيارات الكلي
        visit_count = Visit.query.count()
        
        return jsonify(
            message="Hello Mansour! Your DevOps Pipeline is working perfectly.",
            status="Success",
            version="2.0 - auto Deployed",
            total_visits=visit_count
        )
    except Exception as e:
        return jsonify(status="Failed", error=str(e)), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

@app.route('/health')
def health():
    return "Healthy", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
