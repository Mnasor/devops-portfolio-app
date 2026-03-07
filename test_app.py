from app import app

def test_home_route():
    # 1. إنشاء عميل وهمي لمحاكاة متصفح المستخدم
    client = app.test_client()
    
    # 2. إرسال طلب للمسار الرئيسي (/)
    response = client.get('/')
    
    # 3. التحقق (Assert): هل التطبيق رد بنجاح (الكود 200)؟
    assert response.status_code == 200
    
    # 4. التحقق: هل الرد يحتوي على كلمة Success التي برمجناها؟
    assert b"Success" in response.data
