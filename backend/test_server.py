import requests

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
