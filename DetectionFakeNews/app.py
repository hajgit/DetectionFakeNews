from flask import Flask, render_template, request
import tensorflow as tf
import numpy as np

app = Flask(__name__)

# Charger le modèle
model = tf.keras.models.load_model('model_rnn.h5')

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST':
        news = request.form['news']
        # Prétraitement du texte et prédiction
        # Remplacez cette partie par votre propre logique
        prediction = "REAL news" if len(news) % 2 == 0 else "FAKE news"
    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
