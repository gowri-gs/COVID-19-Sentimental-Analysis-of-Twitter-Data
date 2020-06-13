# COVID-19-Sentimental-Analysis-of-Twitter-Data
A predictive analysis to know people’s sentiment towards the epidemic

PRE-REQUISITES:
XAMPP
PyCharm IDE

----------------------------------------------------------------------------------------------------------------------------------------

EXECUTION:
The overall output for COVID-19 Sentimental Analysis can be seen by opening index.html

To see the output data for individual dataset run the python code and view the description below.

----------------------------------------------------------------------------------------------------------------------------------------

When cloned, contains  
	index.html --> Webpage
	index.js --> javascript file
	style.css --> CSS file
	feedbackcovid -->php file
	Database_screenshot --> A screenshot of the database.
	indiafights, lockdown 5.0, lockdownrx, mentalhealth, promote, Quarantine, social, unlock 1.0  -->  Input for the lightbox (Lightbox is a script used to overlay images on the current page. It's a snap to setup and works on all modern browsers.)
	lightbox.html -->Displays only the lightbox.

***************************************************************************************************************************************

We used XAMPP as our local webserver and MySQL database.
When the 'Tweet' button is clicked, it redirects only if Apache server in XAMPP is started.
Apache is a HTTP server.

****************************************************************************************************************************************

Python codes folder contains all the python codes, dataset(10 days) and the output csv files.
	docemo.py --> Gives docemo.csv as output which contains the positive, negative, neutral, sadness, joy, fear, anger, disgust final analytical output for 10 days dataset.
	toneanal.py --> Gives catop.csv as output which has the final analytical output for 10 days dataset categorised based on the pre-defined categories.
	When docemo.py is executed, enter the csv file (Eg: doc2020-04-01) and its output is appended in docemo.csv
	When toneanal.py is executed, enter the csv file (Eg: doc2020-04-01) and its output is appended in catop.csv
	
	piegraph.py --> Takes docemo.csv as input and piechart is the output.
	linegraph.py --> Takes docemo.csv as input and line graph is the output.
	emograph.py --> Takes catop.csv and result1.csv is created from catop.csv and bar graph is the output.
	docemo.csv --> Contains the positive, negative, neutral, sadness, joy, fear, anger, disgust final analytical output for 10 days dataset.
	catop.csv -->Has the final analytical output for 10 days dataset categorised based on the pre-defined categories.
	result1.csv -->Mean value of the categories in catop.csv.

----------------------------------------------------------------------------------------------------------------------------------------

Documentation folder contains all the descriptive content, Roadmap presentation, image for the COVID-19 Sentimental Analysis.





