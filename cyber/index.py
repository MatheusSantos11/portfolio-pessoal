from app import app as dash_app

# Aqui entregamos o servidor Flask puro para a variável 'app' que o Vercel exige
app = dash_app.server