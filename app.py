from flask import Flask, render_template, request
from markdown import markdown

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    html_output = ""
    markdown_output = ""
    user_input = ""  # Ensuring it starts as an empty string

    if request.method == "POST":
        user_input = request.form.get("input_text", "")
        
        # Convert to HTML
        html_output = f"<p>{user_input}</p>"

        # Convert to Markdown
        markdown_output = markdown(user_input)

    return render_template(
        "index.html",
        user_input=user_input,
        html_output=html_output,
        markdown_output=markdown_output
    )

if __name__ == "__main__":
    app.run(debug=True)
