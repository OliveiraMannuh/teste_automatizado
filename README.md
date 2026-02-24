# 🤖 Teste Automatizado

Repositório com exemplos e implementações de testes automatizados utilizando três das principais ferramentas do mercado: **Selenium**, **Cypress** e **PyAutoGUI**. O projeto também conta com agendamento de testes via script Python com `cron`.

---

## 📁 Estrutura do Projeto

```
teste_automatizado/
├── cypress/          # Testes end-to-end com Cypress (JavaScript)
├── pyautogui/        # Automação de interface gráfica com PyAutoGUI (Python/Jupyter)
├── selenium/         # Testes web com Selenium (Python/Jupyter)
├── cron_teste.py     # Script para agendamento e execução automática de testes
└── README.md
```

---

## 🛠️ Tecnologias Utilizadas

| Ferramenta | Linguagem | Finalidade |
|---|---|---|
| [Selenium](https://www.selenium.dev/) | Python | Automação e testes de aplicações web |
| [Cypress](https://www.cypress.io/) | JavaScript | Testes end-to-end modernos para web |
| [PyAutoGUI](https://pyautogui.readthedocs.io/) | Python | Automação de GUI (teclado, mouse, tela) |
| Jupyter Notebook | Python | Desenvolvimento interativo dos scripts |
| Python (cron) | Python | Agendamento e orquestração de testes |

---

## 📦 Pré-requisitos

### Para os testes com Selenium e PyAutoGUI (Python)

- Python 3.8+
- pip

```bash
pip install selenium pyautogui jupyter notebook
```

> Para o Selenium, é necessário ter o [WebDriver](https://chromedriver.chromium.org/downloads) compatível com seu navegador instalado.

### Para os testes com Cypress (JavaScript)

- Node.js 14+
- npm ou yarn

```bash
npm install cypress --save-dev
```

---

## 🚀 Como Executar

### Selenium

Acesse a pasta `selenium/` e abra o notebook desejado:

```bash
cd selenium
jupyter notebook
```

### PyAutoGUI

Acesse a pasta `pyautogui/` e abra o notebook desejado:

```bash
cd pyautogui
jupyter notebook
```

### Cypress

Acesse a pasta `cypress/` e execute:

```bash
# Modo interativo
npx cypress open

# Modo headless (linha de comando)
npx cypress run
```

### Agendamento com Cron

O arquivo `cron_teste.py` permite agendar a execução automática dos testes:

```bash
python cron_teste.py
```

---

## 📌 Visão Geral das Ferramentas

### 🔵 Selenium
Biblioteca amplamente utilizada para automatizar navegadores web. Ideal para testes de regressão e validação de fluxos em aplicações web, com suporte a múltiplos navegadores.

### 🟢 Cypress
Framework moderno para testes end-to-end focado em aplicações JavaScript. Oferece execução em tempo real, recarregamento automático e excelente experiência de depuração.

### 🟡 PyAutoGUI
Biblioteca Python para automação de interface gráfica do sistema operacional. Permite controlar o mouse e teclado, capturar tela e interagir com qualquer aplicação desktop.

---

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma *issue* ou enviar um *pull request*.

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/minha-feature`)
3. Commit suas alterações (`git commit -m 'feat: adiciona minha feature'`)
4. Push para a branch (`git push origin feature/minha-feature`)
5. Abra um Pull Request

---

## 👤 Autor

**OliveiraMannuh**  
[GitHub](https://github.com/OliveiraMannuh)

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.