from app import app

if __name__ == '__main__':
    app.run(debug=True) #<---This is the problem
    print("block executed")

print("run.py is working")