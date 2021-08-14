# Application

The repository contains a Flask application that uses a Flask Blueprint to calculate the distance from a place in the world to the Moscow Ring Road (MKAD) in kilometers.

The application uses the [Distance Matrix API](https://distancematrix.ai) to access the address geolocation information.

## How to run the application

The application can run inside a Docker container and to do that first clone the repository, then enter the new folder and run the commands:

``` shell
docker-compose up -d # If docker-compose is installed or

docker build -t flask_image .
docker run --rm -p 5000:5000 flask_image # If docker-compose is not installed
```

If the user doesn't have Docker installed, it's recommended to create a virtual environment to install the dependencies and run the application. It's also necessary to add the folder of the application to the Python path:

```shell
python -m venv env
source env/bin/activate
export PYTHONPATH="${PYTHONPATH}:/path_to_application"

pip install -r requirements.txt # Installs the dependencies

python app/app.py # Runs the application
```

It's necessary Python version 3.8+.

## How to use the application

The API has only one endpoint, `/distance` and can be accessed in http://localhost:5000. To use this endpoint the user needs to pass the address as query parameter.

Examples:

- `/distance?address=Rio de Janeiro`
- `/distance?address=Novogorsk, Moscow Oblast, Russia`

If no address is passed the application returns not found.

## Application logic

The application uses the latitude and longitude of the MKAD, found in [this link](https://en.wikipedia.org/wiki/Module:Location_map/data/Russia_Moscow_Ring_Road/doc) and uses the [Haversine formula](https://en.wikipedia.org/wiki/Haversine_formula) to calculate the distance from the passed address to MKAD.

To make the logic easier, using the previous information, it is defined that the MKAD region is a circle with a radius of 29.05 km. Then, whenever a distance is calculated, the result is compared with 29.05 to check if place is inside or outside the region.

The API returns the address passed and the distance. All the results are saved in a file `log.log` inside the log folder.

## Tests

The application has unit tests that can be run with the command:

```shell
python -m unittest discover tests
```

P.S: To run the tests, the dependencies need to be installed and the Python path needs to be configured as previous stated.

## Considerations

The .env files are stored in the public repository just for tests purpose, but this is not a good practice and shouldn't be done in a real project.