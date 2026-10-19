# Visão Computacional — Inova Trônica

## Objetivo

Desenvolver uma aplicação web integrada ao Microsoft Azure AI Vision / Computer Vision, capaz de analisar imagens a partir de uma URL e apresentar uma descrição automática do conteúdo, o nível de confiança e as principais tags identificadas.

## Tecnologias utilizadas

- Python 3
- Flask
- Microsoft Azure AI Vision / Computer Vision
- Azure Cognitive Services
- HTML e CSS

## Funcionalidades

- Entrada de uma URL de imagem.
- Análise automática da imagem utilizando o Azure Computer Vision.
- Exibição da descrição gerada pelo serviço.
- Apresentação do nível de confiança da descrição.
- Identificação das principais tags relacionadas à imagem.

## Como executar

### 1. Clonar o repositório

```bash
git clone https://github.com/jubsfreitas/app-visao-inova.git
cd app-visao-inova
```

### 2. Criar e ativar o ambiente virtual

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 4. Configurar as credenciais do Azure

Crie um arquivo `.env` na raiz do projeto com as variáveis abaixo:

```env
VISION_ENDPOINT=SEU_ENDPOINT
VISION_KEY=SUA_CHAVE
```

Substitua os valores pelos dados do recurso Computer Vision criado no Azure. Não compartilhe esse arquivo nem envie suas credenciais ao GitHub.

### 5. Iniciar a aplicação

```bash
python3 app.py
```

Acesse o endereço local informado pelo Flask no terminal. Na página, insira a URL de uma imagem e clique em **Analisar imagem** para visualizar os resultados.

## Repositório

[GitHub — app-visao-inova](https://github.com/jubsfreitas/app-visao-inova)

## Observação

A análise depende da disponibilidade do serviço Azure Computer Vision, de credenciais válidas e de uma URL de imagem acessível pelo serviço.
