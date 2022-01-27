from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    users = [
        {'first_name' : 'Karen', 'last_name' : 'Reyes'},
        {'first_name' : 'Nataly', 'last_name' : 'Miro'},
        {'first_name' : 'Erick', 'last_name' : 'Castillo'},
        {'first_name' : 'Eduardo', 'last_name' : 'Molina'}
    ]
    return render_template("index.html",users=users)



if __name__=="__main__":
    app.run(debug=True)