from flask import Flask, render_template, jsonify
from scraper import TwitterScraper

app = Flask(__name__)
scraper = TwitterScraper()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/scrape', methods=['POST'])
def scrape_trends():
    try:
        results = scraper.get_trending_topics()
        return jsonify(results)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)