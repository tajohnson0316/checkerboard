from flask import Flask, render_template

application = Flask(__name__)


@application.route("/")
def landing():
    return render_template(
        "index.html", primary_color="red", accent_color="black", rows=8, columns=8
    )


@application.route("/<int:rows>")
def board_with_rows(rows):
    return render_template(
        "index.html", primary_color="red", accent_color="black", rows=rows, columns=8
    )


@application.route("/<int:rows>/<int:columns>")
def board_with_rows_and_columns(rows, columns):
    return render_template(
        "index.html",
        primary_color="red",
        accent_color="black",
        rows=rows,
        columns=columns,
    )


@application.route("/<int:rows>/<int:columns>/<string:primary_color>")
def rows_columns_primary(rows, columns, primary_color):
    return render_template(
        "index.html",
        primary_color=primary_color,
        accent_color="black",
        rows=rows,
        columns=columns,
    )


@application.route(
    "/<int:rows>/<int:columns>/<string:primary_color>/<string:accent_color>"
)
def rows_columns_primary_accent(rows, columns, primary_color, accent_color):
    return render_template(
        "index.html",
        primary_color=primary_color,
        accent_color=accent_color,
        rows=rows,
        columns=columns,
    )


if __name__ == "__main__":
    application.run(debug=True, port=5000)
