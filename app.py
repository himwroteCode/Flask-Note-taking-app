from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'index'

@app.route('/', methods=["GET", "POST"])
def index():
    if 'notes' not in session:
        session['notes'] = []
    notes = session['notes']
    
    if request.method == "POST":
        note = request.form["note"]
        if len(note) >= 1:
            notes.append(note)
            session['notes'] = notes
            return render_template("home.html", notes=notes)
        else:
            return render_template("home.html", notes=notes)

    if request.method == "GET":
        return render_template("home.html", notes=notes)

if __name__ == '__main__':
    app.run(debug=True)
