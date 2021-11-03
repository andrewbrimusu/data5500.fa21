import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
import seaborn as sn
import matplotlib.pyplot as plt

import pandas as pd
import numpy as np



from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

from sklearn.neural_network import MLPClassifier


candidates = {'gmat': [780,750,690,710,780,730,690,720,740,690,610,690,710,680,770,610,580,650,540,590,620,600,550,550,570,670,660,580,650,760,640,620,660,660,680,650,670,580,590,790],
              'gpa': [4,3.9,3.3,3.7,3.9,3.7,2.3,3.3,3.3,1.7,2.7,3.7,3.7,3.3,3.3,3,2.7,3.7,2.7,2.3,3.3,2,2.3,2.7,3,3.3,3.7,2.3,3.7,3.3,3,2.7,4,3.3,3.3,2.3,2.7,3.3,1.7,3.7],
              'work_experience': [3,4,3,5,4,6,1,4,5,1,3,5,6,4,3,1,4,6,2,3,2,1,4,1,2,6,4,2,6,5,1,2,4,6,5,1,2,1,4,5],
              'age': [25,28,24,27,26,31,24,25,28,23,25,27,30,28,26,23,29,31,26,26,25,24,28,23,25,29,28,26,30,30,23,24,27,29,28,22,23,24,28,31],
              'admitted': [2,2,1,2,2,2,0,2,2,0,0,2,2,1,2,0,0,1,0,0,1,0,0,0,0,1,1,0,1,2,0,0,1,1,1,0,0,0,0,2]
              }

df = pd.DataFrame(candidates,columns= ['gmat', 'gpa','work_experience','age','admitted'])
# print (df)


X = df[['gmat', 'gpa','work_experience','age']]
y = df['admitted']


X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.20,random_state=0)


#build and test random forest model
clf = RandomForestClassifier()
clf.fit(X_train,y_train)
y_pred=clf.predict(X_test)
print("y predictions: ", y_pred)
# print("y actuals: ", y_test)

confusion_matrix = pd.crosstab(y_test, y_pred, rownames=['Actual'], colnames=['Predicted'])
sn.heatmap(confusion_matrix, annot=True).get_figure().savefig("/home/ubuntu/environment/data5500.fa21/week12_ml/random_forest.png")
# sn.get_figure().savefig("results.png")
print('Accuracy: ',metrics.accuracy_score(y_test, y_pred))
plt.show()

print("3 candidate predictions...")
print(clf.predict([[780, 4, 3, 25]])) # predict candidate with gmat 780, gpa 4.0, 3 yrs work exp., 25 years old
print(clf.predict([[690, 3.3, 3, 25]])) #  predict candidate with gmat 690, gpa 3.3, 3 yrs work exp., 25 years old
print(clf.predict([[660, 2, 3, 25]])) #  predict candidate with gmat 660, gpa 2.0, 3 yrs work exp., 25 years old



# build and test 7 additional models
models = [LogisticRegression(), DecisionTreeClassifier(), KNeighborsClassifier(), 
    GaussianNB(), LinearDiscriminantAnalysis(), SVC(), MLPClassifier(), RandomForestClassifier()]
    

for model in models:
    lst = [[0 for j in range(20)] for i in range(20)]
    
    print(str(model) + "...")
    clf = model
    clf.fit(X_train,y_train)
    y_pred=clf.predict(X_test)
    print("y predictions: ", y_pred)
    # print("y actuals: ", y_test)
    
    for x in range(20):
        for y in range(20):
            lst[x][y] = clf.predict([[ 420 + 20*x, 2 + y*0.1, 3, 25]])[0]
            
            
    confusion_matrix = pd.crosstab(y_test, y_pred, rownames=['Actual'], colnames=['Predicted'])
    sn.heatmap(confusion_matrix, annot=True).get_figure().savefig("/home/ubuntu/environment/data5500.fa21/week12_ml/" + str(model) + ".png")
    # sn.get_figure().savefig("results.png")
    print('Accuracy: ',metrics.accuracy_score(y_test, y_pred))
    plt.show()
    plt.close()
    print("3 candidate predictions...")
    print(clf.predict([[780, 4, 3, 25]])) # predict candidate with gmat 780, gpa 4.0, 3 yrs work exp., 25 years old
    print(clf.predict([[690, 3.3, 3, 25]])) #  predict candidate with gmat 690, gpa 3.3, 3 yrs work exp., 25 years old
    print(clf.predict([[660, 2, 3, 25]])) #  predict candidate with gmat 660, gpa 2.0, 3 yrs work exp., 25 years old

    plt.imshow(np.array(lst), cmap='Blues',interpolation="nearest")
    plt.savefig(str(model)+".png")
