from flask import Flask, render_template, jsonify
import pickle as pkl

app = Flask(__name__)
xrf_model = pkl.load(open('./data/nyctaxi_xRF.pkl','rb'))
logreg_model = pkl.load(open('./data/nyctaxi_logreg.pkl','rb'))

@app.route('/')
def index():
    """
    Uses Flask's Jinja2 template renderer to generate the html
    """
    return render_template('index.html')

@app.route('/predict/<trip_array>/1')
def predict(trip_array):
	"""
	Uses a pre-built sklearn SVM predictor to classify a handwritten glyph as
	an alphanumeric digit.
	Input: image_vector=feature vector of integer representing pixel intensity
	Output: JSON object where result=alphanumeric character predicted by model
	"""
	trip_array = map(lambda el: float(el), trip_array.split(","))
	predicted_fare = xrf_model.predict(trip_array)[0]
	return jsonify(result=predicted_fare)

@app.route('/predict/<trip_array>/2')
def predict_proba(trip_array):
	"""
	Uses a pre-built sklearn SVM predictor to classify a handwritten glyph as
	an alphanumeric digit.
	Input: image_vector=feature vector of integer representing pixel intensity
	Output: JSON object where result=alphanumeric character predicted by model
	"""
	trip_array = map(lambda el: float(el), trip_array.split(","))
	predicted_shareable = logreg_model.predict_proba(trip_array)[0]
	return jsonify(result=predicted_shareable[1])
	
if __name__ == '__main__':
    app.run(debug=True)
