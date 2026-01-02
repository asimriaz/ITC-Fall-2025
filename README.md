## eBooks
1. Flask Web Development by Miguel Grinberg [source code](https://github.com/miguelgrinberg/flasky)
2. Mastering Flask Web  and API Development by Sherwin John C. Tragura [source code](https://github.com/PacktPublishing/Mastering-Flask-Web-Development)


### Installation

Use curl to download the script and execute it with sh:

```sh
curl -LsSf https://astral.sh/uv/install.sh | sh
```
If your system doesn't have curl, you can use wget:

```sh
wget -qO- https://astral.sh/uv/install.sh | sh
```
type `uv` and press `Enter`

```
An extremely fast Python package manager.

Usage: uv [OPTIONS] <COMMAND>

Commands:
  auth     Manage authentication
  run      Run a command or script
  init     Create a new project
  add      Add dependencies to the project
  remove   Remove dependencies from the project
  version  Read or update the project's version
  sync     Update the project's environment
  lock     Update the project's lockfile
  export   Export the project's lockfile to an alternate format
  tree     Display the project's dependency tree
  format   Format Python code in the project
  tool     Run and install commands provided by Python packages
  python   Manage Python versions and installations
  pip      Manage Python packages with a pip-compatible interface
  venv     Create a virtual environment
  build    Build Python packages into source distributions and wheels
  publish  Upload distributions to an index
  cache    Manage uv's cache
  self     Manage the uv executable
  help     Display documentation for a command

Cache options:
  -n, --no-cache               Avoid reading from or writing to the cache, instead using a temporary directory for the duration of the operation [env: UV_NO_CACHE=]
      --cache-dir <CACHE_DIR>  Path to the cache directory [env: UV_CACHE_DIR=]

Python options:
      --managed-python       Require use of uv-managed Python versions [env: UV_MANAGED_PYTHON=]
      --no-managed-python    Disable use of uv-managed Python versions [env: UV_NO_MANAGED_PYTHON=]
      --no-python-downloads  Disable automatic downloads of Python. [env: "UV_PYTHON_DOWNLOADS=never"]

Global options:
  -q, --quiet...                                   Use quiet output
  -v, --verbose...                                 Use verbose output
      --color <COLOR_CHOICE>                       Control the use of color in output [possible values: auto, always, never]
      --native-tls                                 Whether to load TLS certificates from the platform's native certificate store [env: UV_NATIVE_TLS=]
      --offline                                    Disable network access [env: UV_OFFLINE=]
      --allow-insecure-host <ALLOW_INSECURE_HOST>  Allow insecure connections to a host [env: UV_INSECURE_HOST=]
      --no-progress                                Hide all progress outputs [env: UV_NO_PROGRESS=]
      --directory <DIRECTORY>                      Change to the given directory prior to running the command [env: UV_WORKING_DIRECTORY=]
      --project <PROJECT>                          Run the command within the given project directory [env: UV_PROJECT=]
      --config-file <CONFIG_FILE>                  The path to a `uv.toml` file to use for configuration [env: UV_CONFIG_FILE=]
      --no-config                                  Avoid discovering configuration files (`pyproject.toml`, `uv.toml`) [env: UV_NO_CONFIG=]
  -h, --help                                       Display the concise help for this command
  -V, --version                                    Display the uv version

Use `uv help` for more details.
```

initialize Flask Project

```sh
uv init app-1
```

install packages

```sh
uv add flask requests
```

check package installation 


<pre style="line-height: 1.15;">
$ uv tree
Resolved 14 packages in 0.55ms
app-1 v0.1.0
├── flask v3.1.2
│   ├── blinker v1.9.0
│   ├── click v8.3.1
│   ├── itsdangerous v2.2.0
│   ├── jinja2 v3.1.6
│   │   └── markupsafe v3.0.3
│   ├── markupsafe v3.0.3
│   └── werkzeug v3.1.3
│       └── markupsafe v3.0.3
└── requests v2.32.5
    ├── certifi v2025.11.12
    ├── charset-normalizer v3.4.4
    ├── idna v3.11
    └── urllib3 v2.5.0
</pre>

Edit main.py

```py
import sys
def main():
    print(sys.executable)


if __name__ == "__main__":
    main()
```


```sh
$ uv run main.py
/home/asim-riaz/Flask/app-1/.venv/bin/python3
```

```sh
$ rm -rf .venv/

$ uv run main.py 
Using CPython 3.12.3 interpreter at: /usr/bin/python3.12
Creating virtual environment at: .venv
Installed 12 packages in 4ms
/home/asim-riaz/Flask/app-1/.venv/bin/python
```

```sh
$ uv sync
Resolved 14 packages in 0.47ms
Audited 12 packages in 0.10ms
```


This README documents the example routes in `main.py` and shows how each route works with code snippets and practical examples.

# Flask app tutorial (routes explained)
## Routes overview

- `/` — root route, returns a simple HTML welcome message (GET)
- `/hello/<name>` — path parameter route that greets a user by name
- `/add/<int:a>/<int:b>` — path parameter route with integer converters to add two numbers
- `/form` — demonstrates a simple GET/POST form using `render_template_string` and `request.form`

All examples below match the code in `main.py`.

---

src: `main.py`

```py
import flask
from flask import Flask, request, render_template_string 

app = Flask(__name__)

# ---------------- Root Route ----------------
@app.route("/")
def index():
    return "<h2>Welcome to Flask app using UV!</h2>"


if __name__ == "__main__":
    # Development server — use `flask run` or a production server for deployment
    app.run(debug=True, host="127.0.0.1", port=5000)


```



## Routes overview

- `/` — root route, returns a simple HTML welcome message (GET)
- `/hello/<name>` — path parameter route that greets a user by name
- `/add/<int:a>/<int:b>` — path parameter route with integer converters to add two numbers
- `/form` — demonstrates a simple GET/POST form using `render_template_string` and `request.form`

All examples below match the code in `main.py`.



#### 1) Root route — `/`

Code (from `main.py`):

```py
@app.route("/")
def index():
    return "<h2>Welcome to Flask app using UV!</h2>"
```

Explanation:
- `@app.route("/")`: registers the function `index` for HTTP GET requests to the root path `/`.
- The function returns an HTML string which Flask will send to the client with status code `200`.

Practical test (browser or curl):

```sh
curl http://127.0.0.1:5000/
```

---

**2) Greeting route — `/hello/<name>`**

Code:

```py
@app.route("/hello/<name>")
def hello(name):
    return f"<h3>Hello {name} 🙌</h3>"
```

Explanation:
- `<name>` is a path parameter (string by default). When a request comes to `/hello/Alex`, Flask calls `hello('Alex')`.
- The function returns a formatted greeting string.

Practical test:

```sh
curl http://127.0.0.1:5000/hello/Alex
```

---

**3) Add two numbers — `/add/<int:a>/<int:b>`**

