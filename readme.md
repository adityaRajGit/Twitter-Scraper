# Create a .env file with your credentials:

` TWITTER_EMAIL=your_email@example.com`
`TWITTER_PASSWORD=your_password`
`PROXYMESH_HOST=your_proxymesh_host`
`PROXYMESH_PORT=your_proxymesh_port`
`MONGO_URI=your_mongodb_connection_string` 

# Install the required packages:

* pip install -r requirements.txt

## Files Consisting :

* config.py : Handles environment variables
* scraper.py : Contains the TwitterScraper class that handles web scraping and MongoDB storage
* app.py : Flask application that serves the web interface
* frontend.html : For Frontend html page

# To run application :

- python app.py