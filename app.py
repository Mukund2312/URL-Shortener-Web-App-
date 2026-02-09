from flask import Flask, render_template, request, redirect, abort
from InputForm import InputForm
import secrets

app = Flask(__name__)
app.config['SECRET_KEY'] = "abc"

shortened_urls = {}

@app.route("/", methods=["GET", "POST"])
def home():
    form = InputForm()
    short_url = None

    if form.validate_on_submit():
        short_id = secrets.token_urlsafe(6)
        shortened_urls[short_id] = form.url_input.data
        short_url = request.host_url + short_id
        form.url_input.data = ""

    return render_template("index.html", form=form, short_url=short_url)


@app.route("/<short_id>")
def redirect_url(short_id):
    if short_id in shortened_urls:
        return redirect(shortened_urls[short_id])
    return abort(404)

if __name__ == "__main__":
    app.run(debug=True)
