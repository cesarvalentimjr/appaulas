# Curso de Julgamento e Tomada de Decisão em Contabilidade

Este repositório contém um aplicativo Streamlit para o curso de "Julgamento e Tomada de Decisão em Contabilidade", focado em Behavioral Finance.

## Como usar

O aplicativo permite aos alunos navegar pelas aulas (em formato HTML) e interagir com exercícios práticos através de uma barra lateral.

### Aulas disponíveis:

*   **Bloco 1 - Fundamentos e Ruído** (`Aula1_nova.html`)
*   **Bloco 2 - Anomalias e Prospect Theory** (`Aula2_nova.html`)
*   **Bloco 3 - Séries Temporais e Efeitos de Mercado** (`Aula3_nova.html`)
*   **Bloco 4 - Integração e Neuroeconomia** (`Aula4_nova.html`)
*   **Aplicativo Interativo - Exercícios Práticos** (`AppBF.html`)

## Deploy no Streamlit Cloud

Para fazer o deploy deste aplicativo no Streamlit Cloud, siga os passos:

1.  Crie um novo repositório no GitHub.
2.  Faça o upload de todos os arquivos deste projeto para o seu novo repositório.
3.  Vá para o [Streamlit Cloud](https://share.streamlit.io/).
4.  Clique em "New app" e conecte-se ao seu repositório GitHub.
5.  Selecione o repositório onde você fez o upload dos arquivos.
6.  Certifique-se de que o "Main file path" esteja configurado para `app.py`.
7.  Clique em "Deploy!"

## Estrutura do Projeto

```
.github/
├── workflows/
│   └── streamlit.yml  (Opcional: para CI/CD)
├── .gitignore
├── app.py
├── requirements.txt
├── Aula1_nova.html
├── Aula2_nova.html
├── Aula3_nova.html
├── Aula4_nova.html
└── AppBF.html
```

