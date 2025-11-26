
import flask


from flask import Flask, request, render_template_string 

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
form_html = """
<form method="POST">
    <input name="username" placeholder="Enter Username">
    <button type="submit">Submit</button>
</form>
"""

@app.route("/form", methods=["GET","POST"])
def form():
    if request.method == "POST":
        user = request.form.get("username")
        return f"<h2>Form Submitted → Welcome {user}</h2>"
    return render_template_string(form_html)


if __name__ == "__main__":
    # Development server — use `flask run` or a production server for deployment
    app.run(debug=True, host="127.0.0.1", port=5000)

