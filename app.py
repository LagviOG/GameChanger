from ext import app


if __name__ == "__main__":
    from routes import Register,Login,About,home,Post,game,delete_game,logout
    app.run(debug=True)
