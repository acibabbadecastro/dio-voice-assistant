# Assistente de Voz Inteligente

Um assistente pessoal que entende sua voz e responde de forma natural, combinando as melhores tecnologias de IA disponíveis.

> Projeto desenvolvido durante o bootcamp DIO - Explorando integração entre Speech-to-Text, processamento de linguagem natural e Text-to-Speech.

---

## O que ele faz?

- **Ouve você** - Capta sua voz e converte para texto usando a API Whisper da OpenAI
- **Entende e processa** - Usa o ChatGPT para gerar respostas inteligentes e contextuais
- **Responde em voz** - Transforma o texto em áudio usando Google TTS para uma conversa natural

Tudo em tempo real, direto no seu computador!

---

## Para Professores - Como Testar

**Atenção:** Para testar este projeto, você precisa de uma API Key da OpenAI.

### Passo a passo para criar sua API Key gratuita:

1. Acesse: https://platform.openai.com/api-keys
2. Crie uma conta (é gratuita e inclui créditos iniciais)
3. Clique em "Create new secret key"
4. Copie a chave gerada (começa com `sk-`)
5. Cole a chave no arquivo `.env` ou direto no código onde indicado

**Importante:** Cada pessoa deve usar sua própria API Key. Não compartilhe chaves.

### Links do Projeto:

- **Repositório:** https://github.com/acibabbadecastro/dio-voice-assistant
- **Notebook Colab:** https://colab.research.google.com/github/acibabbadecastro/dio-voice-assistant/blob/main/assistente_voz.ipynb

---

## Tecnologias Utilizadas

| Tecnologia | Função |
|------------|--------|
| **OpenAI Whisper** | Reconhecimento de fala de alta precisão |
| **OpenAI GPT-3.5** | Processamento de linguagem natural |
| **Google TTS (gTTS)** | Síntese de voz em português brasileiro |
| **SpeechRecognition** | Interface com o microfone |
| **Pygame** | Reprodução de áudio |

---

## Instalação

### Pré-requisitos
- Python 3.8 ou superior
- Microfone funcional
- Conexão com internet

### Passo a passo

1. **Clone o repositório**
```bash
git clone https://github.com/seu-usuario/dio-voice-assistant.git
cd dio-voice-assistant
```

2. **Crie um ambiente virtual** (recomendado)
```bash
python -m venv venv

# Windows:
venv\Scripts\activate

# Linux/Mac:
source venv/bin/activate
```

3. **Instale as dependências**
```bash
pip install -r requirements.txt
```

4. **Configure sua API Key**
```bash
# Crie um arquivo .env na pasta do projeto:
echo "OPENAI_API_KEY=sua_chave_aqui" > .env
```

> Onde conseguir a chave? Acesse [platform.openai.com/api-keys](https://platform.openai.com/api-keys) e crie uma chave gratuita (inclui créditos iniciais)

---

## Como usar

Execute o assistente:

```bash
python assistant.py
```

### Comandos disponíveis:

| Comando | Descrição |
|---------|-----------|
| Fale naturalmente | O assistente te responde em voz |
| `texto` | Desativa a resposta por voz (modo silencioso) |
| `voz` | Reativa a resposta por voz |
| `tchau` ou `sair` | Encerra o assistente |

---

## Exemplo de uso

```
Iniciando assistente...
Calibrando microfone para o ambiente (aguarde 2 segundos)
Pronto! Estou te ouvindo.

Ouvindo... (processando...)
Você: "Qual a capital do Brasil?"

Pensando... 
Assistente: "A capital do Brasil é Brasília."

[Resposta falada em voz alta]
```

---

## Estrutura do projeto

```
.
├── assistant.py              # Código principal do assistente
├── assistente_voz.ipynb      # Notebook para Google Colab
├── requirements.txt          # Dependências Python
├── .env.example             # Exemplo de configuração
├── .gitignore               # Arquivos ignorados pelo Git
├── README.md                # Este arquivo
├── INSTRUCOES_GITHUB.md     # Guia de publicação no GitHub
└── deploy_github.sh         # Script de deploy automatizado
```

---

## Personalização

Quer mudar o idioma ou ajustar algum comportamento? É simples:

```python
# No arquivo assistant.py, altere na inicialização:
assistente = AssistenteVoz(idioma='en')  # Para inglês
# ou
assistente = AssistenteVoz(idioma='es')  # Para espanhol
```

---

## Limitações

- Requer conexão com internet para funcionar
- A qualidade do reconhecimento depende do microfone
- Respostas limitadas a ~200 tokens (conversas curtas e objetivas)

---

## Licença

Este projeto foi desenvolvido para fins educacionais durante o bootcamp DIO.

Sinta-se livre para usar, modificar e distribuir!

---

## Autor

**Acib ABBADE**

Desenvolvido durante o bootcamp DIO - Abril/2026
