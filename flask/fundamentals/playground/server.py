from flask import Flask, render_template
app = Flask(__name__)

#TODO Level 1
'''
When a user visits http://localhost:5000/play, 
have it render three beautiful looking blue boxes. 
Please use a template to render this.
'''
@app.route('/', defaults={'path': '/play'})
@app.route('/<path:path>')
def play(path):
    return render_template('level1.html')

#TODO level 2
'''
When a user visits localhost:5000/play/(x), 
have it display the beautiful looking blue boxes x times.
'''
@app.route('/play/<int:num>')
def play_with_custom_num_of_boxes(num):
    return render_template('level2.html', times = num)

#TODO level 3
'''
When a user visits localhost:5000/play/(x)/(color), 
have it display beautiful looking boxes x times, 
but this time where the boxes appear in (color).
'''

@app.route('/play/<int:num>/<color>')
def play_with_custom_num_of_boxes_and_colors(num, color):
    return render_template("level3.html", times= num, color_change=color)

if __name__ == "__main__":
    app.run(debug=True)
