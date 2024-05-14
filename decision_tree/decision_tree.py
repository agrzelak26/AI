import numpy as np
from collections import Counter

#pojedynczy wezel drzewa
class Node:
    def __init__(self, feature=None, threshold=None, left=None, right=None, *, value=None):
        self.feature = feature #indeks cechy
        self.threshold = threshold #prog podzialu dla tej cechy
        self.left = left
        self.right = right
        self.value = value #etykieta - gdy jest lisciem

    def is_leaf_node(self):
        return self.value is not None

class DecisionTree:
    def __init__(self, min_samples_split=2, max_depth=100, n_features=None):
        self.min_samples_split = min_samples_split #minimum elementow do podzielenia
        self.max_depth = max_depth #maksymalna glebokosc drzewa
        self.n_features = n_features #ilosc cech wybieranych przy podziale
        self.root = None

    #funkcja ktora tworzy drzewo z x (wartosci) i y (etykiet)
    def fit(self, X, y):
        if self.n_features is None:
            self.n_features = len(X[0]) #ilosc cech to dlugosc wierszy tablicy danych
        else:
            self.n_features = min(self.n_features, len(X[0])) #lub minimum z ilosci cech i dlugosci wierszy tablicy danych
        self.root = self._grow_tree(X, y) #tworzenie drzewa

    #rekurencyjne tworzenie drzewa
    def _grow_tree(self, X, y, depth=0):
        n_samples = len(X) #ilosc probek
        n_features = len(X[0]) #ilosc cech w tych probkach
        n_labels = len(np.unique(y)) #ilosc roznych etykiet na dany moment

    #zatrzyma sie gdy - osiagnie max glebokosc; zabraknie probek; zostanie jedna etykieta
        if depth >= self.max_depth or n_samples < self.min_samples_split or n_labels == 1:
            counter = Counter(y)
            most_common_value = counter.most_common(1)[0][0] #najczesciej wystepujaca wartosc w etykietach tego liscia
            return Node(value=most_common_value)

        feat_indexes = np.random.choice(n_features, self.n_features, replace=False)

        # wybranie najlepszych cech i progu podzialu oraz podzielenie w ten sposob
        best_features_column, best_threshold = self._best_split(X, y, feat_indexes)
        left_indexes, right_indexes = self._split(X[:, best_features_column], best_threshold)

        #wywolania rekurencyjne
        left = self._grow_tree(X[left_indexes, :], y[left_indexes], depth + 1)
        right = self._grow_tree(X[right_indexes, :], y[right_indexes], depth + 1)

        # zwraca node ktory nie jest lisciem
        return Node(best_features_column, best_threshold, left, right)

#szuka najlepszego podzialu dla danych
    def _best_split(self, X, y, feat_indexes):
        split_index = None
        split_threshold = None
        best_gain = -1
        #przejscie po indeksach cech
        for i in feat_indexes:
            values = X[:, i] #wyciagamy unikalne wartosci z kolumny danej cechy
            unique_values = np.unique(values)
            if len(unique_values) == 1:
                continue
            for threshold in unique_values[:-1]:
                gain = self._information_gain(y, values, threshold)
                if gain > best_gain:
                    best_gain = gain
                    split_index = i
                    split_threshold = threshold
        return split_index, split_threshold

    # 𝐼𝐺=𝐸(𝑝𝑎𝑟𝑒𝑛𝑡)−[𝑤𝑒𝑖𝑔ℎ𝑡𝑒𝑑_𝑎𝑣𝑒𝑟𝑎𝑔𝑒]∗𝐸(𝑐ℎ𝑖𝑙𝑑𝑟𝑒𝑛)
    def _information_gain(self, y, X_column, threshold):
        parent_entropy = self._entropy(y)
        # podzial na lewe i prawe wartosci wzgledem progu
        left_indexes, right_indexes = self._split(X_column, threshold)

        if len(left_indexes) == 0 or len(right_indexes) == 0:
            return 0

        #liczenie ze wzoru
        count = len(y)
        left_count, right_count = len(left_indexes), len(right_indexes)
        left_entropy, right_entropy = self._entropy(y[left_indexes]), self._entropy(y[right_indexes])
        children_entropy = (left_count / count) * left_entropy + (right_count / count) * right_entropy

        return parent_entropy - children_entropy


#dzieli podzialu kolumny wzgledem progu
    def _split(self, X_column, split_thresh):
        left_indexes = []
        right_indexes = []
        for i, x in enumerate(X_column):
            if x <= split_thresh:
                left_indexes.append(i)
            else:
                right_indexes.append(i)
        return np.array(left_indexes), np.array(right_indexes)

#liczy entropie
    def _entropy(self, y):
        hist = np.bincount(y)
        ps = hist / len(y)
        return -np.sum([p * np.log(p) for p in ps if p > 0])

#przechodzenie drzewa
    def _traverse_tree(self, x, node):
        if node.is_leaf_node():
            return node.value

        if x[node.feature] <= node.threshold:
            return self._traverse_tree(x, node.left)
        else:
            return self._traverse_tree(x, node.right)

#predykcja na podstawie drzewa
    def predict(self, X):
        return np.array([self._traverse_tree(x, self.root) for x in X])
