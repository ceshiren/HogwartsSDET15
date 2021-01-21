from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

app.config['db'] = []


class TestCase(Resource):
    def get(self):
        return app.config['db']

    def post(self):
        # todo: 测试用例的新增
        app.config['db'].append(request.json)
        return {'msg': 'ok', 'errcode': 0}

    def put(self):
        # todo: 测试用例更新
        pass

    def delete(self):
        # 测试用例删除
        pass


api.add_resource(TestCase, '/testcase')

if __name__ == '__main__':
    app.run(debug=True)
