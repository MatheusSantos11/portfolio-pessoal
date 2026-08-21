import dash
from dash import dcc, html, Input, Output, State, MATCH
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
import os

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY, dbc.icons.BOOTSTRAP], suppress_callback_exceptions=True)
app.title = "Matheus Santos - Portfolio"

# ==========================================
# 1. TRATAMENTO DOS DADOS (Dataset do CP1)
# ==========================================
arquivo_excel = 'Cybersecurity_Investment_Dataset_2020_2024.xlsx'
if os.path.exists(arquivo_excel):
    df = pd.read_excel(arquivo_excel)
else:
    df = pd.DataFrame({
        'Ano': [2020, 2021, 2022, 2023, 2024],
        'Investimento_Total_Bilhão': [45.2, 53.8, 67.5, 82.1, 95.4],
        'Fintech': [15.0, 18.2, 22.1, 27.5, 31.0],
        'Cloud': [12.2, 15.8, 20.4, 25.1, 30.2],
        'Health SEC': [8.0, 9.5, 12.0, 15.5, 18.7],
        'Gov SEC': [10.0, 10.3, 13.0, 14.0, 15.5]
    })

cores_profissionais = ['#00bc8c', '#3498db', '#f39c12', '#e74c3c']

fig_linha = px.line(
    df, x='Ano', y='Investimento_Total_Bilhão', 
    title='Escalada Global de Investimentos em Cibersegurança (2020-2024)',
    markers=True, template='plotly_dark',
    color_discrete_sequence=['#00bc8c']
)
fig_linha.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font=dict(color='white'))

df_barras = df.melt(id_vars=['Ano', 'Investimento_Total_Bilhão'], 
                    value_vars=['Fintech', 'Cloud', 'Health SEC', 'Gov SEC'],
                    var_name='Setor', value_name='Investimento')
df_barras_2024 = df_barras[df_barras['Ano'] == 2024]

fig_barras = px.bar(
    df_barras_2024, x='Setor', y='Investimento', 
    title='Distribuição de Aportes por Setor (2024)',
    template='plotly_dark',
    color='Setor',
    color_discrete_sequence=cores_profissionais
)
fig_barras.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font=dict(color='white'))

# ==========================================
# 2. ESTILOS DA BARRA LATERAL E CONTEÚDO
# ==========================================
SIDEBAR_STYLE = {
    "position": "fixed", "top": 0, "left": 0, "bottom": 0, "width": "18rem",
    "padding": "2rem 1rem", "background-color": "#1a1a1a" 
}
CONTENT_STYLE = {
    "margin-left": "19rem", "margin-right": "2rem", "padding": "2rem 1rem",
}

sidebar = html.Div([
    html.Div([
        html.Img(src="assets/IMG-20250916-WA0410.jpg", 
                 style={"width": "150px", "borderRadius": "50%", "marginBottom": "15px", "border": "3px solid #00bc8c"}),
        html.H4("Matheus Santos", className="text-white"),
        html.P("Engenharia de Software", className="text-light"),
    ], className="text-center"),
    html.Hr(style={"borderColor": "white"}),
    dbc.Nav([
        dbc.NavLink([html.I(className="bi bi-person me-2"), "Quem sou eu"], href="/", active="exact"),
        dbc.NavLink([html.I(className="bi bi-award me-2"), "Qualificações"], href="/qualificacoes", active="exact"),
        dbc.NavLink([html.I(className="bi bi-code-slash me-2"), "Skills"], href="/skills", active="exact"),
        dbc.NavLink([html.I(className="bi bi-graph-up me-2"), "Análise de Dados"], href="/analise", active="exact"),
    ], vertical=True, pills=True, className="mt-4"),
], style=SIDEBAR_STYLE)

# ==========================================
# 3. PÁGINAS DO SISTEMA
# ==========================================

