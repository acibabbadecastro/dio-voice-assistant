#!/bin/bash
# Script de deploy automático para GitHub
# Autor: Stark (para Acib)

set -e  # Para em caso de erro

REPO_NAME="dio-voice-assistant"
GITHUB_USER=""  # Preencher com seu usuário

echo "🚀 Deploy Automático para GitHub"
echo "================================"

# Verifica se está no diretório correto
if [ ! -f "assistant.py" ]; then
    echo "❌ Erro: Execute este script na pasta do projeto"
    exit 1
fi

# Pede o usuário do GitHub se não estiver configurado
if [ -z "$GITHUB_USER" ]; then
    read -p "Digite seu usuário do GitHub: " GITHUB_USER
fi

echo ""
echo "📋 Resumo do que será feito:"
echo "  - Usuário: $GITHUB_USER"
echo "  - Repositório: $REPO_NAME"
echo "  - Visibilidade: Público"
echo ""
read -p "Confirma? (s/n): " CONFIRM

if [ "$CONFIRM" != "s" ] && [ "$CONFIRM" != "S" ]; then
    echo "❌ Cancelado"
    exit 1
fi

# Configura Git
echo ""
echo "🔧 Configurando Git..."
git config user.email "acib@servmil.com.br" 2>/dev/null || true
git config user.name "Acib Abbade" 2>/dev/null || true

# Inicializa repositório se necessário
if [ ! -d ".git" ]; then
    echo "📦 Inicializando repositório Git..."
    git init
    git branch -M main
fi

# Adiciona todos os arquivos
echo "📁 Adicionando arquivos..."
git add .

# Commit
echo "💾 Criando commit..."
git commit -m "feat: Assistente de Voz com ChatGPT + Whisper + gTTS

Implementação completa do projeto do bootcamp DIO:
- Reconhecimento de voz via Whisper (OpenAI)
- Processamento de linguagem natural via ChatGPT
- Resposta por voz via Google TTS (gTTS)
- Interface conversacional natural e amigável

Tecnologias: Python, OpenAI API, SpeechRecognition, Pygame" || echo "Nada novo para commit"

# Conecta ao GitHub
echo ""
echo "🔗 Conectando ao GitHub..."
git remote remove origin 2>/dev/null || true
git remote add origin "https://github.com/$GITHUB_USER/$REPO_NAME.git"

# Push
echo ""
echo "📤 Enviando para o GitHub..."
echo "(Será solicitado seu token de acesso pessoal)"
echo ""
git push -u origin main

echo ""
echo "✅ Deploy concluído com sucesso!"
echo ""
echo "🔗 Link do repositório:"
echo "   https://github.com/$GITHUB_USER/$REPO_NAME"
echo ""
echo "📎 Link para entregar aos professores:"
echo "   https://github.com/$GITHUB_USER/$REPO_NAME"
echo ""
