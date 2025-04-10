# Estrutura de Páginas e Rotas do Front-End - Conexão Sênior

Este documento descreve a estrutura de páginas e rotas para o front-end da plataforma Conexão Sênior, organizadas por funcionalidades e alinhadas com os requisitos funcionais e endpoints da API.

## Tecnologias Recomendadas

- **Framework**: React.js com TypeScript
- **Roteamento**: React Router
- **Gerenciamento de Estado**: Context API + Hooks
- **UI/Componentes**: Material-UI (com temas personalizados para acessibilidade)
- **Requisições HTTP**: Axios
- **Formulários**: React Hook Form
- **Validação**: Yup

## 1. Páginas de Autenticação

### 1.1. Página Inicial (Landing Page)

- **Rota**: `/`
- **Componentes**: Banner principal, seção de benefícios, depoimentos, FAQ
- **Funcionalidades**: Apresentação da plataforma, links para cadastro e login

### 1.2. Login

- **Rota**: `/login`
- **Componentes**: Formulário de login, link para recuperação de senha
- **Endpoints da API**: `POST /users/login/`
- **Requisitos**: RF02

### 1.3. Cadastro

- **Rota**: `/cadastro`
- **Componentes**: Formulário de cadastro com validações
- **Endpoints da API**: `POST /users/`
- **Requisitos**: RF01

### 1.4. Recuperação de Senha

- **Rota**: `/recuperar-senha`
- **Componentes**: Formulário para solicitar redefinição
- **Endpoints da API**: `POST /users/reset-password/`
- **Requisitos**: RF03

### 1.5. Confirmação de Recuperação de Senha

- **Rota**: `/recuperar-senha/confirmar`
- **Componentes**: Formulário para nova senha
- **Endpoints da API**: `PUT /users/reset-password/confirm/`
- **Requisitos**: RF03

## 2. Páginas de Perfil de Usuário

### 2.1. Meu Perfil

- **Rota**: `/perfil`
- **Componentes**: Dados do usuário, foto, informações pessoais, interesses
- **Endpoints da API**: `GET /users/me/`
- **Requisitos**: RF05

### 2.2. Editar Perfil

- **Rota**: `/perfil/editar`
- **Componentes**: Formulário de edição de perfil
- **Endpoints da API**: `PUT /users/me/`
- **Requisitos**: RF05

### 2.3. Excluir Conta

- **Rota**: `/perfil/excluir`
- **Componentes**: Confirmação de exclusão
- **Endpoints da API**: `DELETE /users/me/`
- **Requisitos**: RF04

### 2.4. Perfil de Outro Usuário

- **Rota**: `/usuarios/:id`
- **Componentes**: Visualização de perfil, botão para iniciar conversa
- **Endpoints da API**: `GET /users/{id}/`
- **Requisitos**: RF06

### 2.5. Pesquisa de Usuários

- **Rota**: `/usuarios/pesquisa`
- **Componentes**: Barra de pesquisa, filtros, lista de resultados
- **Endpoints da API**: `GET /users/search/`
- **Requisitos**: RF07

## 3. Páginas de Comunidades

### 3.1. Lista de Comunidades

- **Rota**: `/comunidades`
- **Componentes**: Lista de comunidades, filtros, barra de pesquisa
- **Endpoints da API**: `GET /communities/`
- **Requisitos**: RF10

### 3.2. Criar Comunidade

- **Rota**: `/comunidades/criar`
- **Componentes**: Formulário de criação
- **Endpoints da API**: `POST /communities/`
- **Requisitos**: RF08

### 3.3. Detalhes da Comunidade

- **Rota**: `/comunidades/:id`
- **Componentes**: Informações da comunidade, feed de posts, lista de membros
- **Endpoints da API**: `GET /communities/{id}/`, `GET /communities/{id}/feed/`
- **Requisitos**: RF11

### 3.4. Editar Comunidade (Moderador)

- **Rota**: `/comunidades/:id/editar`
- **Componentes**: Formulário de edição
- **Endpoints da API**: `PUT /communities/{id}/`
- **Requisitos**: RF13

