from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

X, y = [], []
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=1)
my_model = RandomForestClassifier(n_estimators=100,
                                  random_state=0).fit(train_X, train_y)