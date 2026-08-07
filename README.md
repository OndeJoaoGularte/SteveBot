# 🍁 SteveBot (Projeto Pessoal)

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![Contexto](https://img.shields.io/badge/Contexto-Projeto%20Pessoal-blueviolet)
![Status](https://img.shields.io/badge/Status-Arquivado-success)

Este projeto é um bot simples e interativo para o Discord desenvolvido como um projeto pessoal para uso exclusivo em um servidor de amigos. O sistema é tematizado em torno do "Steve", uma persona de um jovem estudante canadense de 14 anos, cristão, apaixonado por história e filosofia, cheio de relatos sobre sua própria vida e que ama muito seus amigos. O desenvolvimento segue um "Roadmap de Crescimento", onde o bot amadurece e ganha novas funcionalidades.

---

## 🎯 Objetivo do Projeto

O projeto tem como objetivo consolidar os conhecimentos em **Python** e programação assíncrona, utilizando a biblioteca `discord.py`. Além do aspecto técnico, o projeto explora o *worldbuilding* dentro do código, estruturando dados e respostas para criar um personagem cativante, com memórias, opiniões e vínculos fictícios para criar uma experiência de uso imersiva e bem humorada.

---

## 🚀 Funcionalidades

As funcionalidades acompanham o amadurecimento do personagem:

1. **👶 Baby & 👦 Kid Steve (Fases Em Desenvolvimento):**
   * **Comandos Básicos e Tasks:** Medição de latência (`/ping`), repetição de mensagens (`/falar`), gerenciamento de datas e rotinas em background (*Task de datas*).
   * **Integração de Lore:** Um sistema rico de respostas onde o Steve conta curiosidades da sua vida (`/segredo`), compartilha sua fé (`/versiculo`), dá conselhos ou mede o seu afeto pelos usuários (`/amor`, que sempre retorna 100%).

2. **🧒 Teen & 🧑 Young Steve (Sistemas e Roleplay):**
   * **Interação de Usuários:** Comandos interativos com menções e GIFs, como `/bater`, `/beijar`, além de sistemas de relacionamento (`/casar`, `/shipp`) e duelos.
   * **Gerenciamento de Comunidade:** Criação e atribuição de cargos customizados (como *steVeroner* e *steVideos*) para notificações e lembretes específicos.
   * **Ferramentas de RPG:** Sistema de rolagem de dados (`/rolagem`) nativo no chat.

3. **👨 Adult & 👴 Old Steve (Integrações Futuras):**
   * **Consumo de APIs Externas:** Buscas automatizadas no Google/Wikipedia e ferramentas de tradução de idiomas.
   * **Reprodutor de Áudio:** Sistema completo para tocar, pular e pausar músicas do YouTube e Spotify nos canais de voz.

---

## 🛠️ Tecnologias Utilizadas

* **Python:** Linguagem de programação principal utilizada em todo o ecossistema do bot.
* **Discord.py (v2.5):** Wrapper moderno, assíncrono e orientado a objetos para comunicação com a API oficial do Discord.
* **Aiohttp (v3.11):** Cliente HTTP assíncrono para realizar requisições web rápidas e sem bloqueio de thread.
* **Flask (v3.0):** Micro-framework web utilizado para criar rotas de *keep-alive* e manter o bot rodando continuamente em serviços de hospedagem.
* **Python-dotenv:** Gerenciamento de variáveis de ambiente para ocultar chaves sensíveis (como o Token do Discord).

---

## 🧠 Conceitos Aplicados

* **Programação Assíncrona (Async/Await):** Utilização da arquitetura *event-driven* do Python para lidar com múltiplos comandos e eventos do servidor simultaneamente sem travar a aplicação.
* **Interação de Usuário (Slash Commands):** Registro e validação de comandos nativos do Discord, melhorando a experiência de uso e organização no chat.
* **Rotinas em Background (Tasks):** Implementação de tarefas agendadas (como alertas de datas) que rodam paralelamente ao loop de eventos do bot.
* **Design de Persona e Estrutura de Dados:** Criação de arrays e arquivos JSON para armazenar as histórias, medos e interesses do bot, sorteadas aleatoriamente para simular conversas orgânicas.
* **Gerenciamento de Cargos e Permissões:** Manipulação da API do Discord para ler e atribuir *roles* específicos a usuários que desejam ser marcados em lembretes e vídeos.
