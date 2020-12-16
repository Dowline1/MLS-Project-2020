# Neural networks
import tensorflow.keras as kr
import pandas as pd
import numpy as np

# Read Dataset into Dataframe
power_data = pd.read_csv("Resources/power_dataset.csv")

# Speed = 0 & Power = 0
clean_data = power_data[(power_data["speed"]==0) & (power_data["power"]==0)]

# Speed > 0 & Power > 0
non_zero = power_data[(power_data["speed"]>0) & (power_data["power"]>0)]

# Combine Data
clean_data = clean_data.append(non_zero)

# Sigmoid Neural Network Model Class
#-------------------------------------------------------------------------------#
class SigmoidModel:
    def sigmoidPrediction(x):         
        # Train Model using Sigmoid Activation which most closely matches data
        model = kr.models.Sequential()
        
        # Use 50 Sigmoid Neuron Layer
        model.add(kr.layers.Dense(50, input_shape=(1,), activation='sigmoid', kernel_initializer="glorot_uniform", bias_initializer="glorot_uniform"))
        
        # Use Single Linear Layer to ensure numbers align with raw data else will stay < 1
        model.add(kr.layers.Dense(1, activation='linear', kernel_initializer="glorot_uniform", bias_initializer="glorot_uniform"))
        model.compile(kr.optimizers.Adam(lr=0.001), loss='mean_squared_error')

        # Fit the data/Train Model
        # Trys to get lowest cost score by small changes
        model.fit(clean_data['speed'], clean_data['power'], epochs=500, batch_size=10)

        # Make Prediction Using Wind Speed
        prediction = model.predict([x])

        # Stores elemtent of array as variable so can be returned
        result = round(np.ndarray.item(prediction[0]),2)

        return {"value": result}