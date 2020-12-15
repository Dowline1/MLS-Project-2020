import flask as fl
from linearModel import LinearModel as lm
from sigmoid_nn import SigmoidModel as sm

# Create Web App
app = fl.Flask(__name__, static_url_path = '', static_folder = 'staticpages')

@app.route('/')
def home():
    return app.send_static_file('index.html')

# Route Wind Speed Request to Non-Cleansed Linear Model
@app.route('/api/linearmodelnc/<string:windSpeed>')
def linearmodelnc(windSpeed):
    
    # String must be converted to float as cannot pass natively
    # Insight from https://github.com/pallets/flask/issues/315
    windSpeed = float(windSpeed)
    return lm.nc_linear_input(windSpeed)


# Route Wind Speed Request to Non-Cleansed Linear Model
@app.route('/api/linearmodelc/<string:windSpeed>')
def linearmodelc(windSpeed):
    
    # String must be converted to float as cannot pass natively
    # Insight from https://github.com/pallets/flask/issues/315
    windSpeed = float(windSpeed)
    return lm.c_linear_input(windSpeed)


# Trains Sigmoid Model
#@app.route('/api/trainSigmoid')
#def trainSModel():

#    return sm.trainSigmoidModel()


# Route Wind Speed Request to Non-Cleansed Linear Model
@app.route('/api/trainSigmoid/<string:windSpeed>')
def sigmoidModelPredict(windSpeed):
    
    # String must be converted to float as cannot pass natively
    # Insight from https://github.com/pallets/flask/issues/315
    windSpeed = float(windSpeed)
    return sm.trainSigmoidModel(windSpeed)


if __name__ == "__main__":
    app.run(debug = True)