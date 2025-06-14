from flask import Flask, render_template_string
import pandas as pd

app = Flask(__name__)

try:
    df = pd.read_pickle("proventos_b3.pkl")
except Exception as e:
    df = pd.DataFrame()
    print("Erro ao carregar dados locais:", e)

@app.route("/")
def index():
    if df.empty:
        return "<h1>Sem dados disponíveis.</h1>"
    html = df.head(10).to_html()
    return f"<h1>Proventos Recentes</h1>{html}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
