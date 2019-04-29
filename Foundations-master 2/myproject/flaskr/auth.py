import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')


# @bp.route associates the URL /register with the register view function.
# When Flask receives a request to /auth/register,
# it will call the register view and use the return value as the response.
@bp.route('/register', methods=('GET', 'POST'))
def register():
        # If the user submitted the form, request.method will be 'POST'.
        # In this case, start validating the input.
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None

        # Validate that username and password are not empty.
        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'

        # Validate that username is not already registered by querying
        # the database and checking if a result is returned
        elif db.execute(
            'SELECT id FROM user WHERE username = ?', (username,)
        ).fetchone() is not None:
            error = 'User {} is already registered.'.format(username)

        # insert the new user data into the database
        if error is None:
            db.execute(
                'INSERT INTO user (username, password) VALUES (?, ?)',
                (username, generate_password_hash(password))
            )
            db.commit()
            # redirected to the login page
            return redirect(url_for('auth.login'))

        # If validation fails, the error is shown
        flash(error)

    return render_template('auth/register.html')


@bp.route('/login', methods=('GET', 'POST'))
def login():
        # user is queried first and stored in a variable
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone()

        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password.'

        if error is None:
                # session is a dict that stores data across requests.
                # When validation succeeds, the user’s id is stored in a new session
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('index'))

        flash(error)

    return render_template('auth/login.html')


# checks if a user id is stored in the session and gets that
# user’s data from the database and stores it
# it lasts for the length of the request
@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM user WHERE id = ?', (user_id,)
        ).fetchone()


# removes the user id from the session
# Then load_logged_in_user won’t load a user on subsequent requests
@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


# requires a user to be logged in
#  checks if a user is loaded and redirects to the login page otherwise
def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
                #  generates the URL to a view based on a name and arguments
                # The name associated with a view is also called the endpoint,
                # and by default it’s the same as the name of the view function
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view