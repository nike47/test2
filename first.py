from sklearn import svm

#[height weight shoe size]
x=[[188,78,54],[136,76,40],[166,60,45],[155,70,55],[136,76,40],[166,67,50],[144,67,40],[144,67,40],[164,52,45],[168,78,54],[176,79,56]]
y=['male','female','female','male','female','female','male','male','male','male','female']


clf=svm.SVC()


clf=clf.fit(x,y)


#prediction code
a = [int(x) for x in input('enter height weight shoe').split()]
prediction=clf.predict([a])
print (prediction)