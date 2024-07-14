import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
import joblib  # Libreria per salvare e caricare il modello
import matplotlib.pyplot as plt

# Caricamento del file CSV
file_path = 'final.csv'
data = pd.read_csv(file_path)

# Creazione della nuova colonna 'point_diff'
data['point_diff'] = data['pts_H'] - data['pts_A']

# Separazione delle feature e del target
features = data.drop(columns=['pts_H', 'pts_A', 'referee_id', 'point_diff', 'home_team', 'away_team', 'referee_name', 'winner', 'date', 'season'])
target = data['point_diff']

# Salva l'ID della partita
game_ids = data['game_id']

# Identificazione delle colonne categoriali e numeriche
categorical_cols = ['playoff']
numerical_cols = [col for col in features.columns if col not in categorical_cols and col != 'game_id']

# Preprocessing: One-Hot Encoding per categoriali, Min-Max Scaling per numeriche
preprocessor = ColumnTransformer(
    transformers=[
        ('num', MinMaxScaler(), numerical_cols),
        ('cat', OneHotEncoder(), categorical_cols)
    ])

# Applicazione del preprocessing ai dati
features_preprocessed = preprocessor.fit_transform(features)

# Divisione del dataset in training set (80%) e test set (20%)
X_train, X_test, y_train, y_test, train_game_ids, test_game_ids = train_test_split(
    features_preprocessed, target, game_ids, test_size=0.2, random_state=42
)

# Creazione del modello Linear Regression
linear_regressor = LinearRegression()

# Addestramento del modello
linear_regressor.fit(X_train, y_train)

# Salvataggio del modello
joblib.dump(linear_regressor, 'linear_regression_model.joblib')
joblib.dump(preprocessor, 'preprocessor_linear.joblib')

# Predizione sui dati di test
y_pred = linear_regressor.predict(X_test)

# Valutazione del modello
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
print(f'Mean Absolute Error (MAE): {mae}')
print(f'Mean Squared Error (MSE): {mse}')
print(f'Root Mean Squared Error (RMSE): {rmse}')

# Visualizzazione dell'importanza delle feature
feature_names = (
    numerical_cols +
    list(preprocessor.named_transformers_['cat'].get_feature_names_out(categorical_cols))
)
feature_importance = linear_regressor.coef_

# Creazione del DataFrame per l'importanza delle feature
importance_df = pd.DataFrame({
    'Feature': feature_names,
    'Importance': feature_importance
})

# Ordinamento per importanza
importance_df = importance_df.sort_values(by='Importance', ascending=False)

# Print dell'importanza delle feature
print("\nFeature Importance:")
for index, row in importance_df.iterrows():
    print(f"Feature: {row['Feature']}, Importance: {row['Importance']}")

# Plot dell'importanza delle feature
plt.figure(figsize=(12, 12))
plt.barh(importance_df['Feature'], importance_df['Importance'], color='skyblue')
plt.xlabel('Importance')
plt.ylabel('Feature')
plt.title('Feature Importance - Linear Regression')
plt.gca().invert_yaxis()
plt.xticks(rotation=45, fontsize=8)  
plt.yticks(fontsize=8)
plt.show()

# Funzione per fare predizioni per una partita specifica dato il suo ID
def predict_game(game_id, model, preprocessor):
    game_index = data[data['game_id'] == game_id].index[0]
    game_features = features.iloc[game_index].to_frame().T  # Converti in DataFrame
    game_features_preprocessed = preprocessor.transform(game_features)
    predicted_point_diff = model.predict(game_features_preprocessed)[0]
    actual_point_diff = target[game_index]
    return predicted_point_diff, actual_point_diff

# Funzione per calcolare l'accuratezza del modello basata sulla concordanza del segno
def calculate_sign_accuracy(y_true, y_pred):
    y_true_sign = np.sign(y_true)
    y_pred_sign = np.sign(y_pred)
    accuracy = np.mean(y_true_sign == y_pred_sign)
    return accuracy

# Calcola l'accuratezza del modello basata sulla concordanza del segno
sign_accuracy = calculate_sign_accuracy(y_test, y_pred)
print(f'Sign Accuracy: {sign_accuracy}')

# Selezioniamo 10 righe random dal dataset di test e prediciamo lo scarto dei punti
random_indices = np.random.choice(X_test.shape[0], 10, replace=False)
random_samples = X_test[random_indices]
random_labels = y_test.iloc[random_indices]
random_game_ids = test_game_ids.iloc[random_indices].values
random_predictions = linear_regressor.predict(random_samples)

print("\nPredictions on random test samples:")
for i in range(10):
    print(f"Sample {i+1} - Game ID: {random_game_ids[i]}, Predicted Point Difference: {random_predictions[i]}, Actual Point Difference: {random_labels.iloc[i]}")

# Esempio di utilizzo della funzione predict_game
game_id_to_predict = test_game_ids.iloc[0]
predicted_diff, actual_diff = predict_game(game_id_to_predict, linear_regressor, preprocessor)
print(f"\nPrediction for Game ID {game_id_to_predict}:")
print(f"Predicted Point Difference: {predicted_diff}, Actual Point Difference: {actual_diff}")
