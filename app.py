from flask import Flask, request, render_template
import pickle
import pandas as pd

app = Flask(__name__, template_folder='./templates', static_folder='./static')

# Load the trained model
Pkl_Filename = "rf_tuned_6.pkl"
with open(Pkl_Filename, 'rb') as file:
    model = pickle.load(file)

# Define model columns (after one-hot encoding)
model_columns = ['age', 'bmi', 'children', 'sex_1', 'smoker_1', 'region_1', 'region_2', 'region_3']

@app.route('/')
def home():
    return render_template('home.html')
@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Collect form inputs
        age = request.form.get('age')
        sex = request.form.get('Gender')  # 0-Male, 1-Female
        bmi = request.form.get('bmi')
        children = request.form.get('children')
        smoker = request.form.get('smoker')  # 0-No, 1-Yes
        region = request.form.get('region')  # 0-NW, 1-NE, 2-SE, 3-SW

        # Check for missing inputs
        if None in [age, sex, bmi, children, smoker, region] or '' in [age, sex, bmi, children, smoker, region]:
            return render_template('op.html', pred="Please enter all 6 features.")

        # Convert numeric
        age = float(age)
        bmi = float(bmi)
        children = float(children)
        sex = int(sex)
        smoker = int(smoker)
        region = int(region)

        # Create DataFrame
        df = pd.DataFrame([[age, bmi, children, sex, smoker, region]], 
                          columns=['age', 'bmi', 'children', 'sex', 'smoker', 'region'])

        # One-hot encode categorical features
        df_encoded = pd.get_dummies(df, columns=['sex', 'smoker', 'region'], drop_first=True)

        # Align columns with model
        df_encoded = df_encoded.reindex(columns=model_columns, fill_value=0)

        # Predict
        pred = model.predict(df_encoded)[0]

        # Format result
        result = f"Expected amount is {pred:.2f}" if pred >= 0 else "Error calculating amount!"

        # Render the result page (op.html)
        return render_template('op.html', pred=result)

    except Exception as e:
        return render_template('op.html', pred=f"An error occurred: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)
