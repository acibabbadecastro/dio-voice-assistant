# Assistente de Voz com IA

Oi! Esse projeto nasceu durante o bootcamp da DIO. É um assistente que ouve você falar, entende o que disse e responde em voz alta. Tudo isso usando inteligência artificial de verdade.

## Como funciona

Você fala algo → o sistema transforma sua voz em texto → a IA (ChatGPT) pensa numa resposta → o sistema fala a resposta em voz alta. Tudo acontece em segundos.

## Duas formas de usar

### 1. No seu computador (Python)

Roda local, sem depender de navegador.

```bash
# Instala o que precisa
pip install -r requirements.txt

# Roda o assistente
python assistente.py
```

Pronto, é só falar quando ele pedir.

### 2. No Google Colab (Python + JavaScript)

Quer testar sem instalar nada? Abre o notebook `assistente_colab.ipynb` no Colab. Lá a gente usa JavaScript para acessar o microfone do navegador e Python para fazer a mágica acontecer.

## Configuração rápida

Você precisa de uma API Key da OpenAI (é grátis pra começar):

1. Entra em https://platform.openai.com/api-keys
2. Cria uma conta (rapidinho)
3. Gera uma nova key
4. Cria um arquivo `.env` na pasta do projeto e coloca:
   ```
   OPENAI_API_KEY=sua_chave_aqui
   ```

## O que está por baixo

- **Whisper** (OpenAI): transforma sua fala em texto
- **ChatGPT**: pensa na melhor resposta
- **gTTS** (Google): transforma a resposta em voz

## Sobre

Feito com carinho durante o bootcamp DIO.

*Abril/2026*
