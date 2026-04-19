#!/usr/bin/env python3
"""
Assistente de Voz com IA
Bootcamp DIO - Abril/2026
"""

import os
import sys
import time

try:
    import openai
    from gtts import gTTS
    import speech_recognition as sr
    import pygame
    from dotenv import load_dotenv
except ImportError as e:
    print(f"Opa, falta instalar alguma coisa: {e}")
    print("Rode: pip install -r requirements.txt")
    sys.exit(1)

load_dotenv()


class AssistenteVoz:
    def __init__(self, idioma='pt'):
        self.idioma = idioma
        self.modo_voz_ativo = True
        self.rec = sr.Recognizer()
        self.mic = sr.Microphone()
        
        print("\nIniciando...")
        print("Calibrando microfone (2 segundos)")
        
        with self.mic as source:
            self.rec.adjust_for_ambient_noise(source, duration=2)
            
        print("Pronto! Pode falar.\n")
        
    def ouvir(self):
        print("Ouvindo...", end=" ", flush=True)
        
        with self.mic as source:
            try:
                audio = self.rec.listen(source, timeout=10, phrase_time_limit=8)
            except sr.WaitTimeoutError:
                print("(silencio)")
                return None
                
        print("(processando)")
        
        import tempfile
        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp:
            tmp.write(audio.get_wav_data())
            tmp_path = tmp.name
        
        try:
            with open(tmp_path, 'rb') as f:
                resultado = openai.Audio.transcribe("whisper-1", f)
            
            texto = resultado['text'].strip()
            if texto:
                print(f"Voce: {texto}")
            
            os.remove(tmp_path)
            return texto
            
        except Exception as e:
            print(f"Nao entendi: {e}")
            os.remove(tmp_path)
            return None
    
    def pensar(self, mensagem):
        if not mensagem:
            return None
            
        print("Pensando...", end=" ", flush=True)
        
        try:
            resposta = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Voce e um assistente amigavel que conversa de forma natural em portugues brasileiro. Respostas curtas."},
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
            print(f"Erro: {e}")
            return "Desculpa, deu problema. Pode repetir?"
    
    def falar(self, texto):
        if not texto or not self.modo_voz_ativo:
            return
            
        try:
            tts = gTTS(text=texto, lang=self.idioma, slow=False)
            
            import tempfile
            with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as tmp:
                arquivo = tmp.name
            
            tts.save(arquivo)
            
            pygame.mixer.init()
            pygame.mixer.music.load(arquivo)
            pygame.mixer.music.play()
            
            while pygame.mixer.music.get_busy():
                time.sleep(0.1)
            
            pygame.mixer.quit()
            os.remove(arquivo)
            
        except Exception as e:
            print(f"[Erro ao falar: {e}]")
    
    def executar(self):
        print("=" * 40)
        print("Assistente de Voz - DIO")
        print("=" * 40)
        print("\nComandos:")
        print("  'texto' - modo silencioso")
        print("  'voz' - volta a falar")
        print("  'tchau' - encerra")
        print("-" * 40 + "\n")
        
        saudacao = "Oi! Tudo bem? Estou aqui pra ajudar."
        print(f"Assistente: {saudacao}")
        self.falar(saudacao)
        
        while True:
            entrada = self.ouvir()
            
            if not entrada:
                continue
            
            entrada_lower = entrada.lower()
            
            if entrada_lower in ['tchau', 'ate logo', 'adeus', 'sair']:
                despedida = "Tchau! Ate a proxima."
                print(f"Assistente: {despedida}")
                self.falar(despedida)
                break
                
            elif entrada_lower == 'texto':
                self.modo_voz_ativo = False
                print("Modo texto ativado.")
                continue
                
            elif entrada_lower == 'voz':
                self.modo_voz_ativo = True
                print("Modo voz ativado.")
                msg = "Pronto, posso falar de novo!"
                print(f"Assistente: {msg}")
                self.falar(msg)
                continue
            
            resposta = self.pensar(entrada)
            
            if resposta:
                self.falar(resposta)


def verificar_configuracao():
    api_key = os.getenv('OPENAI_API_KEY')
    
    if not api_key:
        print("\nAtençao!")
        print("Crie um arquivo .env com:")
        print("OPENAI_API_KEY=sua_chave_aqui")
        print("\nOu: export OPENAI_API_KEY='sua_chave'")
        print("Obtenha em: https://platform.openai.com/api-keys")
        return False
    
    return True


def main():
    if not verificar_configuracao():
        sys.exit(1)
    
    try:
        assistente = AssistenteVoz()
        assistente.executar()
        
    except KeyboardInterrupt:
        print("\n\nEncerrando... Ate logo!")
    except Exception as e:
        print(f"\nErro: {e}")


if __name__ == "__main__":
    main()
