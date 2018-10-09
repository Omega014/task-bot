from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

app.config['SECRET_KEY'] = 'omega014'
if __name__ == "__main__":
    app.run(port=5000, debug=True, threaded=True)
