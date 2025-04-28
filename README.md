# Desafio CRUD de Usuários (Versão Simplificada)

## Contexto
Este projeto é uma resposta ao desafio técnico solicitado. Confesso que ainda estou em fase de aprendizado em FastAPI e conceitos avançados como PostgreSQL e Docker, então optei por uma abordagem simplificada:

- **Banco de dados em memória**: Usei uma lista Python para armazenar os usuários (sem PostgreSQL).
- **Foco nos fundamentos**: Implementei apenas o CRUD básico para garantir o funcionamento.

## Como Executar
1. Instale as dependências:
   ```bash
   pip install -r requirements.txt

# O Que Foi Entendido
Lógica do CRUD: Implementei as operações básicas (Create, Read, Update, Delete) seguindo os endpoints pedidos.

Validação de Dados: Utilizei Pydantic para garantir que os dados recebidos estejam no formato correto.

Estrutura da API: Aprendi a organizar rotas e métodos HTTP no FastAPI.

# Limitações Atuais
Banco de dados em memória: Por não dominar PostgreSQL ainda, os dados são armazenados temporariamente numa lista Python.

Falta de Docker: A containerização não foi implementada por falta de experiência prática.

Tratamento de erros básico: A API tem validações simples, mas poderia ser mais robusta.

# Próximos Passos para Evolução
Planejo melhorar este projeto ao aprender:

Integração com PostgreSQL: Para persistência real dos dados.

Dockerização: Para facilitar a execução em qualquer ambiente.

Autenticação: Adicionar segurança aos endpoints.

Testes Automatizados: Garantir maior confiabilidade.

# Agradecimento
Agradeço pela oportunidade de demonstrar meu aprendizado atual. Entendo que há muito para melhorar, e estou comprometido em evoluir essas habilidades técnicas. Qualquer feedback será muito valioso para meu crescimento!

