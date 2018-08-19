from . import admin


@admin.route("/")
def index():
    return "<h1 style='color:green;'>This is admin</h1>"
