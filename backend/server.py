import json

from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from jenkinsapi.jenkins import Jenkins

app = Flask(__name__)
api = Api(app)
CORS(app)

app.config['db'] = []

# java mybatis hibernate python sqlalchemy
username = 'python15'
password = 'ceshiren.com'
host = 'stuq.ceshiren.com:23306'
dbname = 'python15'
options = 'charset=utf8mb4'
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{username}:{password}@{host}/{dbname}?{options}'
db = SQLAlchemy(app)

jenkins = Jenkins(
    'http://stuq.ceshiren.com:8020',
    username='seveniruby',
    password='11c5aeeb345481059b7146fbccc179d17d'
)
jenkins_job = jenkins['python15_task']


class TestCase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120), unique=False, nullable=True)
    steps = db.Column(db.String(1024), nullable=True)

    def __repr__(self):
        # 方便打印
        return '<TestCase %r>' % self.name

    def as_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'steps': self.steps
        }


class TestCaseService(Resource):
    def get(self):
        testcase_id = request.args.get('id', None)
        if testcase_id:
            testcase = TestCase.query.filter_by(id=testcase_id).first()
            return {'errcode': 0, 'body': testcase.as_dict()}
        else:
            return {'errcode': 0, 'body': [testcase.as_dict() for testcase in TestCase.query.all()]}

    def post(self):
        # todo: 测试用例的新增
        print(request.json)
        testcase = TestCase(**request.json)
        testcase.id = None
        print(testcase)
        db.session.add(testcase)
        db.session.commit()

        return {'msg': 'ok', 'errcode': 0}

    def put(self):
        # todo: 测试用例更新
        testcase_new = TestCase(**request.json)
        if testcase_new.id:
            testcase = TestCase.query.filter_by(id=testcase_new.id).first()
            testcase.name = testcase_new.name
            testcase.description = testcase_new.description
            testcase.steps = testcase_new.steps
            db.session.commit()
            return {'msg': 'ok', 'errcode': 0}
        else:
            return {'msg': 'error', 'errcode': 1}

    def delete(self):
        # 测试用例删除
        pass


# task -> testcases -> []
# task testcase  中间表多对多关系
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=True)
    description = db.Column(db.String(120), unique=False, nullable=True)
    testcases = db.Column(db.String(1024), nullable=True)

    def __repr__(self):
        # 方便打印
        return '<Task %r>' % self.id

    def as_dict(self):
        id_list=json.loads(self.testcases)

        name_list=[]
        for testcase_id in id_list:
            testcase=TestCase.query.filter_by(id=testcase_id).first()
            name_list.append(testcase.name)


        return {
            'id': self.id,
            'name': self.name,
            'testcases': json.loads(self.testcases),
            'command':  'pytest --junitxml=junit.xml '+' '.join(name_list),
        }


# 一个测试任务/测试计划 代表了测试用例的集合与编排顺序
class TaskServie(Resource):
    def get(self):
        task_id = request.args.get('id', None)
        if task_id:
            task = Task.query.filter_by(id=task_id).first()
            return {'errcode': 0, 'body': task.as_dict()}
        else:
            return {'errcode': 0, 'body': [task.as_dict() for task in Task.query.all()]}

    def post(self):
        data = request.json.copy()
        data['testcases'] = json.dumps(data['testcases'])
        task = Task(**data)
        print(task)
        db.session.add(task)
        db.session.commit()

        return {'msg': 'ok', 'errcode': 0}

    def put(self):
        pass

    def delete(self):
        pass


class ExecutionService(Resource):
    def get(self):
        pass

    def post(self):
        task_id = request.json.get('task_id')
        task = Task.query.filter_by(id=task_id).first()
        r = jenkins_job.invoke(build_params={
            'task': json.dumps(task.as_dict()),
            'task_id': task.id,
            'command': task.as_dict()['command']
        })
        return {'errcode': 0, 'msg': 'ok'}


class ResultService(Resource):
    """
    测试结果的保存
    """
    pass


class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(120), unique=False, nullable=True)
    output = db.Column(db.String(1024), nullable=True)

    testcase_id = db.Column(db.Integer, db.ForeignKey('test_case.id'))
    testcase = db.relationship('TestCase', backref='reports', lazy=True)

    def as_dict(self):
        return {
            'id': self.id,
            'status': self.status,
            'output': self.output
        }


class ReportService(Resource):
    """
    查询测试结果生成测试报告
    """

    def get(self):
        report_id = request.args.get('id', None)
        if report_id:
            report = Task.query.filter_by(id=report_id).first()
            return {'errcode': 1, 'body': report.as_dict()}
        else:
            return {'errcode': 1, 'body': [report.as_dict() for report in Report.query.all()]}

    def post(self):
        """

        :return:
        """
        # todo: 需要一层从name到id之间的转换
        # data=request.json.copy()
        # data['testcase_id']=TestCase.query.filter_by(name=data['testcase_name']).first().id
        report = Report(**request.json)
        db.session.add(report)
        db.session.commit()
        return {'errcode': 0, 'msg': 'ok'}


class LoginService(Resource):
    def post(self):
        print(request.json)
        return {'errcode': 0, 'msg': 'login success'}


api.add_resource(TestCaseService, '/testcase')
api.add_resource(TaskServie, '/task')
api.add_resource(ExecutionService, '/execution')
api.add_resource(ReportService, '/report')
api.add_resource(LoginService, '/login')

if __name__ == '__main__':
    app.run(debug=True)
