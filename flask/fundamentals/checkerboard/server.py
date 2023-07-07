from flask import Flask, render_template
app = Flask(__name__)

#http://localhost:5000 - should display 8 by 8 checkerboard
@app.route('/')
def index():
    return render_template("index.html",row = 8,col=8, color1= 'red', color2= 'black')

#http://localhost:5000/4 - should display 8 by 4 checkerboard
@app.route('/<int:col>')
def def_row_col(col):
    return render_template("index.html", row = 8,col=col, color1= 'red', color2= 'black')

#http://localhost:5000/(x)/(y) - should display x by y checkerboard.
@app.route('/<int:row>/<int:col>')
def row_col(row,col):
    return render_template("index.html", row = row,col=col, color1= 'red', color2= 'black')

#TODO SENSEI BONUS: Have another route accept 4 parameters (i.e. "/<x>/<y>/<color1>/<color2>") 
# and render a checkerboard with x rows and y columns, with alternating colors, color1 and color2
@app.route('/<int:row>/<int:col>/<color1>/<color2>')
def row_col_colors(row,col,color1,color2):
    return render_template("index.html", row = row,col=col, color1= color1, color2= color2)

if __name__=="__main__":
    app.run(debug=True)
