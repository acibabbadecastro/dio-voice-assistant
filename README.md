# Assistente de Voz com IA

Projeto do bootcamp DIO - Assistente que ouve, entende e responde por voz usando ChatGPT + Whisper + gTTS.

## Arquivos

- `assistente.py` - Código principal (execute este)
- `requirements.txt` - Dependências para instalar
- `README.md` - Esta documentação

## Como usar

### 1. Instale as dependências
```bash
pip install -r requirements.txt
```

### 2. Configure sua API Key
Crie um arquivo `.env` na mesma pasta com:
```
OPENAI_API_KEY=sua_chave_aqui
```

Ou obtenha uma chave gratuita em: https://platform.openai.com/api-keys

### 3. Execute
```bash
python assistente.py
```

Fale algo quando aparecer "Ouvindo..."

## Tecnologias

- **Whisper (OpenAI)** - Reconhecimento de voz
- **ChatGPT** - Processamento de linguagem
- **gTTS** - Síntese de voz

---

*Projeto desenvolvido durante o bootcamp DIO - Abril/2026*
