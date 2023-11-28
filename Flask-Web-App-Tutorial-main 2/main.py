from website import create_app
import json

app = create_app()

notes = []



if __name__ == '__main__':
    app.run(debug=True)
#test