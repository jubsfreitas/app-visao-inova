import os

from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials


ENDPOINT = os.environ["VISION_ENDPOINT"]
KEY = os.environ["VISION_KEY"]


def analisar_imagem(url):
    cliente = ComputerVisionClient(
        ENDPOINT,
        CognitiveServicesCredentials(KEY)
    )

    resultado = cliente.analyze_image(
        url,
        visual_features=[
            VisualFeatureTypes.description,
            VisualFeatureTypes.tags
        ]
    )

    print("\n========== RESULTADO ==========")

    if resultado.description and resultado.description.captions:
        descricao = resultado.description.captions[0]
        print(f"Descrição: {descricao.text}")
        print(f"Confiança: {descricao.confidence:.2%}")
    else:
        print("Não foi possível gerar uma descrição.")

    if resultado.tags:
        print("\nTags identificadas:")
        print(", ".join(tag.name for tag in resultado.tags[:10]))

    print("===============================\n")


if __name__ == "__main__":
    print("======================================")
    print("     VISÃO COMPUTACIONAL - INOVA")
    print("======================================")

    imagem = input("\nCole a URL de uma imagem: ").strip()

    if imagem:
        print("\nAnalisando imagem...")
        analisar_imagem(imagem)
    else:
        print("Nenhuma imagem foi informada.")

