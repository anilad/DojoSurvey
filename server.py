from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = 'keepitsecretkeepitsafe'

@app.route('/')
def survey():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    isValid= False
    if len(request.form['name'])<1:
        flash('Name cannot be empty!')
        isValid = True
    else:
        name = request.form['name'] 

    if request.form['location']=="None":
        flash('Location cannot be empty!')
        isValid = True
    else:
        location = request.form['location']

    if request.form['language'] == "None":
        flash('Language cannot be empty!')  
        isValid = True 
    else:
        language = request.form['language']

    if len(request.form['comments'])>120:
        flash('Comments cannot be greater than 120 characters!')   
        isValid = True
    else:
        comments = request.form['comments']
    print isValid
    if isValid:
        return redirect('/')        
    else:
        
        return render_template('results.html', name = name, location = location, language = language, comments = comments)

app.run(debug=True)
