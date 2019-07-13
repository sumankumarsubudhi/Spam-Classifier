# Spam-Classifier

It is the design of a machine learning model that can efficiently predict if an SMS message is spam or not!

Spam detection is one of the major applications of Machine Learning in the interwebs today. Pretty much all of the major email service providers have spam detection systems built in and automatically classify such mail as 'Junk Mail'.
Being able to identify spam messages is a binary classification problem as messages are classified as either 'Spam' or 'Not Spam' and nothing else. 
Also, this is a supervised learning problem, as we will be feeding a labelled dataset into the model, that it can learn from, to make future predictions.

**Here's a preview of the data:**

<img width="1148" alt="dqnb" src="https://user-images.githubusercontent.com/20025875/61074798-2bb54500-a436-11e9-8083-16ad4fd07606.png">

### Score's on evaluating the model on "spam classifier.ipynb"

* Accuracy score:  0.9885139985642498
* Precision score:  0.9720670391061452
* Recall score:  0.9405405405405406
* F1 score:  0.9560439560439562

### Score's on evaluating the model on "spam classifier 2.ipynb"

**Bagging Scores**

* Accuracy score for bagging : 0.9755922469490309
* Precision score bagging : 0.9171270718232044
* Recall score bagging : 0.8972972972972973
* F1 score bagging : 0.907103825136612

**Random Forest scores**

* Accuracy score for random forest : 0.9813352476669059
* Precision score random forest : 1.0
* Recall score random forest : 0.8594594594594595
* F1 score random forest : 0.9244186046511628
 
**AdaBoost scores**

* Accuracy score for adaboost : 0.9770279971284996
* Precision score adaboost : 0.9693251533742331
* Recall score adaboost : 0.8540540540540541
* F1 score adaboost : 0.9080459770114943
