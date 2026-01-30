from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}

def test_hello_default():
    r = client.get("/hello")
    assert r.status_code == 200
    assert r.json() == {"message": "hello, world"}

def test_hello_with_name():
    r = client.get("/hello?name=junior")
    assert r.status_code == 200
    assert r.json() == {"message": "hello, junior"}

def test_echo_ok():
    r = client.post("/echo", json={"text": "abc"})
    assert r.status_code == 200
    assert r.json() == {"text": "abc", "length": 3}

def test_sumab():
    r=client.get("/sum?a=2&b=3")
    assert r.status_code==200
    assert r.json()=={"result":5}

def test_echo_validation_error():
    # sem o campo obrigatório "text"
    r = client.post("/echo", json={})
    assert r.status_code == 422
