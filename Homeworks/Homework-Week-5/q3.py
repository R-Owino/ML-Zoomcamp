import pickle
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression

# Saving the models as variables to open them easily

model = 'model1.bin'
dv = 'dv.bin'

# Using wih to open, ensures the files are closed

with open(model, 'rb') as f_in:
    model = pickle.load(f_in)

with open(dv, 'rb') as f_in:
    dv = pickle.load(f_in)

# Client to make predictions for
# Got this by passing an index to the dataframe constructor i.e
# df = pd. DataFrame(cuat, index=[3])
cust = {"reports": 0, "share": 0.001694, "expenditure": 0.12, "owner": "yes"}

# Making predictions

X = dv.transform([cust])
y_pred = model.predict_proba(X)[0, 1]

print("Credit card probability: ", y_pred)