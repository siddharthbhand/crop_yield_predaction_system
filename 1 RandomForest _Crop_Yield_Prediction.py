import pandas as pd

import warnings
warnings.filterwarnings("ignore")


from sklearn.model_selection import train_test_split

from sklearn.metrics import accuracy_score

from sklearn.metrics import classification_report

from sklearn.ensemble import RandomForestClassifier




data = pd.read_csv('model/crop_yield_dataset.csv')
crop_summary = pd.pivot_table(data,index=['label'],aggfunc='mean')
#data1 = data[['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']]
          

  
X = data.drop('label', axis=1)
y = data['label']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.33, shuffle = True, random_state = 0)




classifier_rf= RandomForestClassifier(n_estimators= 10, criterion="entropy")  
classifier_rf.fit(X_train, y_train) 

print("X_train :::::::::::::::::::: ",X_train)
print("y_train :::::::::::::::::::: ",y_train)

print("X_TEST")
print(X_test)
print("\n ===========================================\n")
print("y_test :::::::::::::::::::: ",y_test)


print("\n TT============================================================TT\n")

y_pred= classifier_rf.predict(X_test)



accuracy=accuracy_score(y_pred, y_test)
print('Random Forest Model accuracy score: {0:0.4f}'.format(accuracy_score(y_test, y_pred)))



print("report ----------------")
print(classification_report(y_test, y_pred))


res = pd.DataFrame(y_pred)
res.index = X_test.index # its important for comparison
res.columns = ["prediction"]
res.to_csv("model/prediction_results.csv")
print("Prediction Data Stored Successfully")



