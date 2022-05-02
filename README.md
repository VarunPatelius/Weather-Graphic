# Weather-Messenger
A Python script that uses OpenWeatherMap and an SVG template to send a weather graphic. Used alongside a cron job.

# Setup
After cloning or downloading the repository, the only thing that needs to be established is a .env

```bash
WEATHER=xxxxxxxxxx
PTN_USER=xxxxxxxxxx
CSRF=xxxxxxxxxx
SID=xxxxxxxxxx
LATITUDE=xxxxxxxxxx
LONGITUDE=xxxxxxxxxx
RECIPIENT=xxxxxxxxxx
```

WEATHER is the API token used by OpenWeatherMap. PTN_USER, CSRF, and SID can all be pulled from the TextNow web application. LATITUDE, LONGITUDE, and RECIPIENT are used to determine the location and establish the recipient of the graphic.
