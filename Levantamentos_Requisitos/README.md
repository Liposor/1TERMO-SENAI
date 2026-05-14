# Documento de Levantamento de Requisitos de Software

## 1. Introdução
Este documento detalha o levantamento de requisitos para o desenvolvimento do sistema, consolidando as informações coletadas por meio de diversas técnicas de engenharia de requisitos, incluindo entrevistas, brainstormings e prototipagem.

## 2. Técnicas de Levantamento Utilizadas

### 2.1. Brainstorming
Realizado com as partes interessadas (stakeholders) para explorar ideias e identificar necessidades latentes.
- **Objetivo:** Definir a visão geral do produto e funcionalidades inovadoras.
- **Principais Ideias Geradas:** Centralização de dados em nuvem, interface intuitiva para usuários leigos e automação de notificações.

### 2.2. Entrevistas
Sessões individuais com gestores e usuários operacionais para entender o fluxo de trabalho atual e os pontos de dor.
- **Público-alvo:** Gerentes de projeto e analistas de suporte.
- **Resultados:** Identificou-se a necessidade crítica de relatórios de produtividade em tempo real.

## 3. Requisitos Funcionais (RF)
Os requisitos funcionais descrevem as funções que o sistema deve executar.

| ID | Descrição | Prioridade |
|:---|:---|:---|
| RF01 | O sistema deve permitir o cadastro de novos usuários com diferentes níveis de acesso. | Alta |
| RF02 | O sistema deve gerar relatórios técnicos em formato PDF e CSV. | Média |
| RF03 | O sistema deve enviar notificações automáticas via e-mail sobre prazos vencidos. | Alta |
| RF04 | O sistema deve permitir a importação de dados a partir de planilhas Excel. | Baixa |
| RF05 | O sistema deve manter um histórico de logs de todas as alterações feitas em registros. | Média |

## 4. Requisitos Não Funcionais (RNF)
Os requisitos não funcionais definem atributos de qualidade e restrições técnicas.

| ID | Descrição | Categoria |
|:---|:---|:---|
| RNF01 | O sistema deve responder a qualquer consulta em menos de 2 segundos. | Desempenho |
| RNF02 | A interface deve ser responsiva, adaptando-se a dispositivos móveis e desktops. | Usabilidade |
| RNF03 | Todos os dados sensíveis devem ser criptografados utilizando AES-256. | Segurança |
| RNF04 | O sistema deve estar disponível (uptime) 99,9% do tempo. | Disponibilidade |
| RNF05 | O código-fonte deve seguir as convenções de Clean Code para facilitar a manutenção. | Manutenibilidade |

## 5. Diagramas e Modelagem

### 5.1. Diagrama de Caso de Uso
O diagrama de caso de uso descreve as interações entre os atores (usuários/sistemas externos) e as funcionalidades do sistema.
- **Atores:** Administrador, Usuário Padrão, Sistema de E-mail.
- **Casos de Uso Principais:** Manter Usuário, Gerar Relatório, Autenticar Login.

### 5.2. Diagrama de Fluxo de Dados (DFD)
Representa a movimentação de informações através do sistema, desde a entrada de dados pelo usuário até o armazenamento no banco de dados e saída em relatórios.

## 6. Prototipagem
Foram desenvolvidos protótipos de baixa e alta fidelidade para validação com o usuário.
- **Baixa Fidelidade (Wireframes):** Desenhos esquemáticos focados na disposição dos elementos e fluxo de navegação.
- **Alta Fidelidade (Mockups):** Representação visual fiel com paleta de cores, tipografia e ícones, utilizada para testes de usabilidade.

## 7. Relatórios Técnicos
O sistema deve ser capaz de processar grandes volumes de dados para gerar os seguintes documentos:
1. **Relatório de Desempenho Mensal:** Sumarização de métricas de produtividade.
2. **Relatório de Auditoria:** Listagem de acessos e modificações por período.
3. **Relatório de Erros e Exceções:** Logs técnicos para a equipe de infraestrutura.

## 8. Conclusão
Este levantamento serve como base para as fases de design e implementação. A validação destes requisitos junto aos stakeholders é mandatória antes do início do desenvolvimento técnico.