import requests
from jenkinsapi.jenkins import Jenkins

from backend.server import db, TestCase


def test_db_init():
    db.create_all()


def test_db():
    db.create_all()
    all = TestCase.query.all()
    print(all)
    testcase = TestCase(name="1", steps='1,2,3')
    db.session.add(testcase)
    db.session.commit()
    all = TestCase.query.all()
    print(all)


def test_testcase_post():
    r = requests.post(
        'http://127.0.0.1:5000/testcase',
        json={'name': '4'}
    )
    assert r.status_code == 200


def test_task():
    r = requests.post(
        'http://127.0.0.1:5000/task',
        json={'testcases': [1, 2, 3]}
    )
    assert r.status_code == 200

    r = requests.get(
        'http://127.0.0.1:5000/task'
    )
    assert r.status_code == 200
    assert len(r.json()['body']) > 0


def test_jenkins():
    jenkins = Jenkins(
        'http://stuq.ceshiren.com:8020',
        username='seveniruby',
        password='11c5aeeb345481059b7146fbccc179d17d'
    )
    print(jenkins.version)
    print(jenkins.keys())
    jenkins['python15_task'].invoke(build_params={'task': 'demo'})

def test_execution():
    r=requests.post(
        'http://127.0.0.1:5000/execution',
        json={'task_id': 1}
    )
    assert r.status_code == 200
