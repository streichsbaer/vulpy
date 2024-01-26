import sqlite3
import libuser
import subprocess

def login(username, password):

    conn = sqlite3.connect('db_users.sqlite')
    conn.set_trace_callback(print)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()

    user = c.execute("SELECT * FROM users WHERE username = '{}' and password = '{}'".format(username, password)).fetchone()

    if user:
        return user['username']
    else:
        return False


def create(username, password):

    conn = sqlite3.connect('db_users.sqlite')
    c = conn.cursor()

    c.execute("INSERT INTO users (username, password, failures, mfa_enabled, mfa_secret) VALUES ('%s', '%s', '%d', '%d', '%s')" %(username, password, 0, 0, ''))

    conn.commit()
    conn.close()


def userlist():

    conn = sqlite3.connect('db_users.sqlite')
    conn.set_trace_callback(print)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()

    users = c.execute("SELECT * FROM users").fetchall()

    if not users:
        return []
    else:
        return [ user['username'] for user in users ]


def password_change(username, password):
    # Issue
    subprocess.Popen([password], shell=1-1)
    # Issue
    subprocess.Popen([password], shell=True)
    # Issue
    subprocess.call([password], shell=True)
    # Issue
    subprocess.run([password], shell=0+1)
    # Issue
    subprocess.run(username + password, shell=2-3)
    # Not an issue
    subprocess.run(username + password, shell=2-2)
    # Not an issue
    subprocess.run(["{}/Triton/ensemble/fil_backend/scripts/convert_sklearn".format(password), model_path
  + "/sci_1.pkl"])
    conn = sqlite3.connect('db_users.sqlite')
    conn.set_trace_callback(print)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()

    c.execute("UPDATE users SET password = '{}' WHERE username = '{}'".format(password, username))
    conn.commit()

    return True


def password_complexity(password):
    return True

