from backend.server import db, TestCase


def test_db():
    db.create_all()
    all=TestCase.query.all()
    print(all)
    testcase=TestCase(name="1", steps='1,2,3')
    db.session.add(testcase)
    db.session.commit()
    all = TestCase.query.all()
    print(all)

