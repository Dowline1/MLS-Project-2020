# Packages required for Model
import pandas as pd
import sklearn.linear_model as lin
import numpy as np

# Read Dataset into Dataframe
power_data = pd.read_csv("Resources/power_dataset.csv")

# Speed = 0 & Power = 0
clean_data = power_data[(power_data["speed"]==0) & (power_data["power"]==0)]

# Speed > 0 & Power > 0
non_zero = power_data[(power_data["speed"]>0) & (power_data["power"]>0)]

# Combine Data
clean_data = clean_data.append(non_zero)

# Linear Model Class
#-------------------------------------------------------------------------------#

# c = Cleansed, nc = Non-Cleansed
class LinearModel:
    # Trains Non-Cleansed Model
    def train_nc_linear_model():
        x = power_data["speed"].to_numpy()
        y = power_data["power"].to_numpy()

        x = x.reshape(-1, 1)

        model = lin.LinearRegression()
        model.fit(x, y)

        return [model.intercept_, model.coef_[0]]

    def nc_linear_model(x, p):
        return p[0] + x * p[1]

    def nc_linear_predict(x):
        return LinearModel.nc_linear_model(x, LinearModel.train_nc_linear_model())

    # Takes input for Non-Cleansed Model
    def nc_linear_input(x):
        wind_speed = x

        prediction = round(LinearModel.nc_linear_predict(wind_speed),2)

        return {"value": prediction}

#-------------------------------------------------------------------------------#

    # Trains Cleansed Model
    def train_c_linear_model():
        x = clean_data["speed"].to_numpy()
        y = clean_data["power"].to_numpy()

        x = x.reshape(-1, 1)

        model = lin.LinearRegression()
        model.fit(x, y)

        return [model.intercept_, model.coef_[0]]

    def c_linear_model(x, p):
        return p[0] + x * p[1]

    def c_linear_predict(x):
        return LinearModel.c_linear_model(x, LinearModel.train_c_linear_model())

    # Takes input for Non-Cleansed Model
    def c_linear_input(x):
        wind_speed = x

        prediction = round(LinearModel.c_linear_predict(wind_speed),2)

        return {"value": prediction}



#-------------------------------------------------------------------------------#