# Página: Quem sou eu
page_sobre = html.Div([
    html.Img(
        src="https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?q=80&w=1000&auto=format&fit=crop", 
        style={"width": "100%", "height": "250px", "objectFit": "cover", "borderRadius": "10px", "marginBottom": "30px", "opacity": "0.8"}
    ),
    html.H2("Sobre mim", className="mb-4 text-info"),
    html.P(
        "Olá! Meu nome é Matheus Santos de Oliveira, tenho 19 anos e sou um entusiasta de tecnologia em todas as suas camadas. "
        "Atualmente, curso Engenharia de Software na FIAP, mas a minha jornada na área começou no 'mundo físico'. Desde cedo, "
        "desenvolvi uma forte paixão por hardware e montagem de setups de alto desempenho. Esse interesse me levou a concluir o "
        "curso técnico em manutenção eletroeletrônica no SENAI, uma base fundamental que ainda hoje me ajuda a otimizar minhas próprias máquinas "
        "e entender a computação direto na raiz.",
        className="lead text-justify text-light mb-4"
    ),
    html.P(
        "No universo do software, encontrei minha verdadeira vocação. No meu dia a dia, utilizo o ambiente Ubuntu como meu ecossistema principal "
        "para arquitetar, compilar e testar soluções em linguagens como Java, C#, C++ e Python. Sou movido por desafios lógicos, seja "
        "estruturando a rede e as portas de um servidor local para multiplayer, explorando a criação de modelos 3D no Autodesk Maya, ou "
        "gerenciando serviços no meu próprio Umbrel.",
        className="lead text-justify text-light mb-4"
    ),
    html.P(
        "Meu grande objetivo atual é conquistar uma posição como Engenheiro de Software Júnior para construir soluções de impacto em escala corporativa. "
        "Acredito que minha visão holística — que transita entre a infraestrutura de rede, o hardware e as linhas de código — me permite "
        "desenvolver sistemas não apenas eficientes, mas blindados. É com essa mentalidade que busco consolidar minha carreira com um foco inabalável em Cibersegurança.",
        className="lead text-justify text-light mb-5"
    ),
    html.Hr(style={"borderColor": "#444"}),
    
    html.H4("Contatos Profissionais", className="text-info text-center mb-4 mt-4"),
    html.Div([
        dbc.Button(
            [html.I(className="bi bi-linkedin me-2"), "LinkedIn"], 
            href="https://www.linkedin.com/in/matheus-santos-809a43225", 
            target="_blank", 
            color="primary", 
            className="me-3 px-4 py-2"
        ),
        dbc.Button(
            [html.I(className="bi bi-github me-2"), "GitHub"], 
            href="https://github.com/MatheusSantos11", 
            target="_blank", 
            style={"backgroundColor": "#333", "borderColor": "#555", "color": "white"},
            className="me-3 px-4 py-2"
        ),
        dbc.Button(
            [html.I(className="bi bi-envelope-fill me-2"), "E-mail"], 
            href="mailto:Matheus.soliveira11@hotmail.com", 
            color="info", 
            className="px-4 py-2"
        ),
    ], className="d-flex justify-content-center mb-5")
])

# Função para criar os Cards Modais (Qualificações)
def criar_card_modal(id_index, titulo, instituicao, ano, descricao, arquivo_imagem):
    return html.Div([
        dbc.Card([
            dbc.Button([
                html.Div(
                    html.Img(src=f"assets/{arquivo_imagem}", style={"height": "120px", "objectFit": "contain", "width": "100%", "padding": "10px"}),
                    style={"backgroundColor": "#111"}
                ),
                dbc.CardBody([
                    html.H5(titulo, className="text-info mb-1", style={"fontWeight": "bold", "fontSize": "1rem"}),
                    html.Small(f"{instituicao} | {ano}", className="text-light"),
                ], style={"backgroundColor": "#222", "textAlign": "left", "padding": "15px"})
            ],
            id={'type': 'card-abrir', 'index': id_index},
            style={"padding": "0", "border": "none", "width": "100%", "height": "100%", "textAlign": "left", "cursor": "pointer"},
            color="dark"
            )
        ], className="mb-4 shadow h-100", style={"borderColor": "#444", "overflow": "hidden"}),

        dbc.Modal([
            dbc.ModalHeader(dbc.ModalTitle("Detalhes da Qualificação", className="text-info")),
            dbc.ModalBody([
                html.Div(
                    html.Img(src=f"assets/{arquivo_imagem}", style={"height": "100px", "objectFit": "contain"}), 
                    style={"textAlign": "center", "marginBottom": "20px", "backgroundColor": "#111", "padding": "15px", "borderRadius": "5px"}
                ),
                html.H4(titulo, className="text-white text-center mb-2"),
                html.H6(f"{instituicao} | {ano}", className="text-muted text-center mb-4"),
                html.P(descricao, className="text-light text-justify", style={"fontSize": "1.1rem"}),
            ]),
            dbc.ModalFooter(
                dbc.Button("Fechar", id={'type': 'card-fechar', 'index': id_index}, color="danger", n_clicks=0)
            ),
        ],
        id={'type': 'card-modal', 'index': id_index},
        is_open=False,
        centered=True, 
        size="lg"
    )
    ], style={"height": "100%"})

