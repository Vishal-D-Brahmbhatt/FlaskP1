"""This test the homepage"""


def test_request_main_menu_links(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'<a class="nav-link" href="/page1">GIT</a>' in response.data
    assert b'<a class="nav-link" href="/page2">DOCKER</a>' in response.data
    assert b'<a class="nav-link" href="/page3">PYTHON/FLASK</a>' in response.data
    assert b'<a class="nav-link" href="/page4">CI/CD</a>' in response.data
    assert b'<a class="dropdown-item" href="/page5">OOP</a>' in response.data
    assert b'<a class="dropdown-item" href="/page6">AAA Testing</a>' in response.data
    assert b'<a class="dropdown-item" href="/page7">PYLINT</a>' in response.data
    assert b'<a class="dropdown-item" href="/page8">SOLID and DESIGN PATTERN</a>' in response.data


def test_request_index(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Z Layout" in response.data


def test_request_page1(client):
    """This makes the page1"""
    response = client.get("/page1")
    assert response.status_code == 200
    assert b"GIT" in response.data


def test_request_page2(client):
    """This makes the page2"""
    response = client.get("/page2")
    assert response.status_code == 200
    assert b"DOCKER" in response.data


def test_request_page3(client):
    """This makes the page3"""
    response = client.get("/page3")
    assert response.status_code == 200
    assert b"PYTHON/FLASK" in response.data


def test_request_page4(client):
    """This makes the page4"""
    response = client.get("/page4")
    assert response.status_code == 200
    assert b"CI/CD" in response.data


def test_request_page5(client):
    """This makes the page5"""
    response = client.get("/page5")
    assert response.status_code == 200
    assert b"OOP" in response.data


def test_request_page6(client):
    """This makes the page6"""
    response = client.get("/page6")
    assert response.status_code == 200
    assert b"AAA TESTING" in response.data


def test_request_page7(client):
    """This makes the page7"""
    response = client.get("/page7")
    assert response.status_code == 200
    assert b"PYLINT" in response.data


def test_request_page8(client):
    """This makes the page8"""
    response = client.get("/page8")
    assert response.status_code == 200
    assert b"SOLID PATTERN AND DESIGN PATTERN" in response.data
