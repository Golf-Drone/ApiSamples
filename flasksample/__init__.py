import os

from flask import (Flask, render_template, request, redirect, url_for)

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'testdb.sqlite'),
    )

    try:
        os.makedirs(app.instance_path)  # Will be used for database file
    except OSError:
        pass

    from . import dbstuff
    dbstuff.init_app(app)

    @app.route("/", methods=['GET', 'POST'])
    def hello():
        if request.method == "POST":
            name = request.form['name']
            db = dbstuff.get_db()
            row = db.execute('SELECT * FROM sampledata WHERE name = ?', (name,)).fetchone()
            if row is None:
                return redirect(url_for('new_user', name=name))
            return redirect(url_for('existing_user', name=name, comments=row['comments']))

        return render_template("index.html")

    @app.route("/newuser/<name>", methods=['GET', 'POST'])
    def new_user(name, methods=['GET', 'POST']):
        if request.method == "POST":
            name = request.form.get('name')
            comments = request.form.get('comments')
            db = dbstuff.get_db()
            try:
                db.execute('INSERT INTO sampledata (name, comments) VALUES (?, ?)', (name, comments))
                db.commit()
            except db.IntegrityError:
                return f"User {name} is already registered."
            else:
                return redirect(url_for("hello"))

        return render_template("newuser.html", name=name)

    @app.route("/existinguser/<name>/<comments>", methods=['GET', 'POST'])
    def existing_user(name, comments, methods=['GET', 'POST']):
        if request.method == "POST":
            db = dbstuff.get_db()
            try:
                db.execute('DELETE FROM sampledata WHERE name = ?', (name,))
                db.commit()
            except db.IntegrityError:
                return f"User {name} doesn't exist."
            else:
                return redirect(url_for("hello"))

        return render_template("existinguser.html", name=name, comments=comments)

    return app
