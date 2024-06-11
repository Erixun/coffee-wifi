from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from models import CafeForm
from utils import emoji
from csv import reader, writer


app = Flask(__name__)
app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
Bootstrap5(app)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/add", methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        row = []
        for key, value in form.data.items():
            if key in emoji.keys():
                value = emoji[key] * int(value)

            row.append(value)

        with open("cafe-data.csv", mode="a", newline="", encoding="utf-8") as csv_file:
            csv_writer = writer(csv_file, delimiter=",")
            csv_writer.writerow(row[:-2])

    return render_template("add.html", form=form)


@app.route("/cafes")
def cafes():
    with open("cafe-data.csv", newline="", encoding="utf-8") as csv_file:
        csv_data = reader(csv_file, delimiter=",")
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template("cafes.html", cafes=list_of_rows)


if __name__ == "__main__":
    app.run(debug=True)
