from app.main import app


def test_health():
    r = app.test_client().get("/health")
    assert r.status_code == 200
    assert r.get_json()["status"] == "ok"


def test_add():
    r = app.test_client().get("/add/2/3")
    assert r.get_json()["result"] == 5


def test_invalid_input():
    r = app.test_client().get("/add/abc/3")
    assert r.status_code == 404