Code:

```py
@app.route("/add/<int:a>/<int:b>")
def add(a, b):
    return f"Sum = {a + b}"
```

Explanation:
- `int:` is a converter that ensures the path components are parsed as integers. If a non-integer is passed, Flask will return a 404.
- The function receives `a` and `b` as integers and returns their sum in a string.

Practical test:

```sh
curl http://127.0.0.1:5000/add/4/5
# Response: Sum = 9
```

---

**4) Simple form submission — `/form` (GET + POST)**

Code (simplified from `main.py`):

```py
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
```

Explanation:
- `methods=["GET","POST"]` tells Flask to accept both GET and POST on this route.
- On `GET`, we return an HTML form rendered from the `form_html` string using `render_template_string`.
- On `POST`, `request.form` contains form-encoded data; `request.form.get('username')` retrieves the submitted value.

Practical test (browser):
- Open `http://127.0.0.1:5000/form`, fill the input and submit.

Practical test (curl):

```sh
curl -X POST -d "username=Alice" http://127.0.0.1:5000/form
# Response: <h2>Form Submitted → Welcome Alice</h2>
```

Security note: This is a minimal example for learning. For real apps use CSRF protection (for example via Flask-WTF) and validate/sanitize input.

---

## Running the app (development)

The `main.py` file includes a development entrypoint. Example snippet in `main.py`:

```py
if __name__ == "__main__":
    # Development server — use `flask run` or a production server for deployment
    app.run(debug=True, host="127.0.0.1", port=5000)
```

Explanation:
- `app.run(...)` starts Flask's built-in development server. `debug=True` enables the debugger and auto-reload — do not enable this in production.
- `host="127.0.0.1"` binds the server to the loopback interface so it is only reachable locally. To make the server reachable on your LAN (for development only), set `host="0.0.0.0"`.

Start the app:

```sh
# run directly using uv (project's uv tool) if you have it configured:
uv run main.py
```

---

## Quick reference — HTTP methods used

- `GET` (default): retrieve resources, used by `/`, `/hello/<name>`, `/add/...`, and GET `/form`.
- `POST`: send data to the server, used here by `/form` to submit the form. Access submitted form data with `request.form`.

---

