from flask import Flask, request, render_template_string

app = Flask(__name__)

# Simple HTML form
html_form = """
    <form method="POST" enctype="multipart/form-data">
        <input type="file" name="clothing" accept="image/*">
        <input type="submit" value="Upload">
    </form>
"""

@app.route("/", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        file = request.files["clothing"]
        if file:
            file.save(f"uploads/{file.filename}")  # save image to folder
            return f"Uploaded {file.filename}"
    return render_template_string(html_form)

if __name__ == "__main__":
    app.run(debug=True)

