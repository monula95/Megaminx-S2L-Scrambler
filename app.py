from flask import Flask, jsonify
import mega

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>Megaminx S2L Scrambler</title>
        </head>
        <body style="font-family: monospace;">
            <h1>Megaminx S2L Scrambler</h1>
            <button onclick="generate()">Generate Scramble</button>
            <pre id="output"></pre>

            <script>
                async function generate() {
                    const res = await fetch('/scramble');
                    const data = await res.json();
                    document.getElementById('output').textContent = data.scramble;
                }
            </script>
        </body>
    </html>
    """

@app.route("/scramble")
def get_scramble():
    return jsonify({
        "scramble": mega.scramble(49)
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
