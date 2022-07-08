# data102-finalproject

## Analysis of MLB All-Star Pitchers and the Impact of Elevation on Home Runs

### UC Berkeley Data 102 (Data, Inference, and Decisions) Final Project - Fall 2021

#### Contributors: Noah Kaminer, Jonathon Wang, Rodrigo Cochran

### Research Question 1: Can one predict if a pitcher is chosen to be an All-Star in a given year based on pitching statistics?

  Currently, All-Star pitchers are selected by managers, whereas starting fielders are selected by fans, and reserves are selected by managers and players. This selection takes place via tallying of votes. Intuitively, the votes casted by managers to select All-Star pitchers likely relates to not only a pitcher’s pitching statistics that season, but also a number of other factors, such as popularity and league dynamics. The research question above seeks to not only explore the current objectivity in determining All-Star pitchers, but also the feasibility of replacing the voting system with a more objective, statistics-based classification of All-Star pitchers. Prediction with generalized linear models (GLMs) and nonparametric models is a natural fit for this type of research question because it signifies classification and prediction of a binary variable based on continuous variables. Specifically, the nonparametric used will be Random Forest because of the ability to split the data (pitchers) based on numerous pitching statistic thresholds. The GLM used will be Logistic Regression because being an All-Star in a given year is a binary categorical variable. Both of these models will result in a prediction of whether a pitcher is an All-Star in a given year.


### Research Question 2: What is the causal effect of stadium elevation, specifically playing at the Colorado Rockies stadium, on the number of Home Runs scored?

  There are 30 MLB baseball stadiums currently in use. These stadiums can be drastically different from each other in terms of size, elevation, and weather conditions. This question seeks to analyze the effect of elevation on the number of Home Runs at a stadium. Specifically, sitting at 5,211 feet above sea level, the Colorado Rockies stadium (Coors Field) is approximately 4,100 feet further above sea level than any other stadium in the MLB (Arizona Diamondback stadium is 1,059 feet above sea level). While it is assumed that baseballs fly further in higher altitudes, this question seeks to quantify the impact. Causal inference works perfectly for this question because pitch-by-pitch data can be used to model the causal effect of altitude, while also accounting for confounding variables such as statistics relating to the time of impact of each pitch resulting in an in play event. This analysis seeks to help value both hitters and pitchers for the Colorado Rockies. Specifically, if the altitude of the Colorado Rockies stadium has a large causal effect on the number of Home Runs, then their hitters may be overvalued and their pitchers undervalued. The following strategies will help to quantify these impacts and normalize the Rockies’ players against other players in the league.