# Página: Qualificações
page_qualificacoes = html.Div([
    html.H2("Minhas Qualificações", className="mb-2 text-info"),
    html.P("Clique nos cards para expandir os detalhes de cada formação.", className="text-light mb-4"),
    
    dbc.Row([
        dbc.Col(criar_card_modal(
            1, "Graduação em Engenharia de Software", "FIAP", "Em andamento", 
            "Foco intensivo em arquitetura de sistemas, metodologias ágeis, orientação a objetos e desenvolvimento em backend para criar softwares escaláveis. Durante a graduação, tenho desenvolvido projetos práticos colaborativos e aprimorado minhas habilidades lógicas em linguagens de mercado como Java, Python e C++. O curso tem sido fundamental para consolidar minha base teórica e prática, me preparando para atuar como Engenheiro de Software Júnior em ambientes corporativos de alta exigência.",
            "images (7).png"
        ), md=4, className="mb-3"),
        dbc.Col(criar_card_modal(
            2, "Especialização em Segurança de Dados", "FIAP", "2026", 
            "Estudo aprofundado em técnicas de proteção da informação, criptografia, prevenção de intrusões (SQLi, XSS) e políticas de acesso corporativas. A especialização abrange desde a segurança em infraestruturas e redes até o hardening de sistemas operacionais, aliando meu conhecimento prático em ambientes Linux (Ubuntu) com as melhores práticas de defesa cibernética exigidas pelas grandes empresas de tecnologia.",
            "images (7).png"
        ), md=4, className="mb-3"),
        dbc.Col(criar_card_modal(
            3, "Técnico de Manutenção Eletroeletrônica", "SENAI", "2024", 
            "Compreensão avançada sobre circuitos, eletricidade e eletrônica. Uma base vital que me permite entender a computação desde os pulsos físicos até o processamento lógico. Este curso desenvolveu minha capacidade de troubleshooting de hardware, montagem e manutenção de equipamentos, habilidades que utilizo frequentemente na otimização de setups de alto desempenho e no diagnóstico preciso de falhas em nível físico.",
            "logo-senai-cor-1.jpg"
        ), md=4, className="mb-3"),
    ], className="d-flex align-items-stretch"),
    
    dbc.Row([
        dbc.Col(criar_card_modal(
            4, "Curso Avançado de C#", "Alura", "Concluído", 
            "Domínio da sintaxe e da arquitetura .NET para a construção de soluções corporativas, APIs estruturadas e manipulação segura de dados. O treinamento focou no desenvolvimento backend sólido, aplicando conceitos avançados de Orientação a Objetos e boas práticas de estruturação de código, essenciais para a criação de aplicações escaláveis, robustas e seguras.",
            "4975968.png"
        ), md=4, className="mb-3"),
        dbc.Col(criar_card_modal(
            5, "Ensino Médio Técnico em Informática", "Centro Educacional ETIP", "Concluído", 
            "Formação que uniu o currículo do ensino médio com conhecimentos técnicos aprofundados em informática, estruturando a base de lógica de programação para a minha entrada definitiva na área de tecnologia. Foi neste período que consolidei meus primeiros contatos reais com desenvolvimento, banco de dados e infraestrutura, criando a disciplina técnica necessária para evoluir no ecossistema de TI.",
            "images (8).png"
        ), md=4, className="mb-3"),
    ], className="d-flex align-items-stretch")
])

