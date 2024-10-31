from flask import Flask, request, send_file, jsonify
from io import BytesIO
import markdown2

app = Flask(__name__)

@app.route('/convert', methods=['POST'])
def convert_text():
    data = request.json
    text = data.get("text", "")
    format_type = data.get("format", "html")

    output = BytesIO()
    filename = "converted_text"

    if format_type == "html":
        output_text = f"<html><body><p>{text.replace('\n', '<br>')}</p></body></html>"
        output.write(output_text.encode("utf-8"))
        filename += ".html"
    else:
        markdown_text = markdown2.markdown(text)
        output.write(markdown_text.encode("utf-8"))
        filename += ".md"

    output.seek(0)
    return send_file(output, as_attachment=True, download_name=filename, mimetype="text/plain")

if __name__ == '__main__':
    app.run(debug=True)
