# Flask server && Emotion Recognizer

- Here flask server initiated by `flask run` gives an HTML Template that provide user with following applications:

> `Form` <br>
> `WorkFlow Diagram`

- Form works with flask as backend and Mysql as database to store details in table form. These details can be accesed using `GET` call.
- WorkFlow Diagram shows how flask server works and what steps takes place when server is initiated.

* Other than flask server there is `emo.py` file which is emotion recognizer works on the principle of OpenCV to read video and emotion trained model to recognize emotions on the faces availbale in the frame.
* The `emo.py` provides with following applications:

> Emotion recognisation <br>
> Live feedback

### To run locally

```shell
git clone https://github.com/mstomar698/flask-form.git
cd flask-form
flask run
```
