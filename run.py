from flask import Flask, request, render_template, redirect, url_for, send_file
from googleform import get_fields, spam_form

app = Flask(__name__)

@app.route('/', methods=["GET","POST"])
def index():
    return redirect(url_for('gform'))

@app.route('/gform', methods=["GET","POST"])
def gform():
    if request.method=="GET":
        return render_template("gform_get.html")
    if request.method=="POST":
        link = request.form['link']
        fields = get_fields(link)
        return render_template("gform_post.html", fields = fields)

@app.route('/gform_send', methods=["POST"])
def gform_send():
    response = request.form.to_dict()
    spam_form(response)
    return redirect('/gform')

if __name__ == "__main__":
    app.run(host="192.168.1.1", port="1242", debug=True)