from model import generate_prediction
from flask import Flask, render_template, request, jsonify,redirect, url_for
from flask_login import login_user, current_user,LoginManager, UserMixin, login_required


app = Flask(__name__)
prediction_data = []

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/home')
def home():
    return render_template('index.html')
@app.route('/generate_prediction', methods=['POST'])
def handle_generate_prediction():
    try:
        age = float(request.json['age'])
        salary = float(request.json['salary'])
        prediction = generate_prediction(age, salary)
        pred = 'purchased' if prediction == 1 else 'Not purchased'

        prediction_data.append({'age': age, 'salary': salary, 'prediction': pred})

        # Include prediction in JSON response along with redirect
        return jsonify({'prediction': prediction})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to render the HTML template
@app.route('/show_data')
def show_data():
    # Retrieve prediction from query parameter
    prediction_json = request.args.get('prediction', default='{}')
    prediction = jsonify(prediction_json)

    return render_template('show_data.html', prediction_data=prediction_data, prediction=prediction)

@app.route('/login', methods=['POST'])
def login():
    # Récupérez les données du formulaire
    username = request.form.get('username')
    password = request.form.get('password')

    # Vérifiez les informations d'identification (remplacez cela par une vérification sécurisée en production)
    if username == 'admin' and password == 'admin':
        return redirect(url_for('home'))
    
    else:
        mistake = 'Invalid credentials'
        return render_template('login.html', error=mistake)




if __name__ == '__main__':
    app.run(debug=True)







