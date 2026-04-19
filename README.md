# 🤖 Assistente de Voz - ChatGPT + Whisper + gTTS

## 📋 Sobre o Projeto

Bootcamp DIO - Desenvolvimento de um assistente virtual completo que combina:
- **🎤 Speech-to-Text:** OpenAI Whisper para transcrição de voz
- **🧠 Processamento:** ChatGPT GPT-3.5 para geração de respostas
- **🔊 Text-to-Speech:** Google TTS (gTTS) para resposta por voz

## 🎯 Funcionalidades

✅ Reconhecimento de voz em tempo real
✅ Comunicação natural com ChatGPT
✅ Respostas por voz em português brasileiro
✅ Suporte a comandos de voz (modo texto/voz, sair)
✅ Tratamento de erros e exceções

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Função |
|------------|--------|
| OpenAI Whisper | Transcrição de áudio |
| OpenAI GPT-3.5 | Processamento de linguagem natural |
| Google TTS (gTTS) | Síntese de voz |
| SpeechRecognition | Captura de áudio do microfone |
| Pygame | Reprodução de áudio |

## 📦 Instalação

### 1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/dio-voice-assistant.git
cd dio-voice-assistant
```

### 2. Crie ambiente virtual (recomendado)
```bash
python -m venv venv

# Linux/Mac
source venv/bin/activate

# Windows
venv\Scripts\activate
```

### 3. Instale dependências
```bash
pip install -r requirements.txt
```

**Nota:** Se tiver problemas com PyAudio no Linux:
```bash
sudo apt-get install portaudio19-dev python3-pyaudio
```

### 4. Configure API Key
```bash
cp .env.example .env
```

Edite o arquivo `.env` e adicione sua chave da OpenAI:
```
OPENAI_API_KEY=sk-sua_chave_aqui
```

## 🚀 Como Executar

```bash
python assistant.py
```

## 💬 Comandos de Voz

| Comando | Ação |
|---------|------|
| "Sair", "Tchau" | Encerra o assistente |
| "Modo texto" | Desativa resposta por voz |
| "Modo voz" | Reativa resposta por voz |

## 📊 Fluxo de Funcionamento

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│  Microfone  │───▶│   Whisper   │───▶│   ChatGPT   │───▶│    gTTS     │
│  (Entrada)  │    │(Transcrever)│    │  (Responder)│    │  (Falar)    │
└─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘
```

## 🔧 Estrutura do Código

```
assistant.py          # Código principal
requirements.txt      # Dependências
.env.example          # Exemplo de variáveis de ambiente
README.md            # Documentação
```

## 📚 Recursos Adicionais

- [Documentação OpenAI](https://platform.openai.com/docs)
- [Documentação Whisper](https://platform.openai.com/docs/guides/speech-to-text)
- [Documentação gTTS](https://gtts.readthedocs.io/)

## 📝 Licença

Projeto desenvolvido para fins educacionais no Bootcamp DIO.

## 👤 Autor

**Acib ABBADE**
- GitHub: [@AcibAbbade](https://github.com/seu-usuario)
- LinkedIn: [linkedin.com/in/seu-perfil](https://linkedin.com/in/seu-perfil)

---

⭐ **Dica:** Experimente fazer perguntas complexas! O assistente entende contexto e mantém conversas naturais.
