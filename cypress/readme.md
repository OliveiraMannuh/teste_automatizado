## Iniciando projeto Cypress

# Verifica se node está instalado: node -v
# Verifica se npm está instalado: npm -v
# Inicia criação de projeto node com as configurações padrões (package.jason): npm init -y
# Iniciar um projeto cypress: npm install cypress --save-dev
# Garantir que o cypress foi instalado: npx cypress -v
# Iniciar configuração do projeto: npx cypress open → acessa E2E → continua → incia
# Crie uma pasta com nome "e2e" (pasta padrão que o cypress reconhece que vai conter os arquivos de teste) na raiz da pasta cypress, caso queira criar uma pasta com nome personalizado, configure no arquivo cypress.config.js o nome da pasta. 
# Para criar um arquivo a extensão do arquivo é .cy.js para o cypress reconhecer. 
# Configurar o arquivo jsconfig.json na raiz do projeto com o conteúdo: 
{
    "include": ["./node_modules/cypress", "./cypress/**/*.js"]
}

# Caso a aplicação tenha a visualização de conteúdo insegura, problemas no carregamento do network, configure para ignorar o erro, no arquivo cypress.config.js, abaixo de module exports:
chromeWebSecurity: false,

# No arquivo de teste configurar: arrange, act (ações), assert (valida)