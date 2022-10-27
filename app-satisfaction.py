import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('seaborn')

st.title('Satisfaction of airline passengers')
st.image('shuaige.jpg')
df =pd.read_csv(r'train.csv')


#add a slider
distance_slider = st.slider('Flight Distance', 0, 5000, 2000)

st.subheader('See more filters in the sidebar:')

# add a multi select
class_filter = st.sidebar.multiselect(
     'Choose the seat class',
     df.Class.unique(),  # options
     df.Class.unique())  # defaults

# add a radio button
age_filter = st.sidebar.radio(
    'Choose age level',
    ('Young', 'Middle-aged', 'Old')
)


#filter by flight distance
df = df[df['Flight Distance'] <= distance_slider]

# filter by class type
df = df[df.Class.isin(class_filter)]

# filter by age level
if age_filter == 'Young':
    df = df[df.Age <= 20]
    st.sidebar.image('shuaige4.jpg')
elif age_filter == 'Old':
    df = df[df.Age > 55]
    st.sidebar.image('shuaige3.jpg')
elif age_filter == 'Middle-aged':
    df = df[(df.Age > 20) & (df.Age <= 55)]
    st.sidebar.image('shuaige2.jpg')
#show the df
st.write(df)

#show the age distribution
st.subheader('Distribution of passengers\' age:')
fig,ax = plt.subplots()
df.Age.plot.hist(bins=10,ax=ax)
ax.set_ylabel('Quantity')
ax.set_xlabel('Age')
st.pyplot(fig)

#show the flght distance range
st.subheader('The range of flight distance:')
fig,ax = plt.subplots()
df1 = df.sort_values(by = 'Flight Distance', ascending = False, ignore_index = True)
df1['Flight Distance'].plot().set_ylabel('Flight Distance')
st.pyplot(fig)

#show the box plot for flight distance with different classes
st.subheader('The flight distance with different classes:')
fig, ax = plt.subplots(1,3,figsize = (15, 5)) 
df[df['Class'] == 'Eco']['Flight Distance'].plot.box(ax = ax[0])
df[df['Class'] == 'Eco Plus']['Flight Distance'].plot.box(ax = ax[1])
df[df['Class'] == 'Business']['Flight Distance'].plot.box(ax = ax[2])
ax[0].set_xlabel('Class = Eco')  
ax[1].set_xlabel('Class = Eco Plus')  
ax[2].set_xlabel('Class = Business')  
ax[0].set_ylabel('Flight Distance')
st.pyplot(fig)


st.title('Further Analysis')
#===============Analysis1=======================
st.subheader('Factors that might affect customer satisfaction:')
tab1, tab2, tab3, tab4= st.tabs(["Gender", "Customer Type", "Type of Travel","Class"])

with tab1:
   st.image("Gender.png", width=500)
   with st.expander("See analysis"):
    st.write("""
        The heatmap above shows the relationship between every two criteria,and we can clearly see...
    """)

with tab2:
   st.image("Customer Type.png", width=500)
   with st.expander("See analysis"):
    st.write("""
        The heatmap above shows the relationship between every two criteria,and we can clearly see...
    """)

with tab3:
   st.image("Type of Travel.png", width=500)
   with st.expander("See analysis"):
    st.write("""
        The heatmap above shows the relationship between every two criteria,and we can clearly see...
    """)

with tab4:
   st.image("Class.png", width=500)
   with st.expander("See analysis"):
    st.write("""
        The heatmap above shows the relationship between every two criteria,and we can clearly see...
    """)

#=================Analysis2======================
#show the heatmap over criteria
df0=pd.read_csv(r'train.csv')
st.subheader('The heatmap over 14 criteria:')
fig,ax = plt.subplots()
corr = df0[['Inflight wifi service','Departure/Arrival time convenient','Ease of Online booking','Gate location','Food and drink','Online boarding',
'Seat comfort','Inflight entertainment','On-board service','Leg room service','Baggage handling','Checkin service','Inflight service','Cleanliness']].corr()
heatmap = sns.heatmap(corr,cmap='GnBu')
st.pyplot(fig)
with st.expander("See analysis"):
    st.write("""
        The heatmap above shows the relationship between every two criteria,and we can clearly see...
    """)
    st.image("https://static.streamlit.io/examples/dice.jpg")

st.balloons()