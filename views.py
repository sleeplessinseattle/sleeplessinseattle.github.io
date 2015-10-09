from flask import render_template, redirect, request
from app import app

redirect_urls = {
    # '/biggive.html': '/volunteer.html'
}

def redirect_url():
    return redirect(redirect_urls[request.url], 301)

for url in redirect_urls:
    app.add_url_rule(url, url, redirect_url)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/volunteer.html')
def volunteer():
    return render_template('volunteer.html')

@app.route('/contact.html')
def contact():
    return render_template('contact.html')

@app.route('/donate.html')
def donate():
    return render_template('donate.html')

@app.route('/press_kit.html')
def press_kit():
    return render_template('press_kit.html')

@app.route('/sponsorships.html')
def sponsorships():
    return render_template('sponsorships.html')

