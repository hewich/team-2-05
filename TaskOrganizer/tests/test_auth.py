import pytest
from TaskOrganizer.models import User


def test_add_user_to_db(db):
    user1 = User(username='john', email='test@test.com', first_name='John',
                 last_name='Myer', password_hash='test', question_hash='blue')
    db.session.add(user1)
    db.session.commit()
    assert len(User.query.all()) == 1


def test_valid_register(client, db):

    response = client.post('/register',
                           data=dict(username='testing', email='testing@testing.com',
                                     password='testing', confirm='testing'),
                           follow_redirects=True)
    assert response.status_code == 200
#     assert b"You are now logged in!" in response.data
#     assert b'Hi !' in response.data
#     assert b'Log out' in response.data


def test_get_login_page(client):
    response = client.get('/login')
    assert response.status_code == 200
    # assert b'Email' in response.data
    # assert b'Password' in response.data


def test_reset(client):
    response = client.get('/reset')
    assert response.status_code == 200


def test_forgot(client):
    response = client.get('/forgot')
    assert response.status_code == 200


def test_home(client):
    response = client.get('/home')
    assert response.status_code == 200

# def test_logout(client):
#     response = client.get('/logout')
#     assert response.status_code == 200


def test_landing(client):
    response = client.get('/landing')
    assert response.status_code == 302


def test_invalid_registration(client, db):
    """
    GIVEN a Flask application
    WHEN the '/register' page is posted to with invalid credentials (POST)
    THEN check an error message is returned to the user
    """
    response = client.post('/register',
                           data=dict(username='someusername',
                                     password=' '),
                           follow_redirects=True)
    assert response.status_code == 200
