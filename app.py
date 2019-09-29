from flask import Flask, render_template

app = Flask(__name__)

# @app.route('/')
# def index():
#     """Return homepage"""
#     # return render_template('home.html', msg= 'Flask is Cool!!')

if __name__ == '__main__':
    app.run(debug=True)


## OUR MOCK ARRAY OF PROJECTS
playlists = [
    { 'title': 'Cat videos', 'description': 'Cats acting weird' },
    { 'title': '80\'s Music', 'description': 'Don\'t stop believing!' },
    { 'title': '90\'s Music', 'description': 'Creep'},
    { 'title': '60\'s Music', 'description': 'Wild Thing'},
    { 'title': '50\'s Music', 'description': 'Dream Lover'}
]

@app.route('/')
def playlists_index():
    """Show all playlists."""
    return render_template('playlists_index.html', playlists=playlists)
