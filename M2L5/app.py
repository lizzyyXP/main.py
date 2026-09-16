from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/form")
def form():
    return render_template("form.html")


@app.route("/submit", methods=["POST"])
def submit_form():
    name = request.form["name"]
    email = request.form["email"]
    address = request.form["address"]
    date = request.form["date"]

    with open("form.txt", "a") as f:
        f.write(name + "\n")
        f.write(email + "\n")
        f.write(address + "\n")
        f.write(date + "\n")

    return render_template(
        "form_result.html",
        name=name,
        email=email,
        address=address,
        date=date
    )


if __name__ == "__main__":
    app.run(debug=True)