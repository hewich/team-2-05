Functions
===========

.. automodule:: forms
   :members:
   :undoc-members:

.. Professor Carlo's said I can write this .models by hand because there's some issues
.. with Sphinx.
.. [automodule:: models]
.. [:members:]
.. [:undoc-members:]


.. Professor Carlo's said I can write this .routes by hand because there's some issues
.. with Sphinx.
.. [automodule:: myapp.routes]
.. [:members:]
.. [:undoc-members:]


routes./logout

    The logout function terminates the login session from the user
    Arg:
    It identifies the current logged in from the database and push them out.

    Returns:
    User goes to the home page from the app



routes./landing

    The landing page provides users with the add task, remove task and view task from the app

    Arg:
    It crates the landing page

    Returns:
    Returns an html page named landing


routes./register

     The register page let user to register to the app using the user, password and answer of
     the security question.

     Arg:
     The information gets added to the database. Once done it sends a flash message.

     Return:
     If the registration was successful the user gets sent to the login page to reenter the
     information.

routes./login

     The login helps us identify registered users from new users.

     Arg: If registered users successfully enters information. Then they are send to the landing
     page. At the same time, new users can register to the Task Organizer entering information in
     the login form. If user enters wrong information for username or password a flash message
     will pop.

routes./add

     The add tasks function allow users to designate tasks and descriptions to help them keep up with the day

     Arg:
     It defines the task function and then it creates the task name and description and it gets saved on the database
     of the current user

     Returns:
     Returns the task saved in the add.html page

routes./view

     The view function displays the saved on the database recorded by the add.html. Also if user deletes task
     they are no longer visible in the view.html page.

     Arg: User gets authenticated and the task function displays the task while the organize function orders the task
     alphabetically.

     Return: Visible on the view.html page

routes./remove

     The remove feature allow users to delete a task.

     Arg:
     We created a new form named TaskForm(). This function is visible in the remove.html page.
     Once the users task is saved it's saved on the database and in order to be removed they need to
     provide with the exact task name.

     Return:
     The task is automatically deleted from the database.

routes./delete_all

     The delete all feature allow us to delete all the task at the same time by one click.

     Arg:
     It tracks saved tasks from the database

     Returns:
     It displays no tasks on the remove.html file

routes./forgot_password

     The forgot password features helps users set up a new password if forgotten.

     Arg:
     It displays the forgot form.

     Return:
     User gets the new html page.

routes./reset
    The reset function let the users retrieve their account if they forgot their password

    Arg:
    The user when signing up to the app provided with a security question about what's their favorite color.
    If user provided the right color saved on the database they would be able to get back their account.
    We created a ForgotForm that needs to be validated with the users color and user name if the user answers
    as recorded in the database then they gets to choose their new password.

    Returns:
    The user is send to a reset.html page where they need to reset their password.
    If they where not able to provide them they are sent to the login page again

class.models.User
    User Data Model

    Arg: Defines the class User as data model. This is where we define who our user is.
    It sets a authentication field, after that is the construction of the user field and
    relationships. Then the set up of user password hash.

    Return: __repr__ should return a printable representation of the object and
    it returns the User. All saved on the database.

class.models.Task
    Declaring Models

    Arg: This is where we create the Task and description the user is going to save in their
    session.

    Return: __repr__ should return a printable representation of the object and
    it returns the Task.

models.load_user(id)
    Flask LogIn

    Arg: Once user has authenticated

    Returns: The code logs them in with the function that insets user id into the session.



