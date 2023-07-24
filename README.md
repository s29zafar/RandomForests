# Introduction

Decision trees leave you with a difficult decision. A deep tree with lots of leaves will overfit because each prediction is coming from 
historical data from only a few houses at its leaf. But a shallow tree with few leaves will perform poorly because it fails to capture 
as many distinctions in the raw data.

Even today's most sophisticated modelling techniques face this tension between underfitting and overfitting. But, many models have 
clever ideas that can lead to better performance. We'll look at the random forest as an example.

# Random Forests

The random forest uses many trees, and it predicts by averaging the predictions of each component tree. It generally has much 
better predictive accuracy than a single decision tree and it works well with default parameters. If you keep modelling, you can learn 
more models with even better performance, but many of those are sensitive to getting the right parameters.

There is likely room for further improvement, but this is a big improvement over the best decision tree accuracy percentage of :
## 99.763%.

There are parameters which allow you to change the performance of the Random Forest much as we changed the maximum depth of the 
single decision tree. But one of the best features of Random Forest models is that they generally work reasonably even without this 
tuning.
