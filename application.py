from flask import Flask, request, redirect, render_template_string
import sqlite3

application = Flask(__name__)
DB = "/var/app/current/evently.db"

EVENTS = [
    (1, "Tech Innovation Summit", "Technology", "Explore emerging technologies and AI.", "2026-11-15"),
    (2, "Music & Cultural Fest", "Entertainment", "An evening of music and culture.", "2026-11-20"),
    (3, "Startup Connect", "Business", "Meet founders, innovators and investors.", "2026-11-25"),
    (4, "AI & Machine Learning Workshop", "Education", "Hands-on introduction to modern AI.", "2026-12-02"),
    (5, "Photography Exhibition", "Arts", "Discover creative photography.", "2026-12-08"),
    (6, "Entrepreneurship Meetup", "Business", "Network with aspiring entrepreneurs.", "2026-12-12")
]

def database():
    conn = sqlite3.connect(DB)
    conn.execute("""CREATE TABLE IF NOT EXISTS registrations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        event_id INTEGER NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )""")
    return conn

PAGE = """
<!DOCTYPE html>
<html>
<head>
<title>Evently | Discover Experiences</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body{margin:0;background:#f4f5fb;font-family:Arial;color:#20243a}
header{background:#171b36;color:white;padding:28px 8%;display:flex;justify-content:space-between}
header b{font-size:27px;color:#9d9aff}
.hero{padding:65px 8%;background:linear-gradient(120deg,#252953,#6654a8);color:white}
.hero h1{font-size:42px;margin:0 0 12px}
main{padding:35px 8%}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:20px}
.card{background:white;padding:24px;border-radius:14px;box-shadow:0 5px 20px #20243a12}
.tag{color:#6654a8;font-weight:bold}
button{background:#6654a8;color:white;border:0;padding:12px 20px;border-radius:8px;cursor:pointer}
input{display:block;width:95%;padding:12px;margin:12px 0;border:1px solid #ddd;border-radius:7px}
form{background:white;padding:25px;border-radius:14px;max-width:450px;margin:25px 0}
.notice{background:#e2f8e9;padding:15px;border-radius:8px}
footer{text-align:center;padding:30px;color:#777}
</style>
</head>
<body>
<header><b>✦ EVENTLY</b><span>Discover · Register · Experience</span></header>
<section class="hero">
<h1>Make Every Moment an Event.</h1>
<p>Discover exciting experiences. Find your people. Be there.</p>
</section>
<main>
<h2>Upcoming Events</h2>
<div class="grid">
{% for e in events %}
<div class="card">
<p class="tag">{{e[2]}}</p>
<h2>{{e[1]}}</h2>
<p>{{e[3]}}</p>
<p>📅 {{e[4]}}</p>
<a href="/register/{{e[0]}}"><button>Register Now</button></a>
</div>
{% endfor %}
</div>
{% if selected %}
<form method="POST" action="/register/{{selected[0]}}">
<h2>Register for {{selected[1]}}</h2>
{% if message %}<p class="notice">{{message}}</p>{% endif %}
<label>Full Name</label><input name="name" required maxlength="100">
<label>Email Address</label><input name="email" type="email" required maxlength="150">
<button type="submit">Confirm Registration</button>
</form>
{% endif %}
{% if success %}<p class="notice">{{success}}</p>{% endif %}
</main>
<footer>© 2026 Evently | Powered by AWS Elastic Beanstalk</footer>
</body>
</html>
"""

@application.route("/")
def home():
    return render_template_string(PAGE, events=EVENTS, selected=None, message=None, success=None)

@application.route("/register/<int:event_id>", methods=["GET", "POST"])
def register(event_id):
    event = next((e for e in EVENTS if e[0] == event_id), None)
    if not event:
        return "Event not found", 404
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        if not name or not email:
            return render_template_string(PAGE, events=EVENTS, selected=event, message="Please complete all fields.", success=None)
        with database() as conn:
            conn.execute("INSERT INTO registrations(name,email,event_id) VALUES(?,?,?)", (name,email,event_id))
        return render_template_string(PAGE, events=EVENTS, selected=None, message=None, success="Registration confirmed for " + event[1] + "!")
    return render_template_string(PAGE, events=EVENTS, selected=event, message=None, success=None)

@application.route("/health")
def health():
    return {"status": "healthy", "application": "Evently"}

if __name__ == "__main__":
    application.run(host="0.0.0.0", port=5000)
