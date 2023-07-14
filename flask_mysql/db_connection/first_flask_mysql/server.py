from flask import Flask, render_template, request, redirect
from friend import Friend
# import the class from friend.py
app = Flask(__name__)

@app.route("/")
def index():
    # calling the get_all method from the friends.py
    # call the get all classmethod to get all friends
    all_friends = Friend.get_all()
    print(all_friends)
    return render_template("index.html", friends =all_friends)

@app.route("/friends/<int:friend_id>")
def show(friend_id):
    # calling the get_one method and supplying it with the id of the friend we want to get
    one_friend = Friend.get_one(friend_id)
    return render_template("index.html", one_friend= one_friend)
            
@app.route('/friends/create', methods=["POST"])
def create_friend():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    # data = {
    #     "fname": request.form["fname"],
    #     "lname" : request.form["lname"],
    #     "occ" : request.form["occ"]
    # }
    
    # We pass the data dictionary into the save method from the Friend class.
    # Friend.save(data)
    Friend.save(request.form)
    # Don't forget to redirect after saving to the database.
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
