# API Conexão Sênior - Documentação

Esta documentação descreve as rotas da API para o projeto Conexão Sênior, uma plataforma digital inclusiva para idosos. A API foi projetada seguindo os princípios RESTful e será implementada usando Django e Django REST Framework.

## Base URL

```
http://localhost:8000/api/v1/
```

## Autenticação

A API utiliza autenticação baseada em tokens JWT (JSON Web Tokens).

```
POST /auth/token/           # Obter token de acesso (login)
POST /auth/token/refresh/   # Renovar token de acesso
POST /auth/token/verify/    # Verificar validade do token
```

## 1. Gerenciamento de Usuários

```
# Usuários
POST   /users/                  # Cadastrar novo usuário (RF01)
POST   /users/login/            # Login de usuário (RF02)
POST   /users/reset-password/   # Solicitar redefinição de senha (RF03)
PUT    /users/reset-password/confirm/  # Confirmar redefinição de senha (RF03)
GET    /users/me/               # Obter perfil do usuário logado
PUT    /users/me/               # Editar perfil do usuário (RF05)
DELETE /users/me/               # Excluir perfil do usuário (RF04)
GET    /users/{id}/             # Visualizar perfil de outro usuário (RF06)
GET    /users/search/           # Pesquisar por usuários (RF07)
```

## 2. Gerenciamento de Comunidades

```
# Comunidades
POST   /communities/                    # Criar nova comunidade (RF08)
GET    /communities/                    # Listar comunidades
GET    /communities/search/             # Pesquisar por comunidades (RF10)
GET    /communities/{id}/               # Obter detalhes de uma comunidade
PUT    /communities/{id}/               # Editar comunidade (RF13 - moderador)
DELETE /communities/{id}/               # Excluir comunidade (RF14 - moderador)
GET    /communities/{id}/feed/          # Visualizar feed da comunidade (RF11)

# Membros de Comunidades
POST   /communities/{id}/members/       # Solicitar participação em comunidade (RF09)
DELETE /communities/{id}/members/me/    # Deixar uma comunidade (RF12)
GET    /communities/{id}/members/       # Listar membros da comunidade
DELETE /communities/{id}/members/{user_id}/ # Remover membro da comunidade (RF15 - moderador)

# Solicitações de Participação (para comunidades privadas)
GET    /communities/{id}/requests/      # Listar solicitações pendentes (moderador)
PUT    /communities/{id}/requests/{request_id}/ # Aceitar/recusar solicitação (RF16 - moderador)
```

## 3. Interação em Comunidades

```
# Posts
POST   /communities/{id}/posts/         # Criar post na comunidade (RF20)
GET    /communities/{id}/posts/         # Listar posts da comunidade
GET    /communities/{id}/posts/{post_id}/ # Obter detalhes de um post
PUT    /communities/{id}/posts/{post_id}/ # Editar post (RF21)
DELETE /communities/{id}/posts/{post_id}/ # Excluir post (RF22, RF18 - moderador)

# Moderação de Posts (para comunidades moderadas)
GET    /communities/{id}/posts/pending/ # Listar posts pendentes de aprovação (moderador)
PUT    /communities/{id}/posts/{post_id}/approve/ # Aprovar/recusar post (RF17 - moderador)

# Comentários
POST   /communities/{id}/posts/{post_id}/comments/ # Comentar em um post (RF23)
GET    /communities/{id}/posts/{post_id}/comments/ # Listar comentários de um post
PUT    /communities/{id}/posts/{post_id}/comments/{comment_id}/ # Editar comentário (RF24)
DELETE /communities/{id}/posts/{post_id}/comments/{comment_id}/ # Excluir comentário (RF25, RF19 - moderador)
```

## 4. Eventos e Atividades

```
# Eventos
GET    /events/                  # Listar eventos na região (RF26)
GET    /events/{id}/             # Obter detalhes de um evento
GET    /events/calendar/         # Visualizar calendário de eventos (RF32)

# Atividades Online
GET    /activities/              # Listar atividades online (RF27)
GET    /activities/{id}/         # Obter detalhes de uma atividade

# Favoritos
POST   /events/{id}/favorite/    # Salvar evento como favorito (RF28)
DELETE /events/{id}/favorite/    # Remover evento dos favoritos
GET    /events/favorites/        # Listar eventos favoritos (RF30)

POST   /activities/{id}/favorite/ # Salvar atividade como favorita (RF29)
DELETE /activities/{id}/favorite/ # Remover atividade dos favoritos
GET    /activities/favorites/     # Listar atividades favoritas (RF31)

# Recomendações
GET    /recommendations/events/    # Obter recomendações de eventos (RF33)
GET    /recommendations/activities/ # Obter recomendações de atividades (RF33)
```

## 5. Comunicação

```
# Grupos de Discussão
GET    /discussion-groups/         # Listar grupos de discussão
GET    /discussion-groups/{id}/    # Obter detalhes de um grupo
POST   /discussion-groups/{id}/join/ # Participar de um grupo (RF34)
DELETE /discussion-groups/{id}/leave/ # Sair de um grupo
GET    /discussion-groups/{id}/messages/ # Listar mensagens do grupo
POST   /discussion-groups/{id}/messages/ # Enviar mensagem ao grupo

# Chat Privado
GET    /chats/                    # Listar conversas do usuário
POST   /chats/                    # Iniciar nova conversa (RF35)
GET    /chats/{id}/               # Obter detalhes de uma conversa
GET    /chats/{id}/messages/      # Listar mensagens de uma conversa
POST   /chats/{id}/messages/      # Enviar mensagem em uma conversa

# Compartilhamento de Fotos e Experiências
POST   /experiences/              # Compartilhar experiência (RF36)
GET    /experiences/              # Listar experiências compartilhadas
GET    /experiences/{id}/         # Obter detalhes de uma experiência
POST   /experiences/{id}/photos/  # Adicionar foto a uma experiência
DELETE /experiences/{id}/photos/{photo_id}/ # Remover foto de uma experiência

# Círculos de Amizade
POST   /friendship-circles/       # Criar círculo de amizade (RF37)
GET    /friendship-circles/       # Listar círculos de amizade do usuário
GET    /friendship-circles/{id}/  # Obter detalhes de um círculo
POST   /friendship-circles/{id}/members/ # Adicionar membro a um círculo
DELETE /friendship-circles/{id}/members/{user_id}/ # Remover membro de um círculo
```

## 6. Acessibilidade

```
# Preferências de Acessibilidade
GET    /accessibility/preferences/ # Obter preferências de acessibilidade do usuário
PUT    /accessibility/preferences/ # Atualizar preferências (RF38)

# Tutoriais
GET    /tutorials/                # Listar tutoriais disponíveis (RF39)
GET    /tutorials/{id}/           # Obter tutorial específico

# Suporte por Áudio
GET    /audio-support/{content_id}/ # Obter versão em áudio de um conteúdo (RF40)
```

## Códigos de Status HTTP

- 200 OK: Requisição bem-sucedida
- 201 Created: Recurso criado com sucesso
- 204 No Content: Requisição bem-sucedida, sem conteúdo para retornar
- 400 Bad Request: Erro na requisição do cliente
- 401 Unauthorized: Autenticação necessária
- 403 Forbidden: Sem permissão para acessar o recurso
- 404 Not Found: Recurso não encontrado
- 500 Internal Server Error: Erro interno do servidor
