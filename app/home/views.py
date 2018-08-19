from . import home


@home.route("/")
def index():
    return "<h1 style='color:red;'>This is home</h1>"