### 3.5. Membros da Comunidade

- **Rota**: `/comunidades/:id/membros`
- **Componentes**: Lista de membros, opções de moderação
- **Endpoints da API**: `GET /communities/{id}/members/`
- **Requisitos**: RF15

### 3.6. Solicitações Pendentes (Moderador)

- **Rota**: `/comunidades/:id/solicitacoes`
- **Componentes**: Lista de solicitações, botões de aprovar/recusar
- **Endpoints da API**: `GET /communities/{id}/requests/`
- **Requisitos**: RF16

## 4. Páginas de Posts e Interações

### 4.1. Criar Post

- **Rota**: `/comunidades/:id/posts/criar`
- **Componentes**: Editor de texto, upload de imagens
- **Endpoints da API**: `POST /communities/{id}/posts/`
- **Requisitos**: RF20

### 4.2. Detalhes do Post

- **Rota**: `/comunidades/:id/posts/:postId`
- **Componentes**: Conteúdo do post, comentários, botões de ação
- **Endpoints da API**: `GET /communities/{id}/posts/{post_id}/`
- **Requisitos**: RF23, RF24, RF25

### 4.3. Editar Post

- **Rota**: `/comunidades/:id/posts/:postId/editar`
- **Componentes**: Editor de texto
- **Endpoints da API**: `PUT /communities/{id}/posts/{post_id}/`
- **Requisitos**: RF21

### 4.4. Moderação de Posts (Moderador)

- **Rota**: `/comunidades/:id/posts/pendentes`
- **Componentes**: Lista de posts pendentes, botões de aprovar/recusar
- **Endpoints da API**: `GET /communities/{id}/posts/pending/`
- **Requisitos**: RF17

## 5. Páginas de Eventos e Atividades

### 5.1. Lista de Eventos

- **Rota**: `/eventos`
- **Componentes**: Lista de eventos, filtros, mapa
- **Endpoints da API**: `GET /events/`
- **Requisitos**: RF26

### 5.2. Detalhes do Evento

- **Rota**: `/eventos/:id`
- **Componentes**: Informações do evento, botão de favoritar
- **Endpoints da API**: `GET /events/{id}/`
- **Requisitos**: RF28

### 5.3. Lista de Atividades Online

- **Rota**: `/atividades`
- **Componentes**: Lista de atividades, filtros
- **Endpoints da API**: `GET /activities/`
- **Requisitos**: RF27

### 5.4. Detalhes da Atividade

- **Rota**: `/atividades/:id`
- **Componentes**: Informações da atividade, botão de favoritar
- **Endpoints da API**: `GET /activities/{id}/`
- **Requisitos**: RF29

### 5.5. Eventos Favoritos

- **Rota**: `/eventos/favoritos`
- **Componentes**: Lista de eventos favoritos
- **Endpoints da API**: `GET /events/favorites/`
- **Requisitos**: RF30

### 5.6. Atividades Favoritas

- **Rota**: `/atividades/favoritas`
- **Componentes**: Lista de atividades favoritas
- **Endpoints da API**: `GET /activities/favorites/`
- **Requisitos**: RF31

### 5.7. Calendário de Eventos

- **Rota**: `/eventos/calendario`
- **Componentes**: Calendário interativo
- **Endpoints da API**: `GET /events/calendar/`
- **Requisitos**: RF32

### 5.8. Recomendações

- **Rota**: `/recomendacoes`
- **Componentes**: Lista de eventos e atividades recomendadas
- **Endpoints da API**: `GET /recommendations/events/`, `GET /recommendations/activities/`
- **Requisitos**: RF33

## 6. Páginas de Comunicação

### 6.1. Grupos de Discussão

- **Rota**: `/grupos`
- **Componentes**: Lista de grupos de discussão
- **Endpoints da API**: `GET /discussion-groups/`
- **Requisitos**: RF34

### 6.2. Detalhes do Grupo

- **Rota**: `/grupos/:id`
- **Componentes**: Mensagens do grupo, formulário para enviar mensagem
- **Endpoints da API**: `GET /discussion-groups/{id}/`, `GET /discussion-groups/{id}/messages/`
- **Requisitos**: RF34

