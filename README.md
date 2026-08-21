# 🛡️ CyberSec Portfolio Dashboard

Um dashboard interativo e profissional desenvolvido em **Python com Dash**, construído para atuar como um portfólio pessoal e apresentar uma análise de dados focada no mercado de Cibersegurança. 

Este projeto foi desenvolvido como parte da avaliação (CP1) da disciplina de Data Science and Statistical Computing do curso de Engenharia de Software da FIAP.

## 🚀 Funcionalidades

O painel é dividido em quatro seções principais acessíveis através de uma barra de navegação lateral fixa:

*   **👤 Quem sou eu:** Apresentação profissional detalhada, destacando vivência com infraestrutura, desenvolvimento de software e foco em Cibersegurança. Inclui links rápidos para LinkedIn, GitHub e E-mail.
*   **🎓 Qualificações:** Uma grade de cards interativos. Ao clicar na logo de uma instituição (FIAP, SENAI, Alura, ETIP), um modal central (pop-up) é aberto detalhando os aprendizados daquela formação.
*   **💻 Skills:** Um painel imponente utilizando barras de progresso animadas e badges (etiquetas) para ilustrar o nível de domínio em linguagens de programação (Java, C#, Python, C++, React), sistemas (Ubuntu/Linux), infraestrutura (Docker) e versionamento (Git/GitHub).
*   **📊 Análise de Dados:** Apresenta gráficos interativos (linhas e barras) gerados com Plotly, baseados na planilha `Cybersecurity_Investment_Dataset_2020_2024.xlsx`, ilustrando o crescimento dos aportes financeiros no setor de segurança da informação global.

## 🛠️ Tecnologias Utilizadas

*   **Linguagem Principal:** Python 3.x
*   **Framework Web:** Dash (by Plotly)
*   **Estilização e UI:** Dash Bootstrap Components (Tema DARKLY)
*   **Manipulação de Dados:** Pandas
*   **Visualização de Dados:** Plotly Express

## 📁 Estrutura do Projeto

Para que o aplicativo funcione perfeitamente, os arquivos devem estar organizados da seguinte maneira no seu computador:

```text
seu_projeto/
│
├── app.py (ou cp1.py - Código principal do dashboard)
├── Cybersecurity_Investment_Dataset_2020_2024.xlsx (Base de dados)
│
└── assets/                        # PASTA OBRIGATÓRIA PARA IMAGENS
    ├── IMG-20250916-WA0410.jpg    # Foto de perfil
    ├── images (7).png             # Logo FIAP
    ├── logo-senai-cor-1.jpg       # Logo SENAI
    ├── 4975968.png                # Logo Alura
    └── images (8).png             # Logo ETIP