# Página: Skills (TOTALMENTE REFORMULADA PARA PREENCHER A TELA)
page_skills = html.Div([
    html.H2("Competências Técnicas", className="mb-4 text-info"),
    html.P("Um panorama do meu ecossistema de desenvolvimento, ferramentas e nível prático em cada tecnologia.", className="text-light mb-4"),

    dbc.Row([
        # Coluna 1: Linguagens (Barras de Progresso Animadas)
        dbc.Col(dbc.Card([
            dbc.CardHeader(html.H5([html.I(className="bi bi-code-slash me-2"), "Stack de Desenvolvimento"], className="text-info m-0")),
            dbc.CardBody([
                html.Div("Java & C# (.NET)", className="text-light mb-1 fw-bold"),
                dbc.Progress(value=85, color="success", className="mb-4", style={"height": "14px"}, animated=True, striped=True),
                
                html.Div("Python & C++", className="text-light mb-1 fw-bold"),
                dbc.Progress(value=75, color="info", className="mb-4", style={"height": "14px"}),
                
                html.Div("React.js & JavaScript / TypeScript", className="text-light mb-1 fw-bold"),
                dbc.Progress(value=70, color="warning", className="mb-4", style={"height": "14px"}),
                
                html.Div("SQL (Modelagem e Consultas)", className="text-light mb-1 fw-bold"),
                dbc.Progress(value=80, color="danger", className="mb-4", style={"height": "14px"}),
                
                html.Div("HTML5, CSS3 & Node.js", className="text-light mb-1 fw-bold"),
                dbc.Progress(value=85, color="primary", className="mb-2", style={"height": "14px"}),
            ])
        ], className="shadow mb-4 h-100", style={"backgroundColor": "#222", "borderColor": "#444"}), md=6),

        # Coluna 2: Infra, Ferramentas e Versionamento (Badges/Etiquetas)
        dbc.Col(dbc.Card([
            dbc.CardHeader(html.H5([html.I(className="bi bi-pc-display me-2"), "Sistemas, Infraestrutura & Versionamento"], className="text-info m-0")),
            dbc.CardBody([
                # Destaque absoluto para GIT e GITHUB
                html.P("Controle de Versão e Código-Fonte:", className="text-light mb-2 fw-bold"),
                html.Div([
                    dbc.Badge([html.I(className="bi bi-git me-2"), "Git"], color="danger", className="me-2 mb-3 p-2 fs-6 shadow"),
                    dbc.Badge([html.I(className="bi bi-github me-2"), "GitHub"], color="light", text_color="dark", className="me-2 mb-3 p-2 fs-6 shadow"),
                    dbc.Badge([html.I(className="bi bi-terminal me-2"), "Bash / Shell Script"], color="secondary", className="me-2 mb-3 p-2 fs-6 shadow"),
                ]),
                
                html.Hr(style={"borderColor": "#555"}),
                
                html.P("Infraestrutura & Redes:", className="text-light mb-2 fw-bold"),
                html.Div([
                    dbc.Badge("Ubuntu / Linux", color="warning", text_color="dark", className="me-2 mb-3 p-2 fs-6"),
                    dbc.Badge("Docker / Containers", color="info", className="me-2 mb-3 p-2 fs-6"),
                    dbc.Badge("Hardware (Troubleshooting)", color="success", className="me-2 mb-3 p-2 fs-6"),
                    dbc.Badge("Redes (TCP/IP, Portas)", color="primary", className="me-2 mb-3 p-2 fs-6"),
                    dbc.Badge("Umbrel (Self-hosting)", color="dark", className="border me-2 mb-3 p-2 fs-6"),
                ]),

                html.Hr(style={"borderColor": "#555"}),
                
                html.P("Ferramentas Extras:", className="text-light mb-2 fw-bold"),
                html.Div([
                    dbc.Badge("APIs REST & Postman", color="secondary", className="me-2 mb-2 p-2"),
                    dbc.Badge("Autodesk Maya (3D)", color="secondary", className="me-2 mb-2 p-2"),
                    dbc.Badge("Metodologias Ágeis (Scrum)", color="secondary", className="me-2 mb-2 p-2"),
                ])
            ])
        ], className="shadow mb-4 h-100", style={"backgroundColor": "#222", "borderColor": "#444"}), md=6),
    ], className="align-items-stretch"), # Garante que os dois cards tenham a mesma altura
])

# Página: Análise de Dados
page_analise = html.Div([
    html.H2("Estudo de Mercado: Setor de Segurança", className="mb-3 text-info"),
    html.P("Esta análise extrai dados sobre aportes financeiros e tendências do mercado global de Cibersegurança.", className="text-light"),
    dbc.Row([
        dbc.Col(dbc.Card(dcc.Graph(figure=fig_linha), body=True, style={"backgroundColor": "#333", "borderColor": "#444"}, className="shadow"), md=6),
        dbc.Col(dbc.Card(dcc.Graph(figure=fig_barras), body=True, style={"backgroundColor": "#333", "borderColor": "#444"}, className="shadow"), md=6)
    ])
])

# ==========================================
# 4. CALLBACKS E LAYOUT PRINCIPAL
# ==========================================
app.layout = html.Div([
    dcc.Location(id="url"),
    sidebar,
    html.Div(id="page-content", style=CONTENT_STYLE)
])

@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/": return page_sobre
    elif pathname == "/qualificacoes": return page_qualificacoes
    elif pathname == "/skills": return page_skills
    elif pathname == "/analise": return page_analise
    return html.Div([html.H1("404: Página não encontrada", className="text-danger")])

@app.callback(
    Output({'type': 'card-modal', 'index': MATCH}, 'is_open'),
    [Input({'type': 'card-abrir', 'index': MATCH}, 'n_clicks'),
     Input({'type': 'card-fechar', 'index': MATCH}, 'n_clicks')],
    [State({'type': 'card-modal', 'index': MATCH}, 'is_open')]
)
def toggle_modal(n_abrir, n_fechar, is_open):
    if n_abrir or n_fechar:
        return not is_open
    return is_open

if __name__ == '__main__':
    app.run(debug=True)