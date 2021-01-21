from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)

app.config['db'] = []

# java mybatis hibernate python sqlalchemy
username = 'python15'
password = 'ceshiren.com'
host = 'stuq.ceshiren.com:23306'
dbname = 'python15'
options = 'charset=utf8mb4'
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{username}:{password}@{host}/{dbname}?{options}'
db = SQLAlchemy(app)


class TestCase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120), unique=False, nullable=True)
    steps = db.Column(db.String(1024), nullable=True)

    def __repr__(self):
        # 方便打印
        return '<TestCase %r>' % self.name


class TestCaseService(Resource):
    def get(self):
        testcase_id = request.args.get('id', None)
        if testcase_id:
            testcase = TestCase.query.filter_by(id=testcase_id).first()
            return {'errcode': 1, 'body': str(testcase)}
        else:
            return {'errcode': 1, 'body': [str(testcase) for testcase in TestCase.query.all()]}

    def post(self):
        # todo: 测试用例的新增
        print(request.json)
        testcase = TestCase(**request.json)
        print(testcase)
        db.session.add(testcase)
        db.session.commit()

        return {'msg': 'ok', 'errcode': 0}

    def put(self):
        # todo: 测试用例更新
        pass

    def delete(self):
        # 测试用例删除
        pass


api.add_resource(TestCaseService, '/testcase')

if __name__ == '__main__':
    app.run(debug=True)
