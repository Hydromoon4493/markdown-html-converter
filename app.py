from flask import Flask, request, render_template_string
from markdown import markdown

app = Flask(__name__)

@app.route('/')
def index():
    return render_template_string(open('index.html').read())

@app.route('/convert', methods=['POST'])
def convert():
    plain_text = request.form['plain_text']
    format_choice = request.form['format']

    if format_choice == 'html':
        # Convert plain text to HTML (simple conversion)
        result = "<p>{}</p>".format(plain_text.replace('\n', '</p><p>'))
    elif format_choice == 'markdown':
        # Convert plain text to Markdown (using a markdown library)
        result = markdown(plain_text)

    return render_template_string(open('index.html').read() + f"<div><h2>Result:</h2><pre>{result}</pre></div>")

if __name__ == '__main__':
    app.run(debug=True)
