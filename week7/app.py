from flask import Flask, render_template
import requests
import trivia.triviaquestion
import trivia.triviagame

app = Flask(__name__)

question = trivia.triviaquestion.TriviaQuestion
print(question)

game = trivia.triviagame.TriviaGame()
print(game)
def getData():
    URL = "https://opentdb.com/api.php?amount=10&category=9&difficulty=medium&type=multiple"
    try: 
        response = requests.get(URL, timeout=5)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.HTTPError as errh:
        print(errh)
    except requests.exceptions.ConnectionError as errc:
        print(errc)
    except requests.exceptions.Timeout as errt:
        print(errt)
    except requests.exceptions.RequestException as err:
        print(err)



data = getData()
index = 0
for q in data["results"]:
    print(q)
    newUser = question(q["question"],
                q['category'],
                q['difficulty'],
                q['correct_answer'],
                q['incorrect_answers'],
                index)
    index += 1 
    newUser.answerShuffle()
    game.addQuestion(newUser)
print(game.questions)


@app.route("/")
def hello():
    return render_template('index.html', results = game.questions)



if __name__ == "__main__":
    app.run()

