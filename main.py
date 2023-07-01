
from flask import Flask, render_template, request, redirect, url_for, flash, session


import os

project_root = os.path.dirname(os.path.abspath(__file__))


app = Flask(__name__)
app.config['SECRET_KEY'] = '12346890-239810'



@app.route('/', methods={"GET", "POST"})
def home():
    if request.method == "POST":
        df = request.form.to_dict()
        # Check if the file is read-only
        if not os.access(f"{project_root}/data/file.txt.txt", os.W_OK):
            # Change the file permissions to allow write access
            os.chmod(f"{project_root}/data/file.txt.txt", 0o644)  # Provide the desired file permissions

        with open(file=f"{project_root}/data/file.txt.txt", mode='a') as file:
            file.write(str(df))
        print(df)
        return render_template("error.html")
    if request.method == "GET":
        return render_template("index.html")





app.run(host='0.0.0.0', port=81)



