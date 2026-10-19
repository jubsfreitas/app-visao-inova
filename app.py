import os
from flask import Flask, request, render_template_string
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Inova Trônica | Visão Computacional</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #f2f5fa;
            color: #24324a;
            margin: 0;
            padding: 40px 20px;
        }
        main {
            max-width: 700px;
            margin: auto;
            background: white;
            padding: 35px;
            border-radius: 16px;
            box-shadow: 0 5px 20px #0001;
        }
        h1 { color: #1769aa; }
        input {
            box-sizing: border-box;
            width: 100%;
            padding: 12px;
            margin: 15px 0;
        }
        button {
            background: #1769aa;
            color: white;
            border: 0;
            padding: 12px 22px;
            border-radius: 8px;
            cursor: pointer;
        }
        .resultado {
            margin-top: 25px;
            padding: 18px;
            background: #edf7ff;
            border-radius: 10px;
        }
        img { max-width: 100%; margin-top: 15px; border-radius: 8px; }
        .erro { color: #b42318; }
    </style>
</head>
<body>
<main>
    <h1>Inova Trônica</h1>
    <h2>Monitoramento por Visão Computacional</h2>
    <p>Insira o endereço de uma imagem para receber uma descrição automática.</p>
    <form method="post">
        <label for="url">URL da imagem:</label>
        <input id="url" name="url" type="url"
               placeholder="https://exemplo.com/imagem.jpg"
               value="{{ url }}" required>
        <button type="submit">Analisar imagem</button>
    </form>
    {% if descricao %}
    <section class="resultado">
        <h3>Resultado da análise</h3>
        <p><strong>Descrição:</strong> {{ descricao }}</p>
        {% if confianca is not none %}
        <p><strong>Confiança:</strong> {{ "%.2f"|format(confianca * 100) }}%</p>
        {% endif %}
        <img src="{{ url }}" alt="Imagem analisada">
        {% if tags %}
        <p><strong>Tags:</strong> {{ tags|join(", ") }}</p>
        {% endif %}
    </section>
    {% endif %}
    {% if erro %}
    <p class="erro">{{ erro }}</p>
    {% endif %}
</main>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    url = ""
    descricao = None
    confianca = None
    tags = []
    erro = None

    if request.method == "POST":
        url = request.form.get("url", "").strip()
        endpoint = os.getenv("VISION_ENDPOINT")
        chave = os.getenv("VISION_KEY")

        if not endpoint or not chave:
            erro = "Configure as credenciais do Azure antes de analisar imagens."
        else:
            try:
                cliente = ComputerVisionClient(
                    endpoint, CognitiveServicesCredentials(chave)
                )
                resultado = cliente.analyze_image(
                    url,
                    visual_features=["Description", "Tags"]
                )

                if resultado.description.captions:
                    legenda = resultado.description.captions[0]
                    descricao = legenda.text
                    confianca = legenda.confidence
                else:
                    descricao = "Nenhuma descrição automática foi encontrada."

                tags = [tag.name for tag in (resultado.tags or [])[:10]]

            except Exception:
                erro = (
                    "Não foi possível analisar a imagem. "
                    "Verifique a URL e as configurações do Azure."
                )

    return render_template_string(
        HTML, url=url, descricao=descricao,
        confianca=confianca, tags=tags, erro=erro
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "8000")))
