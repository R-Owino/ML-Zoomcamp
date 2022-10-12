import pickle 
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression

dv = 'dv.bin'
model = 'model1.bin'

with open(dv, 'rb') as f_in:
    dv = pickle.load(f_in)

with open(model, 'rb') as f_in:
    model = pickle.load(f_in)

#df = pd.DataFrame(customer, index=[0])
customer = {"reports": 0, "share": 0.001694, "expenditure": 0.12, "owner": "yes"}

X = dv.transform([customer])

y_pred = model.predict_proba(X)[0,1]
print(y_pred)