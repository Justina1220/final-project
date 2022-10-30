# Satisfaction of Air Passengers Analysis

## Background

**Based on the dataset from [*Kaggle: Airline Passenger Satisfaction by TJ KLEIN*](https://www.kaggle.com/datasets/teejmahal20/airline-passenger-satisfaction)**

- Kaggle Usability: 9.41
- There is a content for data variables description.
- It has a label of binary classification which may contribute to further prediction.

## Analyses for some questions

1. **What factors significantly affect the passengers' satifaction?**

    - *'Customer Type'*, *'Type of Travel'*, *'Class'* are influential factors in satisfaction. However, *'Gender'* is not an important indicator.

2. **There are 14 aspects related to the satisfaction in the survey. Which aspects are highly correlated and therefore the satisfaction?**

    - The criteria *'Cleancliness'*, *'Food and drink'*, *'Seat comfort'*, *'Inflight entertainment'* are highly associated. So we can make some possible suggestions that the airline company should take care of cleanliness and comfort when they offer drinking, eating and entertainment service.

## Usage

**Visit the interactive pages on [*Streamlit Cloud*](https://justina1220-final-project-app-satisfaction-jbv6wu.streamlitapp.com/)**

- You can use the slider to choose a flight distance range. For example, if the slider stops at 2000, it means you select data which flight distance is less than 2000.
- You can click the sidebar and choose the seat class and age level you belong to.
- Once you choose correctly and successfully, there will be some balloons flying upwards. Then you can see the plots (*Distribution of passengers' age*, *The range of flight distance*, *The flight distance with different classes*) changing to the conditions you want. In other words, it predicts the passenger's satisfaction level to some extent.
