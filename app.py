from flask import Flask, render_template, request

app = Flask(__name__)

notes = []

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if request.form.get("action") == "add_note":
            note = request.form.get("note")
            if note:
                notes.append(note)
        elif request.form.get("action") == "delete_note":
            note_index = int(request.form.get("note_index"))
            if 0 <= note_index < len(notes):
                del notes[note_index]
        elif request.form.get("action") == "delete_all_notes":
            notes.clear()
    return render_template("home.html", notes=notes)

if __name__ == '__main__':
    app.run(debug=True)
