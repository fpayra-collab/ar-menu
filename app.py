from flask import Flask, render_template, abort

app = Flask(__name__)

DISHES = {
    "burger": {
        "slug": "burger",
        "name": "Signature Burger",
        "glb": "https://drive.google.com/uc?export=download&id=172b0p2P9wbCHkH9Blbla6h2MMfFzrHVf",
        "usdz": "https://drive.google.com/uc?export=download&id=1i-Evet1pokp9AUuTBN6wGberm-yXcwfR",  # optional for iPhone
        "scale": "0.2 0.2 0.2",
    },
    "momo": {
        "slug": "momo",
        "name": "Momos",
        "glb": "https://drive.google.com/uc?export=download&id=1crOsN0blLGS5lEknDzPv-SkxdMP1Gpwm",
        "usdz": "https://drive.google.com/uc?export=download&id=1ezWmxqnx6rJbiKag-y5cZONAMBXxXJbm",
        "scale": "0.18 0.18 0.18",
    },
    "wrap": {
        "slug": "wrap",
        "name": "Wrap",
        "glb": "https://drive.google.com/uc?export=download&id=1ROEfo8NvbHs1FpXeteXVYpyKWZt804nE",
        "usdz": "https://drive.google.com/file/d/1tpTfNF9sGTFPBqM8GmJAIPNEJovpGy81/view?usp=sharing",
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
