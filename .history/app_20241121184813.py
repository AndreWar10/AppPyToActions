from flask import Flask, render_template_string

app = Flask(__name__)

# Template HTML com CSS embutido
HTML_TEMPLATE = """

"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8108)
