from flask import Flask, render_template, abort

app = Flask(__name__)

DISHES = {
    "burger": {
        "slug": "burger",
        "name": "Signature Burger",
        "glb": "/static/models/burger.glb",
        "usdz": "/static/models/burger.usdz",  # optional for iPhone
        "scale": "0.2 0.2 0.2",
    },
    "momo": {
        "slug": "momo",
        "name": "Momos",
        "glb": "/static/models/momo.glb",
        "usdz": "/static/models/momo.usdz",
        "scale": "0.18 0.18 0.18",
    },
    "wrap": {
        "slug": "wrap",
        "name": "Wrap",
        "glb": "/static/models/wrap.glb",
        "usdz": "/static/models/wrap.usdz",
        "scale": "0.18 0.18 0.18",
    },
    # add more dishes...
}

@app.route("/dish/<slug>")
def dish(slug):
    dish = DISHES.get(slug)
    if not dish:
        abort(404)
    return render_template("dish.html", dish=dish)

@app.route("/menu/main")
def menu_main():
    # choose which dishes to include in this album
    dishes = [DISHES["burger"], DISHES["momo"], DISHES["wrap"]]
    return render_template("menu_album.html", dishes=dishes, title="Main Menu")




if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
