## Model Summary ##

This is a modified logistic regression model to estimate the likelihood that a voter is going to participate in the Denver 2023 Municipal election. It factors in 74 different features (voter age, party, past election participation, etc) and outputs a numeric probability for each voter. The model currently has an accuracy of 89% and an F1 score of 82% at a 50% threshold. 

## Problem ##

The two main problems I wanted to address with this model are universe accuracy and voter prioritization.

### Universe Accuracy ###

When we build voter universes in VAN we typically start by selecting groups of voters based on their past voting history. This makes perfect sense because we know that a person’s voting history is the best predictor of whether they will vote in an upcoming election. But should we target voters who have voted in the last 3 elections consecutively, or should we target voters who have voted in 3 of the last 4 elections? What about primary elections? Are certain elections better at predicting turnout than others? I’ve worked on more campaigns than I can remember and have built many different voter universes and in every case I can recall, we didn’t know the answer to those questions. We simply picked some combination of voting history and built the universe from there. 

To be fair, even without answers to those questions campaigns can capture a large share of the voter base in a universe. For example, we can capture around 66% of the Denver 2019 Spring Municipal election voters by creating a universe that consists of people who have voted in the 3 preceding elections. Additionally, there are other factors that are correlated with voter turn out. A voter’s age, primary activity, party affiliation have all shown to have some relationship to their election turnout chances. 

With machine learning, we can use statistical analysis to determine which combination of voting history and other factors are most likely to predict whether someone will vote in an upcoming election. We can then apply that model to every voter in VAN to predict the probability that they will vote in the upcoming election. Think about how many close elections you’ve seen and consider that a campaign with a universe consisting of voters who have voted in the last 3 elections may be targeting significantly different populations than a campaign targeting voters who have participated in 3 of the last 5 elections. What each campaign chose may have ultimately decided who won the election. Something as important as universe creation should be backed by data.

### Voter Prioritization ###

Another problem we run into with traditional voter universes is that we often treat each voter as if they are equally likely to vote. However, even within a well targeted universe there is a range of probabilities. A voter with a 65% chance of voting should probably be treated differently (in some ways) than a voter who has a 95% chance of voting. Should a campaign really spend valuable resources on GOTV for a voter with a 95% chance to vote? If funds come up short for the final mailer and we can't send it to the whole universe, maybe we could prioritize those with a higher voting probability.

Instead of having a single universe of voters you could use voting probabilities to create tiers of voters according to their predicting voting probability. If one precinct has too many doors to canvass on a given day, maybe it makes sense to canvass the tier 1 voters in that precinct which consists of voters who have an 80% + probability of voting. Extra funds for a GOTV text? Maybe it makes sense to target tier 3 voters who have a lower voting probability of 60-70%. These are all made up scenarios and they may or may not make sense in your campaign, but the general idea is the same for any campaign. By having voting probability for each voter you can make more informed decisions about how to deploy campaign resources in order to maximize their effectiveness.  

## Model Performance ##

In machine learning lingo, this is called a classification model because its goal is to separate voters into two classes, those who voted in the 2019 Denver Municipal election and those who did not. I mentioned the model’s accuracy before, but evaluating the performance if a classification model requires a little more than accuracy. 

For example, if we only targeted people who were > 90%  likely to vote (a 90% threshold) our model would be very precise. We would have very few ‘false positives’ (people who we thought would vote but ended up not voting), however the tradeoff is that we would have a huge amount of ‘false negatives’ (people who were not in our model but did end up voting). 

On the other end of the spectrum, we could target people who were > 50% likely to vote (a 50% threshold). That would reduce the number of false negatives because we are targeting so many more people, but expanding the universe that much would give us a ton of voters who end up not voting (false positives). These aspects are known as precision and recall. There isn’t a single ‘best case’ for these metrics. It really just depends on how the model is used.

- A not precise model may find a lot of the voters, but it's selection method is noisy: it also wrongly detects many voters that won't actually vote.

- A precise model is very “pure”: maybe it does not find all the voters, but the ones that the model does class as voters are very likely to be correct.

- A model with high recall succeeds well in finding all the voters  in the data, even though they may also wrongly identify people who end up not voting.

- A model with low recall is not able to find all (or a large part) of the voters.

Accuracy is simply the total number of correct predictions divided by the # of total predictions. Here is a table with this model’s performance at various thresholds:

![image](https://user-images.githubusercontent.com/102785707/213332294-0a7c190f-e7c0-421f-af6f-da34cfd70140.png)

This line chart shows the true and false positive rate at increasing thresholds. As you can see, it maintains a low rate of false positives (voters who the model says will vote who ended up not voting) all the way up to around 0.8 (80% threshold). Once we get above 80% we start seeing increases in the rate of false positives.

![image](https://user-images.githubusercontent.com/102785707/213332427-14e92d8b-0bc2-47cc-8152-3ff7aa436c7d.png)
