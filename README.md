# Airbnb Fare Finder

An Airbnb Fare Finder bot lists all apartments/hotels/rooms from [Airbnb](https://www.airbnb.com) database to [Google Sheets](https://docs.google.com/). 

<p align="center">
  <img src="https://i.ibb.co/rH6CY3L/airbnb-fare-finder.png" alt="airbnb-bot"/>
</p>


# Installing
Download the [Python 3](https://python.org) installer package from the official website and install it, if not installed previously.

* Run the following in the terminal to install the modules to run your program without excussions.
```
pip install selenium
```

Also to use this bot, you should download and install [Google Chrome](https://www.google.com/intl/en_uk/chrome/) web browser and [Chrome Web Driver](https://chromedriver.chromium.org/downloads) here.

# How to Use?

Download the source code from the repository and run the file just as any other Python script (.py) file.
```
python3 main.py
```

* Note! For the code to work you need to fill the information where would you like to go to trip?. e.g. ```CITY```, ```CHECK_IN_DATE```,```CHECK_OUT_DATE```,```MAX_PRICE```,```GUESTS_NUMBER```,.

Follow these instructions below.

1. Decide about where would you like to go and how many days you would like to stay.

2. Fill the blanks in the code.

3. Go to https://docs.google.com/forms/ and create your own form.

<p align="center">
  <img src="https://i.ibb.co/ZdQcw10/blank-google-form.png" alt="blank-google-form"/>
</p>

4. Add these questions to the form, make all questions "short-answer".

* ```What's the name of the apartment? ```

* ```What's the price per night?```

* ```What's the link to the apartment? ```

* ```What is the review of the apartment? ```

<p align="center">
  <img src="https://i.ibb.co/NC87PmN/airbnb-google-form.png" alt="airbnb-google-form"/>
</p>

5. Click send and copy the link address of the form. Replace it on the code ```GOOGLE_FORMS_LINK``` section.

<p align="center">
  <img src="https://i.ibb.co/tpBdt8w/copy-link-google-form.png" alt="airbnb-google-form"/>
</p>

6. Now you can run the code with instructions above.

For further informations check out the articles.

# Documentations

* [Selenium](https://www.selenium.dev)
* [Airbnb](https://www.airbnb.com)
* [Google Chrome Download](https://docs.python.org/3/library/smtplib.html)
* [Chrome Driver](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