### 6.3. Chat Privado - Lista de Conversas

- **Rota**: `/mensagens`
- **Componentes**: Lista de conversas
- **Endpoints da API**: `GET /chats/`
- **Requisitos**: RF35

### 6.4. Chat Privado - Conversa

- **Rota**: `/mensagens/:id`
- **Componentes**: Histórico de mensagens, formulário para enviar mensagem
- **Endpoints da API**: `GET /chats/{id}/messages/`, `POST /chats/{id}/messages/`
- **Requisitos**: RF35

### 6.5. Compartilhamento de Experiências

- **Rota**: `/experiencias`
- **Componentes**: Lista de experiências compartilhadas
- **Endpoints da API**: `GET /experiences/`
- **Requisitos**: RF36

### 6.6. Criar Experiência

- **Rota**: `/experiencias/criar`
- **Componentes**: Formulário para compartilhar experiência, upload de fotos
- **Endpoints da API**: `POST /experiences/`
- **Requisitos**: RF36

### 6.7. Círculos de Amizade

- **Rota**: `/circulos`
- **Componentes**: Lista de círculos de amizade
- **Endpoints da API**: `GET /friendship-circles/`
- **Requisitos**: RF37

### 6.8. Detalhes do Círculo

- **Rota**: `/circulos/:id`
- **Componentes**: Membros do círculo, opções de gerenciamento
- **Endpoints da API**: `GET /friendship-circles/{id}/`
- **Requisitos**: RF37

## 7. Páginas de Acessibilidade

### 7.1. Configurações de Acessibilidade

- **Rota**: `/acessibilidade`
- **Componentes**: Opções de tamanho de fonte, contraste, etc.
- **Endpoints da API**: `GET /accessibility/preferences/`, `PUT /accessibility/preferences/`
- **Requisitos**: RF38

### 7.2. Tutoriais

- **Rota**: `/tutoriais`
- **Componentes**: Lista de tutoriais disponíveis
- **Endpoints da API**: `GET /tutorials/`
- **Requisitos**: RF39

### 7.3. Tutorial Específico

- **Rota**: `/tutoriais/:id`
- **Componentes**: Conteúdo do tutorial, opção de áudio
- **Endpoints da API**: `GET /tutorials/{id}/`
- **Requisitos**: RF39, RF40

## 8. Componentes Globais

### 8.1. Barra de Navegação

- **Componentes**: Links para principais seções, notificações, perfil

### 8.2. Rodapé

- **Componentes**: Links úteis, informações de contato, termos de uso

### 8.3. Controles de Acessibilidade

- **Componentes**: Ajuste rápido de fonte e contraste, ativação de áudio
- **Requisitos**: RF38, RF40, RF41

### 8.4. Notificações

- **Componentes**: Painel de notificações

## 9. Fluxos de Navegação Principais

### 9.1. Fluxo de Autenticação

1. Página Inicial → Login/Cadastro → Feed Principal
2. Login → Recuperação de Senha → Confirmação → Login

### 9.2. Fluxo de Comunidades

1. Lista de Comunidades → Detalhes da Comunidade → Feed de Posts → Detalhes do Post
2. Lista de Comunidades → Criar Comunidade → Detalhes da Comunidade

### 9.3. Fluxo de Eventos

1. Lista de Eventos → Detalhes do Evento → Favoritar
2. Calendário → Detalhes do Evento

### 9.4. Fluxo de Comunicação

1. Lista de Conversas → Conversa Específica
2. Perfil de Usuário → Iniciar Conversa

## 10. Considerações de Acessibilidade

- Todas as páginas devem implementar os controles de acessibilidade globais
- Tutoriais interativos devem estar disponíveis em pontos estratégicos
- Suporte por áudio deve ser oferecido para conteúdos textuais importantes
- Interface deve usar linguagem simples e direta
- Elementos visuais devem ter alto contraste e tamanho adequado
- Navegação deve ser intuitiva e consistente em toda a plataforma
