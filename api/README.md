# API intro

An API is an Application Programming Interface.

If that acronym doesn't help at all, don't worry.

I'll introduce the concept of an API using a motivating example.

**Scenario**

The host examplex.com (not real) has a website that you can visit where they list the temperature, humidity, barometric pressure, and wind speed at various points around the globe.

On their main page they display these numbers for the city their server is based out of.

So, if you visit
```
https://examplex.com/
```
Then you will see
```
Temp: 28C
Humidity: 33%
Pressure: 10.21kPa
Wind: 4mph
```

They have a search bar where you can type in a city, and they'll give you the numbers of that city.

So, if you visit
```
https://examplex.com/search?q=london
```
You will see
```
Temp: 19C
Humidity: 64%
Pressure: 10.13kPa
Wind: 6mph
```

**Exploration**

After learning about this very nice service at examplex.com you get super excited about the possibilities!  You could write a script that pulls the data on a hundred cities from their website every hour or so and run some analysis on the weather data.

You would have to:
  - Write a script to scrape the HTML from their website
  - Improve the script to programatically use the website's search function
  - Parse the HTML

**Problems**

*Problem 1*.  The search bar is for humans and the URLs often get messy.  There's no guarantee that your search script will work consistently.  You may have to worry about timeout issues, 300 errors (redirects), 400 errors (bad queries), or 500 errors (server error).

*Problem 2*. The HTML may be ungainly to work with.  They might change their website.  The HTML parsers out there work, but  they're usually a hack (or you have to write a custom parser).

*Problem 3*. Some website hosts don't like people writing scripts to scrape their webpages without permission.  They might just ban you.  The problem with *that* is that they will try to ban you by IP address and then you could just change your IP address and scrape again...

**Solution**

A very neat solution to all three of these problems is for the website host to provide an API.

An API is an interface for a programmer (like yourself) to interact with a service or application.

So, instead of visiting their website with a browser, you might instruct your script to request this url:
```
https://examplex.com/api/
```
Then the server will send back a JSON object like this:
```
{"temp": 28, "humidity": 33, "pressure": 10.21, "wind": 4}
```

See [json](../standard_library/json) for more details.

Furthermore, the API host often allows for data to be sent along with the url request.

For example, it might be valid to request this url:
```
https://examplex.com/api/cities
```
...and send this data along with it:
```
{"city": "london"}
```
Then the server would respond with a JSON object:
```
{"temp": 19, "humidity": 64, "pressure": 10.13, "wind": 6}
```

## Example

Here is an actual example (in 5 lines) of a script that interacts with an API.

It contacts the NIST beacon service (this is a website that generates and broadcasts random data every minute).

It uses the `requests` module which does not come with the standard library.  It needs to be installed with `pip install requests`.  I recommend doing this in a virtual environment.

```python
import requests
url = "https://beacon.nist.gov/beacon/2.0/pulse/last"
response = requests.get(url)
data = response.json()
print(data['pulse']['outputValue'])
```

The data that is returned from the server is a dictionary.  The last line prints out a single value, but you can browse the dictionary by printing out the entire object with `print(data)`.

## Authentication

One final word, because we still haven't really addressed all of the problems.

An API allows for authentication.  The API host can issue tokens to users who *must* present those tokens along with any API request in order to use the service.  This way the host can track API users and rate-limit if necessary (or ban) by token rather than IP address.

The NIST beacon does not require a token, but many APIs do, which is why you usually need to sign up for the service and request an API token before you can start using the API.
