#!/usr/bin/env python3
"""
DIO Bootcamp - Assistente de Voz com ChatGPT
Tecnologias: Whisper (OpenAI) + ChatGPT + gTTS (Google TTS)
Autor: Acib ABBADE
Data: 2026-04-19
"""

import os
import openai
from gtts import gTTS
import speech_recognition as sr
import pygame
import tempfile
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

# Configurar API OpenAI
openai.api_key = os.getenv('OPENAI_API_KEY')

class VoiceAssistant:
    """Assistente virtual com conversação por voz usando ChatGPT + Whisper + gTTS"""
    
    def __init__(self, language='pt-br'):
        self.language = language
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        
        # Ajustar para ruído ambiente
        print("🎤 Calibrando microfone... Aguarde...")
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source, duration=2)
        print("✅ Microfone calibrado!")
    
    def listen(self):
        """Ouvir áudio do microfone e converter para texto usando Whisper"""
        print("\n🎤 Ouvindo... (fale agora)")
        
        with self.microphone as source:
            audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=10)
        
        # Salvar áudio temporariamente
        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp_audio:
            temp_audio.write(audio.get_wav_data())
            temp_audio_path = temp_audio.name
        
        try:
            # Usar Whisper para transcrever
            with open(temp_audio_path, 'rb') as audio_file:
                transcript = openai.Audio.transcribe("whisper-1", audio_file)
            
            text = transcript['text'].strip()
            print(f"📝 Você disse: {text}")
            
            # Limpar arquivo temporário
            os.unlink(temp_audio_path)
            
            return text
            
        except Exception as e:
            print(f"❌ Erro na transcrição: {e}")
            os.unlink(temp_audio_path)
            return None
    
    def ask_gpt(self, question):
        """Enviar pergunta para ChatGPT e obter resposta"""
        try:
            print("🤖 Pensando...")
            
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Você é um assistente útil e amigável que responde em português brasileiro de forma natural e conversacional."},
                    {"role": "user", "content": question}
                ],
                max_tokens=150,
                temperature=0.7
            )
            
            answer = response.choices[0].message.content.strip()
            print(f"💬 Resposta: {answer}")
            return answer
            
        except Exception as e:
            print(f"❌ Erro ao consultar ChatGPT: {e}")
            return "Desculpe, não consegui processar sua pergunta agora."
    
    def speak(self, text):
        """Converter texto em fala usando gTTS (Google Text-to-Speech)"""
        try:
            print("🔊 Gerando áudio...")
            
            # Criar arquivo de áudio temporário
            tts = gTTS(text=text, lang=self.language[:2], slow=False)
            
            with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as temp_mp3:
                temp_path = temp_mp3.name
            
            tts.save(temp_path)
            
            # Reproduzir áudio
            pygame.mixer.init()
            pygame.mixer.music.load(temp_path)
            pygame.mixer.music.play()
            
            # Aguardar término
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
            
            # Limpar
            pygame.mixer.quit()
            os.unlink(temp_path)
            
        except Exception as e:
            print(f"❌ Erro ao gerar áudio: {e}")
    
    def run(self):
        """Loop principal do assistente"""
        print("=" * 50)
        print("🤖 ASSISTENTE DE VOZ DIO - ChatGPT + Whisper + gTTS")
        print("=" * 50)
        print("\nComandos disponíveis:")
        print("- Diga 'sair' ou 'tchau' para encerrar")
        print("- Diga 'modo texto' para desativar voz")
        print("- Diga 'modo voz' para reativar voz\n")
        
        modo_voz = True
        
        while True:
            # Ouvir pergunta
            text = self.listen()
            
            if not text:
                continue
            
            # Verificar comandos especiais
            if text.lower() in ['sair', 'tchau', 'até logo', 'adeus']:
                print("👋 Encerrando assistente... Até logo!")
                if modo_voz:
                    self.speak("Até logo! Foi um prazer conversar com você.")
                break
            
            if 'modo texto' in text.lower():
                modo_voz = False
                print("🔇 Modo texto ativado.")
                continue
            
            if 'modo voz' in text.lower():
                modo_voz = True
                print("🔊 Modo voz ativado.")
                continue
            
            # Consultar ChatGPT
            answer = self.ask_gpt(text)
            
            # Responder por voz (se ativado)
            if modo_voz:
                self.speak(answer)


def main():
    """Função principal"""
    # Verificar se API key está configurada
    if not os.getenv('OPENAI_API_KEY'):
        print("❌ ERRO: OPENAI_API_KEY não encontrada!")
        print("\nCrie um arquivo .env com:")
        print("OPENAI_API_KEY=sua_chave_aqui")
        print("\nOu exporte a variável:")
        print("export OPENAI_API_KEY='sua_chave_aqui'")
        return
    
    try:
        assistant = VoiceAssistant()
        assistant.run()
    except KeyboardInterrupt:
        print("\n\n👋 Assistente encerrado pelo usuário.")
    except Exception as e:
        print(f"\n❌ Erro: {e}")


if __name__ == "__main__":
    main()
