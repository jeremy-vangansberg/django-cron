import pickle
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Charger le dataset des iris
data = load_iris()
X = data['data']
y = data['target']

# Diviser le dataset en données d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Créer le modèle de classification
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Évaluer le modèle
accuracy = model.score(X_test, y_test)
print(f"Accuracy: {accuracy * 100:.2f}%")

# Sauvegarder le modèle dans un fichier .pkl
with open('iris_model.pkl', 'wb') as file:
    pickle.dump(model, file)

print("Le modèle a été sauvegardé dans 'iris_model.pkl'")