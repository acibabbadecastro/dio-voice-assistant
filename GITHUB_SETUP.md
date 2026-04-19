# 🚀 Como Publicar no GitHub

## Passo a Passo

### 1. Acesse o diretório do projeto
```bash
cd /home/master/LAN/MEMORIES/STARK-KNOWLEDGE/PROJECTS/DIO-VOICE-ASSISTANT
```

### 2. Configure seu Git (se ainda não configurou)
```bash
git config --global user.email "seu-email@exemplo.com"
git config --global user.name "Seu Nome"
```

### 3. Inicialize o repositório Git
```bash
git init
git add .
git commit -m "Initial commit: DIO Voice Assistant"
```

### 4. Crie o repositório no GitHub
- Acesse: https://github.com/new
- Nome: `dio-voice-assistant` (ou o que preferir)
- Deixe público ou privado (recomendo público para portfólio)
- Clique em "Create repository"

### 5. Conecte e envie o código
Copie e cole os comandos que o GitHub mostrar:

```bash
# Exemplo (substitua pelo seu URL):
git remote add origin https://github.com/SEU-USUARIO/dio-voice-assistant.git
git branch -M main
git push -u origin main
```

### 6. Link para entregar aos professores
```
https://github.com/SEU-USUARIO/dio-voice-assistant
```

## ⚠️ IMPORTANTE: Segurança

Antes de fazer o commit, certifique-se de:

✅ **NÃO comitar o arquivo `.env`** (já está no .gitignore implícito)
✅ **Verificar que não há senhas** no código

O arquivo `.env` com sua API key deve ficar LOCAL apenas!

---

## 🔗 Link Final para Entrega

Substitua `SEU-USUARIO` pelo seu usuário do GitHub:

**https://github.com/SEU-USUARIO/dio-voice-assistant**

Copie esse link e envie para os professores! 🎓
