# Satisfaction of Air Passengers Analysis

## Background

**Based on the dataset from [*Kaggle: Airline Passenger Satisfaction by TJ KLEIN*](https://www.kaggle.com/datasets/teejmahal20/airline-passenger-satisfaction)**

- Kaggle Usability: 9.41
- There is a content for data variables description.
- It has a label of binary classification which may contribute to further prediction.

## Analyses for some questions

1. **What factors significantly affect the passengers' satifaction?**

    - We use the `value_counts()` to see whether there are huge differences between the satisfaction of a certain type. If the satisfaction of a factor is distinct, it indicates that the factor is influential to the passengers’ satisfaction.
    - *'Customer Type'*, *'Type of Travel'*, *'Class'* are influential factors in satisfaction. However, *'Gender'* is not an important indicator.

2. **There are 14 aspects related to the satisfaction in the survey. Which aspects are highly correlated and therefore the satisfaction?**

    - We calculate the correlated coefficients of every two criteria and compare.
    - The criteria *'Cleancliness'*, *'Food and drink'*, *'Seat comfort'*, *'Inflight entertainment'* are highly associated. So we can make some possible suggestions that the airline company should take care of cleanliness and comfort when they offer drinking, eating and entertainment service.

## Usage

**Visit the interactive pages on [*Streamlit Cloud*](https://justina1220-final-project-app-satisfaction-jbv6wu.streamlitapp.com/)**

- You can use the slider to choose the upper bound of the flight distance range. For example, if the slider stops at 2000, it means you select data which flight distance is less than 2000.
- You can click the sidebar and choose the seat class and age level you belong to.
- Once you choose correctly and successfully, there will be some balloons flying upwards.
- Then you can see the filterd results and distributions in the following plots (*Distribution of passengers' age*, *The range of flight distance*, *The flight distance with different classes*) changing to the conditions you want. In other words, it predicts the passenger's satisfaction level to some extent.
- In the *Further Analysis* section, you can see the answers and detailed explanations for various factors and plots.
