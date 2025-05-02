# Requisitos Não Funcionais - Conexão Sênior

Este documento descreve os requisitos não funcionais da plataforma Conexão Sênior, uma rede social inclusiva para idosos entre 60 e 70 anos na região de Cuiabá-MT. Estes requisitos complementam os requisitos funcionais e são essenciais para garantir uma experiência de usuário adequada ao público-alvo.

## 1. Usabilidade

RNF01 - A interface deve seguir princípios de design centrado no usuário, com elementos visuais claros e intuitivos.

RNF02 - A navegação deve ser simplificada, com no máximo 3 níveis de profundidade na hierarquia de menus.

RNF03 - Os botões e elementos interativos devem ter tamanho mínimo de 44x44 pixels para facilitar o toque em dispositivos móveis.

RNF04 - A plataforma deve apresentar feedback visual e sonoro para todas as ações realizadas pelo usuário.

RNF05 - O sistema deve oferecer tutoriais interativos para cada funcionalidade principal, com opção de reexibição a qualquer momento.

RNF06 - A linguagem utilizada deve ser simples, direta e livre de jargões técnicos.

## 2. Acessibilidade

RNF07 - A plataforma deve estar em conformidade com as diretrizes WCAG 2.1 nível AA.

RNF08 - O sistema deve permitir ajuste de tamanho de fonte em pelo menos 3 níveis (normal, grande e extra grande).

RNF09 - A interface deve oferecer pelo menos 3 opções de contraste, incluindo alto contraste para usuários com baixa visão.

RNF10 - Todos os conteúdos não-textuais devem possuir alternativas textuais para leitores de tela.

RNF11 - O sistema deve ser compatível com tecnologias assistivas comuns, como leitores de tela e ampliadores.

RNF12 - A navegação deve ser possível utilizando apenas o teclado.

## 3. Desempenho

RNF13 - O tempo de carregamento inicial da aplicação não deve exceder 3 segundos em conexões 4G padrão.

RNF14 - As transições entre páginas devem ocorrer em menos de 1 segundo.

RNF15 - O sistema deve suportar até 10.000 usuários simultâneos sem degradação de desempenho.

RNF16 - O consumo de dados móveis deve ser otimizado, não ultrapassando 5MB por sessão de 10 minutos de uso típico.

RNF17 - A aplicação deve implementar técnicas de carregamento progressivo para imagens e conteúdos pesados.

## 4. Segurança e Privacidade

RNF18 - Todas as comunicações entre cliente e servidor devem ser criptografadas utilizando HTTPS/TLS 1.3 ou superior.

RNF19 - As senhas dos usuários devem ser armazenadas utilizando algoritmos de hash seguros (bcrypt ou similar).

RNF20 - O sistema deve implementar proteção contra ataques comuns (XSS, CSRF, injeção SQL).

RNF21 - A plataforma deve oferecer configurações de privacidade claras e acessíveis, com opções simplificadas.

RNF22 - O sistema deve realizar logout automático após 30 minutos de inatividade.

RNF23 - A política de privacidade deve ser apresentada em linguagem simples e acessível.

## 5. Compatibilidade

RNF24 - A aplicação web deve ser responsiva e funcionar corretamente em dispositivos com telas de 5 a 27 polegadas.

RNF25 - O sistema deve ser compatível com as duas versões mais recentes dos navegadores Chrome, Firefox, Safari e Edge.

RNF26 - A aplicação deve funcionar adequadamente em dispositivos Android (versão 8.0 ou superior) e iOS (versão 12 ou superior).

RNF27 - O sistema deve se adaptar a diferentes velocidades de conexão, oferecendo versões otimizadas para conexões lentas.

## 6. Manutenibilidade e Escalabilidade

RNF28 - O código-fonte deve seguir padrões de codificação consistentes e ser adequadamente documentado.

RNF29 - A arquitetura deve permitir a adição de novos recursos sem necessidade de refatoração significativa.

RNF30 - O sistema deve implementar monitoramento de erros e uso para identificação proativa de problemas.

RNF31 - A aplicação deve ser modular, permitindo atualizações parciais sem afetar todo o sistema.

RNF32 - O banco de dados deve ser escalável para suportar crescimento de até 100% ao ano no volume de dados.

## 7. Disponibilidade e Confiabilidade

RNF33 - O sistema deve estar disponível 99,5% do tempo, com manutenções programadas fora do horário de pico (22h às 5h).

RNF34 - O tempo médio de recuperação após falhas não deve exceder 30 minutos.

RNF35 - A plataforma deve implementar backup automático diário, com retenção de dados por pelo menos 30 dias.

RNF36 - O sistema deve manter logs detalhados de operações críticas para auditoria e recuperação.

RNF37 - A aplicação deve implementar mecanismos de recuperação de estado em caso de falha durante operações críticas.

## 8. Conformidade Legal

RNF38 - O sistema deve estar em conformidade com a Lei Geral de Proteção de Dados (LGPD).

RNF39 - A plataforma deve implementar mecanismos para solicitação de exclusão de dados pessoais conforme exigido pela legislação.

RNF40 - O sistema deve manter registros de consentimento para coleta e uso de dados pessoais.

RNF41 - A aplicação deve implementar controles de acesso baseados em papéis para proteger dados sensíveis.

RNF42 - O sistema deve estar em conformidade com o Estatuto do Idoso no que se refere à acessibilidade digital.
