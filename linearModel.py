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

# Non-Cleaned Linear Model Class
#-------------------------------------------------------------------------------#
class LinearModel:
    def train_nc_linear_model():
        nc_x = power_data["speed"].to_numpy()
        nc_y = power_data["power"].to_numpy()

        nc_x = nc_x.reshape(-1, 1)

        model = lin.LinearRegression()
        model.fit(nc_x, nc_y)

        return [model.intercept_, model.coef_[0]]

    def nc_linear_model(nc_x, nc_p):
        return nc_p[0] + nc_x * nc_p[1]

    def nc_linear_predict(nc_x):
        return LinearModel.nc_linear_model(nc_x, LinearModel.train_nc_linear_model())

    def nc_linear_input(x):
        wind_speed = x#float(input("Please Enter Wind Speed: "))

        prediction = LinearModel.nc_linear_predict(wind_speed)

        return {"value": prediction}

#LinearModel.nc_linear_input()

#-------------------------------------------------------------------------------#