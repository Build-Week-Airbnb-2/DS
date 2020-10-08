# DS

DS
Unit 4 - Data Cleaning, Neural Networks and Linear Regression models.
Goal of App: To ensure that Home owners can rent their properties at the optimal range.

This project does not have a live API which we can scrape data and learn from due to CO-VID19 Site issues but it

does have historical data from many sources available.

Through intense data research, collection, and cleaning, we assembled a table of 243k obvservations

and 107 rows. We reduced the column count to 19 final features, while keeping observation(row) quantity.

'AirBnB_NN_DC' Has A Neural Network which returns an MAE of $165. It doesn't give very precise
results, but it does successfully return results.

'airbnb_linear_regression' has a linear regression model which also returns an MAE of about $181. This result is similar to that of the Neural network, so it's tough to decide how successful our calculations have become. This information is revealed when we view the R2 score of this linear regression model. This linear regression model has an R2 score of 0.06. That's nearly 0. The closer an R2 score is to 1, The better the score is, and the better our model is explaining the variance in targets. The closer the r2 score is 0, the more likeley it is that the model explains none of the variability.
This can be interpreted as :

We are 186$ dollars away from perfect predictions

BUT

Our model is probably seriously overfit.

This might be the case if a lot of duplicate postings existing.

Our NN is currently deployed on the DS Heroku App at the following Address:

https://ds-bw-airbnb-2.herokuapp.com/#/default/predict_predict_post

This Heroku App predicts a price depending on the values provided in the JSON Submission
