## Project for General Assembly's Data Science Course
### NYC Yellow Taxi 2013
#### Project Outline
* To predict taxi fare price under different conditions.
* To classify the probability of sharing a ride within 10-minute waiting windows under different conditions.
* To visualize the changes of taxi demand at different pickup and dropoff points under different conditions.

#### The Data
* The taxi dataset contains variables such as pick-up and drop-off points, time of the day, number of passengers, travel time and fare.
* The taxi data can be obtained from http://www.andresmh.com/nyctaxitrips/
* The weather dataset for hourly precipitation can be obtained from http://www.noaa.gov/

#### How It Runs 
* Clone this repository
* In terminal, navigate to the directory of this repo folder on your local machine
* In terminal, type 'python \_\_init\_\_.py'
* Open an internet browser page and type in 'localhost:5000'

#### How It Works
* The machine learning models are trained in Python and exported as pickle .pkl files.
* The taxi fare prediction model is a regression one and the taxi shareabiliy model is a classification one.
* The pickled models are are applied to web pages through Flask, a micro web framework linking Python with HTML, CSS and JavaScript libraries.
* Visualizations on are done with Leaflet and D3, both JavaScript libraries.
