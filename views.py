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
    teams = [
        {
            'name': "Eastside Neighborhood Team",
            'leader': "Isaac Chan",
            'email': "isaac.d.chan@gmail.com",
            'link': "https://www.facebook.com/groups/eastsideneighborhoodteam/"
        },
        {
            'name': "Shoreline/Bothell",
            'leader': "Danielle Vrchota",
            'email': "dmiles85@hotmail.com",
            'link': "https://www.facebook.com/groups/sbneighborhoodteam/"
        },
        {
            'name': "Northwest Seattle",
            'leader': "Joey DeYoung",
            'email': "joey@theuppercrustcatering.com",
            'link': "https://www.facebook.com/groups/nwseattleneighborhoodteam/"
        },
        {
            'name': "Northeast Seattle",
            'leader': "Jackie Gause",
            'email': "jalee50@hotmail.com",
            'link': "https://www.facebook.com/groups/neseattleneighborhoodteam/"
        },
        {
            'name': "Downtown Seattle",
            'leader': "Kris John",
            'email': "kris.joyhope@yahoo.com",
            'link': "https://www.facebook.com/groups/DowntownNeighborhoodTeam/"
        },
        {
            'name': "Southwest Seattle",
            'leader': "Jessica Hauffe",
            'email': "jessicahauffe@hotmail.com",
            'link': "https://www.facebook.com/groups/swseattleneighborhoodteam/"
        },
        {
            'name': "Southeast Seattle",
            'leader': "Megan Whalen",
            'email': "mlwhalen@gmail.com",
            'link': "https://www.facebook.com/groups/SESeattleNeighborhoodTeam/"
        },
        {
            'name': "Kent",
            'leader': "Tara Hill",
            'email': "tlouhou@msn.com",
            'link': "https://www.facebook.com/groups/kentneighborhoodteam/"
        },
        {
            'name': "Federal Way/Auburn",
            'leader': "Jared Peavey",
            'email': "jared634899@gmail.com",
            'link': "https://www.facebook.com/groups/976614795743458/"
        },
        ]
    return render_template('volunteer.html', teams=teams)

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

@app.route('/share.html')
def share():
    return render_template('share.html')
