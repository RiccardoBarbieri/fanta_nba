import pandas as pd
import joblib

# Caricamento del modello e del preprocessore salvati
best_rf = joblib.load('best_random_forest_model.joblib')
preprocessor = joblib.load('preprocessor.joblib')

# Caricamento del file CSV
file_path = 'final.csv'
data = pd.read_csv(file_path)

# Creazione della nuova colonna 'point_diff'
data['point_diff'] = data['pts_H'] - data['pts_A']

# Separazione delle feature e del target
features = data.drop(columns=['pts_H', 'pts_A', 'referee_id', 'point_diff', 'home_team', 'away_team', 'referee_name', 'winner'])
target = data['point_diff']

# Funzione per fare predizioni per una partita specifica dato il suo ID
def predict_game(game_id, model, preprocessor):
    game_index = data[data['game_id'] == game_id].index[0]
    game_features = features.iloc[game_index].to_frame().T  # Converti in DataFrame
    game_features_preprocessed = preprocessor.transform(game_features)
    predicted_point_diff = model.predict(game_features_preprocessed)[0]
    actual_point_diff = target[game_index]
    return predicted_point_diff, actual_point_diff

# Esempio di utilizzo della funzione predict_game
game_id_to_predict = data['game_id'].iloc[0] 
predicted_diff, actual_diff = predict_game(game_id_to_predict, best_rf, preprocessor)
print(f"\nPrediction for Game ID {game_id_to_predict}:")
print(f"Predicted Point Difference: {predicted_diff}, Actual Point Difference: {actual_diff}")
