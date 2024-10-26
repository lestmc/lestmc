from app import create_app, db

app = create_app()

@app.route('/test')
def test():
    return "Hello from Vercel!"

# 确保在Vercel环境中创建数据库表
with app.app_context():
    db.create_all()

# Vercel需要这个变量名
application = app

if __name__ == '__main__':
    app.run(debug=True)
