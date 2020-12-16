# MLS-Project-2020
Repository for Machine Learning &amp; Statistics Module Project 2020 - Wind Turbine Power Production 

## If you have Python Installed
1. Click this [link](https://github.com/Dowline1/MLS-Project-2020) for my Github repository.
2. Click the download button to save a copy of the repository on your machine.
3. Make sure you have Python installed including, if you require installation please follow instructions in this [link](https://www.anaconda.com/distribution/) to download Python via Anaconda.
4. Use your command line such as CMDER to navigate to the folder housing the Git repository, download for CMDER found via this [link](https://cmder.net/).
5. Ensure you have Flask installed on your machine, to install use "pip install Flask".
6. Once in the folder type the command "python server.py" and click enter.
7. This will launch the server on your machine, open a webbrowser and go to address: "http://127.0.0.1:5000/".


## If you don't have Python Installed
1. Click this [link](https://github.com/Dowline1/MLS-Project-2020) for my Github repository.
2. Click the download button to save a copy of the repository on your machine.
3. Make sure you have Python installed including, if you require installation please follow instructions in this [link](https://www.anaconda.com/distribution/) to download Python via Anaconda.
4. Use your command line such as CMDER to navigate to the folder housing the Git repository, download for CMDER found via this [link](https://cmder.net/).
5. Ensure you have Flask installed on your machine, to install use "pip install Flask".
6. Ensure Docker is installed on your machine to create image, download found at this [link](https://www.docker.com/products/docker-desktop).
7. Once in the folder type the command "docker build -t mls-project ." which will build an image of the docker environment, note this can take some time to complete.
8. After the Docker image has been created use command "docker run --name mls-container -d -p 5000:5000 mls-project", which will create the container on your system.
9. Now that the container is running on your machine it can be accessed in a web browser at "http://127.0.0.1:5000/".