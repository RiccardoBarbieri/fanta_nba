#By Gabriele Tassinari
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.compose import ColumnTransformer
import tensorflow as tf
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt

# Caricamento del file CSV
file_path = 'final.csv'
data = pd.read_csv(file_path)

# Separazione delle feature e del target
features = data.drop(columns=['pts_H', 'pts_A', 'referee_id', 'winner', 'home_team', 'away_team', 'referee_name', 'season', 'date'])
target = data['winner']

# Salva l'ID della partita
game_ids = data['game_id']

# Identificazione delle colonne numeriche
numerical_cols = [col for col in features.columns if col != 'game_id']

# Preprocessing: Min-Max Scaling per le colonne numeriche
preprocessor = ColumnTransformer(
    transformers=[
        ('num', MinMaxScaler(), numerical_cols)
    ])

# Applicazione del preprocessing ai dati
features_preprocessed = preprocessor.fit_transform(features)

# Conversione del target in numerico
target = pd.factorize(target)[0]

# Solitamente 80% e 20% per training e test set -> avendo 3944 righe
# Dividiamo i dati in training set (prime 800 righe) e test set (resto)
X_train = features_preprocessed[:3155]
y_train = target[:3155]
X_test = features_preprocessed[3155:]
y_test = target[3155:]
test_game_ids = game_ids.iloc[3155:]

# Creazione del modello con Dropout per ridurre overfitting
model = Sequential([
    Dense(32, activation='relu'),
    Dropout(0.3),
    Dense(16, activation='relu'),
    Dense(1, activation='sigmoid')
])

# Compilazione del modello
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Early stopping
early_stopping = EarlyStopping(monitor='val_loss', patience=3, restore_best_weights=True)

# Addestramento del modello
history = model.fit(X_train, y_train, epochs=300, batch_size=32, validation_split=0.2)
#history = model.fit(X_train, y_train, epochs=74, batch_size=32, validation_split=0.2, callbacks=[early_stopping])

# Salvataggio del modello
model.save('nba_winner_model13.h5')

# Valutazione del modello
loss, accuracy = model.evaluate(X_test, y_test)
print(f'Loss: {loss}')
print(f'Accuracy: {accuracy}')

# Predizione sui dati di test
y_pred = (model.predict(X_test) > 0.5).astype("int32")

# Report di classificazione
print('Classification Report:')
print(classification_report(y_test, y_pred))

# Plot delle loss e accuracy durante il training
fig, ax1 = plt.subplots()

ax1.set_xlabel('Epoch')
ax1.set_ylabel('Loss', color='tab:red')
ax1.plot(history.history['loss'], label='loss', color='tab:red')
ax1.plot(history.history['val_loss'], label='val_loss', color='tab:orange')
ax1.tick_params(axis='y', labelcolor='tab:red')

ax2 = ax1.twinx()
ax2.set_ylabel('Accuracy', color='tab:blue')
ax2.plot(history.history['accuracy'], label='accuracy', color='tab:blue')
ax2.plot(history.history['val_accuracy'], label='val_accuracy', color='tab:cyan')
ax2.tick_params(axis='y', labelcolor='tab:blue')

fig.tight_layout()
fig.legend(loc='upper left', bbox_to_anchor=(0.1, 0.9))
plt.show()

# Selezioniamo 10 righe random dal dataset di test e prediciamo il winner
random_indices = np.random.choice(X_test.shape[0], 10, replace=False)
random_samples = X_test[random_indices]
random_labels = y_test[random_indices]
random_game_ids = test_game_ids.iloc[random_indices].values
random_predictions = model.predict(random_samples)
random_predictions = (random_predictions > 0.5).astype("int32")

print("\nPredictions on random test samples:")
for i in range(10):
    print(f"Sample {i+1} - Game ID: {random_game_ids[i]}, Predicted: {random_predictions[i][0]}, Actual: {random_labels[i]}")
