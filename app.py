from flask import Flask, request, render_template, jsonify
from predict_zillow_value import predict_home_value

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form data safely
        form_data = request.form

        # Extract and validate fields
        try:
            #features = [bedrooms, bathrooms, sqft_living, sqft_lot, floors, zipcode]
            bedrooms = float(form_data['bedrooms'])
            bathrooms = float(form_data['bathrooms'])
            sqft_living = float(form_data['sqft_living'])
            sqft_lot = float(form_data['sqft_lot'])
            floors = float(form_data['floors'])
            zipcode = int(form_data['zipcode'])

            # Optional: additional validation
            if bedrooms < 0 or bathrooms < 0 or sqft_living <= 0 or sqft_lot <= 0 or floors <= 0:
                return render_template('index.html', error="Invalid values: all values must be positive.")

        except ValueError:
            return render_template('index.html', error="Please enter valid numeric values.")

        # Feature list for prediction
        features = [bedrooms, bathrooms, sqft_living, sqft_lot, floors, zipcode]

        # Call prediction
        predicted_price = predict_home_value(features)
        formatted_price = f"${predicted_price:,.2f}"

        return render_template('index.html', prediction_text=f"Estimated Home Value: {formatted_price}")

    except Exception as e:
        return render_template('index.html', error=f"Error occurred: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)
