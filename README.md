# Assistente de Voz com IA

Projeto DIO usando Python + JavaScript. Assistente que ouve, entende e responde por voz.

## Versões disponíveis

### 1. Local (Python puro)
Roda no seu computador, sem navegador.
- `assistente.py` - Código principal
- Execute: `python assistente.py`

### 2. Google Colab (Python + JavaScript)
Roda no navegador, usa JavaScript para acessar o microfone.
- `assistente_colab.ipynb` - Notebook para importar no Colab

## Instalação (versão local)

```bash
pip install -r requirements.txt
```

## Configuração

Crie um arquivo `.env` com sua API Key:
```
OPENAI_API_KEY=sua_chave_aqui
```

Ou obtenha em: https://platform.openai.com/api-keys

## Tecnologias

- **Python:** Processamento (Whisper, ChatGPT, gTTS)
- **JavaScript:** Gravação de áudio no navegador (Colab)

---

*Projeto DIO - Abril/2026*
