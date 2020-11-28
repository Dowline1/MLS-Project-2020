import flask as fl
from linearModel import LinearModel as lm

# Create Web App
app = fl.Flask(__name__, static_url_path = '', static_folder = 'staticpages')

@app.route('/')
def home():
    return app.send_static_file('index.html')


@app.route('/api/linearmodelnc')
def index():
    return lm.nc_linear_input(20)



if __name__ == "__main__":
    app.run(debug = True)