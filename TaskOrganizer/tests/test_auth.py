import pytest
from myapp.models import User, Task
from myapp.forms import LoginForm,RegisterForm, TaskForm, ForgotForm




def test_login(client):
    response = client.get('/login')
    assert response.status_code == 200


def test_add_user_to_db(db):
    test_user = User(email='test_user@gmail.com', firstname='test',
                     lastname='user', password_hash='1234', username='test_user')
    db.session.add(test_user)
    db.session.commit()
    assert len(User.query.all()) == 1



def test_valid_register(client, db):
    response = client.post('/login',
                           data=dict(firstname='testing', email='testing@testing.com',
                                     password='testing', confirm='testing'),
                           follow_redirects=True)
    assert response.status_code == 200


def test_verify_user_exists(db):
    user = User.query.get(1)
    assert user.is_authenticated == True



def test_new_task(db):
    note = Post(task_name='some task', user_id='1',Description='eat food')
    db.session.add(task)
    db.session.commit()
    assert len(Post.query.all()) == 1
    assert Post.query.get(1).task_name == 'some task'








    def test_new_user(new_user):
        """
        GIVEN a User model
        WHEN a new User is created
        THEN check the email, hashed_password, authenticated, and role fields are defined correctly
        """
        assert new_user.username== 'someusername'
        assert new_user.hashed_password != 'testpassword'
        assert not new_user.authenticated
        assert new_user.role == 'user'


    def test_setting_password(new_user):
        """
        GIVEN an existing User
        WHEN the password for the user is set
        THEN check the password is stored correctly and not as plaintext
        """
        new_user.set_password('MyNewPassword')
        assert new_user.hashed_password != 'MyNewPassword'
        assert new_user.is_correct_password('MyNewPassword')
        assert not new_user.is_correct_password('MyNewPassword2')
        assert not new_user.is_correct_password('testpassword')


    def test_user_id(new_user):
        """
        GIVEN an existing User
        WHEN the ID of the user is defined to a value
        THEN check the user ID returns a string (and not an integer) as needed by Flask-WTF
        """
        new_user.id = 17
        assert isinstance(new_user.get_id(), str)
        assert not isinstance(new_user.get_id(), int)
        assert new_user.get_id() == "17"
