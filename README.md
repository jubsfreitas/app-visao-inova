# Visão Computacional - Inova Trônica

Projeto desenvolvido para integração com o Azure AI Vision / Computer Vision.

## Objetivo

Enviar uma imagem por URL para o serviço Computer Vision da Microsoft Azure e obter uma descrição automática da imagem, além das principais tags identificadas.

## Tecnologias

- Python 3
- Microsoft Azure AI Vision / Computer Vision
- Azure Cognitive Services
- Pillow

## Como executar

### 1. Criar o ambiente virtual

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
export VISION_ENDPOINT="SEU_ENDPOINT"
export VISION_KEY="SUA_CHAVE"
python3 app.py

