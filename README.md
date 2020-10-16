# DS
## Summary
DS
Unit 4 - Data Cleaning, Neural Networks and Linear Regression models.
Goal of App: To ensure that Home owners can rent their properties at the optimal range.

This project did not use a live API due to CO-VID19 Site issues but it did use historical data as recent as 2019 to train and validate the prediction model.

Through intense data research, collection, and cleaning, we assembled a table of 243k obvservations and 107 rows. We reduced the column count to 19 final features, while keeping observation(row) quantity.

'AirBnB_NN_DC' Has A Neural Network which returns an MAE of $165. It doesn't give very precise results, but it does successfully return results. I break my notebook into sections for each area focus.

## Breakdown of Processes
For Data Cleaning, I used pandas to investigate the data. I utilized methods such as pandas.fillna() to fix null values and pandas.replace() to correct fields with invalid entries. [For some awesome data cleaning tips and techniques, watch this.] tutorial(https://www.youtube.com/watch?v=iYie42M1ZyU&t=4302s) Daniel Chen is an excellent teacher and I recommend his material for practitioners of all levels, whether you're looking to learn pandas for the first time, or just need some refreshers.

I Used transformers to normalize data values. in plain english, [Normalization](https://en.wikipedia.org/wiki/Normalization_(statistics)) is the term used to describe the action of adjusting values which vary in scale, down to a common scale. This is a good technique for adding robustness to your model. After some more preprocessing steps, I build a Sequential model using Keras . I constructed a model with three layers. The first two are matching layers with 64 Node densities, both using "relu" as activation functions. "ReLu" is a common and powerful activation function which stands for Rectified Linear Units. [Rectifiers](https://en.wikipedia.org/wiki/Rectifier_(neural_networks)) have been thoroughly researched and are a very valuable sub-topic of machine learning to familiarize with. The last layer is one node dense with a linear activation function. ; since this is a regression problem, it's what we need to produce a result of a single number.
![Pic of Model Summary](/Airbnb/model_summary.png)

'airbnb_linear_regression' has a linear regression model which also returns an MAE of about $181. This result is similar to that of the Neural network, so it's tough to decide how successful our calculations have become. This information is revealed when we view the R2 score of this linear regression model. This linear regression model has an R2 score of 0.06. That's nearly 0. The closer an R2 score is to 1, The better the score is, and the better our model is explaining the variance in targets. The closer the r2 score is 0, the more likeley it is that the model explains none of the variability.

## Conclusion
This can be interpreted as :
* We are 186$ dollars away from perfect predictions
BUT
* Our model is probably seriously overfit.

This might be the case if a lot of duplicate postings existing.

Our NN is currently deployed on the DS Heroku App [At this Address](https://ds-bw-airbnb-2.herokuapp.com/#/default/predict_predict_post)

This Heroku App predicts a price depending on the values provided in the JSON Submission as you can see below:
![Pic of API](/Airbnb/API.png)

## To Use the API
Simply click on the green "predict" method. You'll see an option similar to the screenshot above, where if you click on the "execute" button, you'll get a returned prediction at the bottom. For the most effective showcase, try adjusting the "square footage" feature in your submission , and you should see a noticeable change in predicted rental price.

