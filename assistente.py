#!/usr/bin/env python3
"""
Assistente de Voz Inteligente
Um projeto que combina reconhecimento de fala com IA para conversas naturais

Desenvolvido para o bootcamp DIO - Abril/2026
"""

import os
import sys
import time
from pathlib import Path

try:
    import openai
    from gtts import gTTS
    import speech_recognition as sr
    import pygame
    from dotenv import load_dotenv
except ImportError as e:
    print(f"Opa, parece que falta alguma biblioteca: {e}")
    print("Rode primeiro: pip install -r requirements.txt")
    sys.exit(1)

# Carrega as configurações do arquivo .env
load_dotenv()

class AssistenteVoz:
    """
    Assistente pessoal que entende voz e responde de forma natural.
    Combina tecnologias da OpenAI com síntese de voz do Google.
    """
    
    def __init__(self, idioma='pt'):
        self.idioma = idioma
        self.ouvindo = False
        self.modo_voz_ativo = True
        
        # Configura o reconhecedor de fala
        self.rec = sr.Recognizer()
        self.mic = sr.Microphone()
        
        print("\nIniciando o assistente...")
        print("Calibrando microfone para o ambiente (aguarde 2 segundos)")
        
        with self.mic as source:
            self.rec.adjust_for_ambient_noise(source, duration=2)
            
        print("Pronto! Pode falar.\n")
        
    def escutar(self):
        """Captura áudio do microfone e converte para texto"""
        print("Ouvindo...", end=" ", flush=True)
        
        with self.mic as source:
            try:
                audio = self.rec.listen(source, timeout=10, phrase_time_limit=8)
            except sr.WaitTimeoutError:
                print("(silêncio)")
                return None
                
        print("(processando...)")
        
        # Salva temporariamente para enviar ao Whisper
        import tempfile
        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp:
            tmp.write(audio.get_wav_data())
            tmp_path = tmp.name
        
        try:
            # Usa a IA da OpenAI para entender o que foi dito
            with open(tmp_path, 'rb') as f:
                resultado = openai.Audio.transcribe("whisper-1", f)
            
            texto = resultado['text'].strip()
            if texto:
                print(f"Voce disse: {texto}")
            
            os.remove(tmp_path)
            return texto
            
        except Exception as e:
            print(f"Não consegui entender direito: {e}")
            os.remove(tmp_path)
            return None
    
    def pensar(self, mensagem):
        """Envia a mensagem para o ChatGPT e recebe a resposta"""
        if not mensagem:
            return None
            
        print("Pensando...", end=" ", flush=True)
        
        try:
            resposta = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Você é um assistente amigável e prestativo que conversa de forma natural e descontraída em português brasileiro. Respostas curtas e diretas, mas sempre cordiais."},
                    {"role": "user", "content": mensagem}
                ],
                max_tokens=200,
                temperature=0.8
            )
            
            texto = resposta.choices[0].message.content.strip()
            print("ok")
            print(f"Assistente: {texto}\n")
            return texto
            
        except Exception as e:
            print(f"Ops, deu algum problema: {e}")
            return "Desculpa, minha cabeça deu uma travada aqui. Pode repetir?"
    
    def falar(self, texto):
        """Converte o texto em áudio e reproduz"""
        if not texto or not self.modo_voz_ativo:
            return
            
        try:
            # Cria o áudio usando o Google TTS
            tts = gTTS(text=texto, lang=self.idioma, slow=False)
            
            # Salva temporariamente
            import tempfile
            with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as tmp:
                arquivo_audio = tmp.name
            
            tts.save(arquivo_audio)
            
            # Reproduz o áudio
            pygame.mixer.init()
            pygame.mixer.music.load(arquivo_audio)
            pygame.mixer.music.play()
            
            # Aguarda terminar
            while pygame.mixer.music.get_busy():
                time.sleep(0.1)
            
            # Limpa os recursos
            pygame.mixer.quit()
            os.remove(arquivo_audio)
            
        except Exception as e:
            print(f"[Não consegui falar: {e}]")
    
    def executar(self):
        """Loop principal do assistente"""
        print("=" * 50)
        print("Assistente de Voz - Bootcamp DIO")
        print("=" * 50)
        print("\nDicas:")
        print("  • Fale naturalmente, não precisa ser formal")
        print("  • Digite 'texto' para desativar a voz")
        print("  • Digite 'voz' para voltar a falar")
        print("  • Diga 'tchau' para encerrar")
        print("-" * 55 + "\n")
        
        # Saudação inicial
        saudacao = "Oi! Tudo bem? Estou aqui pra ajudar. O que você precisa?"
        print(f"🤖 Assistente: \"{saudacao}\"")
        self.falar(saudacao)
        
        while True:
            # Captura o que foi dito
            entrada = self.escutar()
            
            if not entrada:
                continue
            
            # Comandos especiais
            entrada_lower = entrada.lower()
            
            if entrada_lower in ['tchau', 'até logo', 'adeus', 'sair', 'exit']:
                despedida = "Tchau! Foi ótimo conversar com você. Até a próxima!"
                print(f"🤖 Assistente: \"{despedida}\"")
                self.falar(despedida)
                break
                
            elif 'modo texto' in entrada_lower or entrada_lower == 'texto':
                self.modo_voz_ativo = False
                print("🔇 Modo texto ativado (sem voz)")
                continue
                
            elif 'modo voz' in entrada_lower or entrada_lower == 'voz':
                self.modo_voz_ativo = True
                print("🔊 Modo voz ativado")
                msg = "Pronto, agora posso falar de novo!"
                print(f"🤖 Assistente: \"{msg}\"")
                self.falar(msg)
                continue
            
            # Processa a mensagem normalmente
            resposta = self.pensar(entrada)
            
            if resposta:
                self.falar(resposta)


def verificar_configuracao():
    """Verifica se a API key está configurada"""
    api_key = os.getenv('OPENAI_API_KEY')
    
    if not api_key:
        print("\n⚠️  Atenção!")
        print("Você precisa configurar sua API key da OpenAI.")
        print("\nCrie um arquivo chamado '.env' na mesma pasta com:")
        print("OPENAI_API_KEY=sua_chave_aqui")
        print("\nOu execute no terminal:")
        print("export OPENAI_API_KEY='sua_chave_aqui'")
        print("\nPara obter uma chave: https://platform.openai.com/api-keys")
        return False
    
    return True


def main():
    """Ponto de entrada do programa"""
    if not verificar_configuracao():
        sys.exit(1)
    
    try:
        assistente = AssistenteVoz()
        assistente.executar()
        
    except KeyboardInterrupt:
        print("\n\nEncerrando... Até logo! 👋")
    except Exception as e:
        print(f"\n❌ Ops, algo deu errado: {e}")
        print("Tente rodar novamente ou verifique sua conexão.")


if __name__ == "__main__":
    main()
