import flask
import json
from flask import Flask, request, render_template

app = Flask(__name__)

# ---------------- Root Route ----------------
@app.route("/")
def index():
    return "<h2>Welcome to Flask app using UV!</h2>"

# ---------------- URL Parameter Route ----------------
@app.route("/hello/<name>")
def hello(name):
    return f"<h3>Hello {name} 🙌</h3>"

# ---------------- URL Params Multiple ----------------
@app.route("/add/<int:a>/<int:b>")
def add(a, b):
    return f"Sum = {a + b}"

# ---------------- GET + POST FORM ----------------
@app.route("/form", methods=["GET", "POST"])
def form():
    # By default show the form. After POST, show the greeting below the same form.
    username = ""
    form_data = ""
    if request.method == "POST":
        username = request.form.get("username", "")
        # show submitted form data for debugging/learning
        form_data = dict(request.form)
    return render_template("form.html", username=username, form_data=form_data)


# @app.route("/json", methods=["GET", "POST"])
# def show_form_json():
#     """Render the submitted form as pretty JSON on a page.

#     - Uses `request.form.to_dict(flat=False)` to preserve repeated fields as lists.
#     - Presents a pretty-printed JSON string in a `<pre>` block for readability.
#     """
#     form_json = ""
#     if request.method == "POST":
#         # preserve lists for repeated fields (checkboxes, multi-selects)
#         data = request.form.to_dict(flat=False)
#         form_json = json.dumps(data, indent=2, ensure_ascii=False)
#     return render_template("show_form_json.html", form_json=form_json)


@app.route("/lcm", methods=["GET", "POST"])
def calculate_lcm():
    def LCM(num: int):
        rows = []
        div = 2
        while num != 1:
            if num % div == 0:
                rows.append((div, num))
                num //= div
            else:
                div += 1
        rows.append(('', num))
        return rows

    rows = []
    if request.method == 'POST':
        try:
            n = int(request.form.get('LCM', ''))
            rows = LCM(n)
        except ValueError:
            rows = []


    return render_template("LCM.html", rows=rows)

if __name__ == "__main__":
    # Development server — use `flask run` or a production server for deployment
    app.run(debug=True, host="127.0.0.1", port=5000)

