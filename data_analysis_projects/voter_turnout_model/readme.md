* Model Summary *

The model uses a classification algorithm called a logistic regression to estimate the likelihood that a voter is going to participate in the Denver 2023 Municipal election. It factors in 74 different features (voter age, party, past election participation, etc) and outputs a numeric probability for each voter. The model currently has an accuracy of 89% and an F1 score of 82% at a 50% threshold. I’ll talk more about model performance below.

Problem

The two main problems I wanted to address with this model are universe accuracy and voter prioritization.

Universe Accuracy

When we build voter universes in VAN we typically start by selecting groups of voters based on their past voting history. This makes perfect sense because we know that a person’s voting history is the best predictor of whether they will vote in an upcoming election. But should we target voters who have voted in the last 3 elections consecutively, or should we target voters who have voted in 3 of the last 4 elections? What about primary elections? Are certain elections better at predicting turnout than others? I’ve worked on more campaigns than I can remember and have built many different voter universes and in every case I can recall, we didn’t know the answer to those questions. We simply picked some combination of voting history and built the universe from there. 

To be fair, even without answers to those questions campaigns can capture a large share of the voter base in a universe. For example, we can capture around 66% of the Denver 2019 Spring Municipal election voters by creating a universe that consists of people who have voted in the 3 preceding elections. Additionally, there are other factors that are correlated with voter turn out. A voter’s age, primary activity, party affiliation have all shown to have some relationship to their election turnout chances. 

With machine learning, we can use statistical analysis to determine which combination of voting history and other factors are most likely to predict whether someone will vote in an upcoming election. We can then apply that model to every voter in VAN to predict the probability that they will vote in the upcoming election. Think about how many close elections you’ve seen and consider that a campaign with a universe consisting of voters who have voted in the last 3 elections may be targeting significantly different populations than a campaign targeting voters who have participated in 3 of the last 5 elections. What each campaign chose may have ultimately decided who won the election. Something as important as universe creation should be backed by data.

Voter Prioritization

Another problem we run into with traditional voter universes is that we often treat each voter as if they are equally likely to vote. However, even within a well targeted universe there is a range of probabilities. A voter with a 65% chance of voting should probably be treated differently (in some ways) than a voter who has a 95% chance of voting. Should a campaign really spend valuable resources on GOTV for a voter with a 95% chance to vote? If funds come up short for the final mailer and we can't send it to the whole universe, maybe we could prioritize those with a higher voting probability.

Instead of having a single universe of voters you could use voting probabilities to create tiers of voters according to their predicting voting probability. If one precinct has too many doors to canvass on a given day, maybe it makes sense to canvass the tier 1 voters in that precinct which consists of voters who have an 80% + probability of voting. Extra funds for a GOTV text? Maybe it makes sense to target tier 3 voters who have a lower voting probability of 60-70%. These are all made up scenarios and they may or may not make sense in your campaign, but the general idea is the same for any campaign. By having voting probability for each voter you can make more informed decisions about how to deploy campaign resources in order to maximize their effectiveness.  

Model Creation

This model was built to predict turnout for the 2019 Denver Municipal Election. I exported voter data from VAN and removed any features that were from after 2019. I then trained a modified logistic regression algorithm on 80% of that data. The objective with this training is for the algorithm to learn what features (age, party voting history etc) were the best predictors of whether or not a person voted in the 2019 municipal election. Features that were most important, like voting history, are given a higher weight than features like sex, which ended up non being related to voter turnout. All of those features and their respective weights end up in one big equation which ends up being the model.

I used the 2019 Denver Municipal Election because it’s the closest we have to the upcoming election. Will there be factors at play in 2023 that were around in 2019? Definitely. But using existing data and statistics is the best method we have for predicting what will happen next.

After the model was trained, I then tested it on the 20% of voter data that it has not seen so that I could evaluate its performance. 

Model Performance

In machine learning lingo, this is called a classification model because its goal is to separate voters into two classes, those who voted in the 2019 Denver Municipal election and those who did not. I mentioned the model’s accuracy before, but evaluating the performance if a classification model requires a little more than accuracy. 

For example, if we only targeted people who were > 90%  likely to vote (a 90% threshold) our model would be very precise. We would have very few ‘false positives’ (people who we thought would vote but ended up not voting), however the tradeoff is that we would have a huge amount of ‘false negatives’ (people who were not in our model but did end up voting). 

On the other end of the spectrum, we could target people who were > 50% likely to vote (a 50% threshold). That would reduce the number of false negatives because we are targeting so many more people, but expanding the universe that much would give us a ton of voters who end up not voting (false positives). These aspects are known as precision and recall. There isn’t a single ‘best case’ for these metrics. It really just depends on how the model is used.

A not precise model may find a lot of the voters, but it's selection method is noisy: it also wrongly detects many voters that won't actually vote.

A precise model is very “pure”: maybe it does not find all the voters, but the ones that the model does class as voters are very likely to be correct.

A model with high recall succeeds well in finding all the voters  in the data, even though they may also wrongly identify people who end up not voting.

A model with low recall is not able to find all (or a large part) of the voters.

Accuracy is simply the total number of correct predictions divided by the # of total predictions. Here is a table with this model’s performance at various thresholds:

This line chart shows the true and false positive rate at increasing thresholds. As you can see, it maintains a low rate of false positives (voters who the model says will vote who ended up not voting) all the way up to around 0.8 (80% threshold). Once we get above 80% we start seeing increases in the rate of false positives. 





Existing VAN Scores

VAN comes with various scores built in. One of them performed better than all of the rest. It’s called “Off Gen,” and it tries to model voter turnout for off years and it kind of works. I tested its accuracy and it performed 10% worse than this model. When I tested and scored this new model I removed the data for the 2019 election. If you’re going to test a model you have to ensure the data you give it does not contain the answer to the question you’re building it to answer. That’s a little like giving a student the answers to a test and then using the test grade to determine how well the student knew the material. The Off Gen score had the answers to the test and still performed 10% worse than this new model. That leads me to believe it will perform much more poorly when it doesn’t have the answer, like for the 2023 elections.

Summary 

I’m hesitant to make specific recommendations because I don’t know all of the specifics of your campaign plan, budget, volunteer capacity etc. If it were me, I would create the universe with two distinct components: voting probability (as estimated by the model) and how likely they are to support Sarah. I don’t know what factors would go into the latter, but I can see some of them in the universe right now. Using those two components I would create different tiers of the universe so that you can prioritize your outreach and eventual GOTV efforts based on those two components. I have some other ideas, but this is already a lengthy write-up so I’ll save that for another time.

If it’s ok with the team, I’d like to publish some of this work to my profile. I’m trying to break into the world of progressive data/tech and projects like these can prove that I have some of the technical skills I say I have. I will redact the details of the model itself until after election day to prevent any competitors from outright stealing it. Let me know if that works for you.

Next Steps

I’ve already deployed the model on the entire Denver voting population. If you decided to use it, the next step would be adding that info in VAN via bulk upload. Lastly, I’m planning to show the model to some more experienced data scientists to ensure I didn’t make any mistakes. I’ve manually checked and verified the models performance so I feel pretty confident, but having an extra set of eyes on it can’t hurt.

Thanks!

Jon


