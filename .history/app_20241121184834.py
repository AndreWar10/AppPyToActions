from flask import Flask, render_template_string

app = Flask(__name__)

# Template HTML atualizado com novo design
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flask App - Andre War</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background: linear-gradient(135deg, #ff9a9e, #fad0c4);
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            color: #333;
        }
        .container {
            text-align: center;
            background: #ffffffdd;
            padding: 40px;
            border-radius: 15px;
            box-shadow: 0 8px 15px rgba(0, 0, 0, 0.2);
        }
        h1 {
            color: #ff6f61;
            font-size: 2.5em;
            margin-bottom: 10px;
        }
        p {
            font-size: 1.3em;
            margin-bottom: 20px;
        }
        .btn {
            display: inline-block;
            padding: 12px 25px;
            font-size: 1.1em;
            color: white;
            background: #ff6f61;
            border: none;
            border-radius: 25px;
            text-decoration: none;
            cursor: pointer;
            transition: background 0.3s ease, transform 0.2s ease;
        }
        .btn:hover {
            background: #e55a50;
            transform: scale(1.05);
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Bem-vindo!</h1>
        <p>Andre War - Teste de GitHub Actions</p>
        <a class="btn" href="#">Clique Aqui</a>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8106)