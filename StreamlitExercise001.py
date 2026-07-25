import streamlit as st
st.set_page_config(layout='wide')

# text
st.title('st title streamlit tutorial')
st.header('st header')
st.subheader('st subheader')
st.text('st text')
st.caption('st caption with _italic_ :blue[colors] \
           and emojis :sunglasses::streamlit:')
st.latex(r''' e^{i\pi} + 1 =0 ''')  #r stands for render
st.markdown('this is a markdown **bold**,*italics* ')
st.divider()
code1='''def hello(text):
            print('helloe {text}')'''  # syntax wrap code 
            # block inside triple quotation marks 
st.code(code1)
st.code('''def calculate_age(birthdate):
            today=pd.to_datetime('today')
            year.diff=today.year-birthdate.year
            if (today.month, today.day) <( birthdate.month , birthdate.day) :
                return year.diff-1 ''')
# color
st.success('color-success')
st.info('color-info')
st.warning('color-warning')
st.error('color-error')
# st.exception("NameError('color-exception')")

# help
# st.help(range)

# write function 
st.write('write')
st.write(range(0,10))

# images|photos|pictures & videos & audio 
from PIL import Image 
img1=Image.open("./assets/images/1.png")
st.image(img1,caption="")   # width better left unset, 
# otherwise it only affect the automatically scaling to fit screen 
# feature
python_img=Image.open('./assets/images/pythonimg.png')
st.image(python_img,caption='')

vidfile=open("./assets/videos/1.mp4","rb").read()
st.video(vidfile,loop=True, autoplay=True, muted=False )
# audio same syntax as video = only exception the required  format argument

# check box & radio button & select box &slider
############## radio button dubugging --to be continued
if st.checkbox('Hide | Show'):
    st.write('Classic info') 

status = st.radio( 'please choose your status',
                  options=['single','married'], key='status_mar1')

if status=='single':
    st.warning('you are single')
else:
    st.success('you are married !')
occupation =st.selectbox('your occupation' ,['Programmer' ,'doctor','data scientist '],key='occupationselectbox1')
st.write('you selected this option ', occupation)

location=st.multiselect('where do you work?',('London','NY','ACC','KIEV','NP'))
st.write('you have selected ' ,len(location) , ' options')

age=st.slider('whats your age',1,100)
st.write(age)

st.button("simple buttom")
if st.button('about'): #when its clicked
    st.text('streamlit is cool')
    
# text input |area box |datetime
x =st.text_input('whats your favorite movie?')
st.write(f"your favorite movie is {x}")

firstname=st.text_input('please enter your firstname')

if st.button('submit'):
    result=firstname.title()
    st.success(result)
    
x =st.text_area('whats your favorite movie?')
st.write(f"your favorite movie is {x}")


from datetime import datetime, timedelta
today1=st.date_input('today is',datetime.now())
st.write('today is',today1)

time1=st.time_input('time is',datetime.now().time())
st.write('time is' , time1)

# Time input with custom step interval of 5 minutes
selected_time0 = st.time_input("Choose a time:", step=timedelta(minutes=5))
st.write("Selected time:", selected_time0)

# Separate date and time inputs
selected_date1 = st.date_input("Select a date:")
selected_time1 = st.time_input("Select a time:")
if selected_date1 and selected_time1:
   combined_datetime = datetime.combine(selected_date1, selected_time1)
   st.write("Combined DateTime:", combined_datetime)
   
st.text('display json')
st.json({'name':'x',
         'nome':'y'})

st.text('display raw code')
st.code('import pandas as pd')


# -----------progress bar------------------
import time 
my_bar=st.progress(0) #value n is ranging from 0 to 100 percentage
for p in range(80):   # 2 scenarios 2.1 static only n 2.2 animated initial 0+for loop
    my_bar.progress(p+1) 
# ----------spinner ===========================
with st.spinner("waiting .."):
    time.sleep(0.5)
st.success('finished!')  
    
# st.balloons()    

# sidebar = st.sidebar()
# csv 
import numpy as np
import pandas as pd
pddf1= pd.read_csv('movies.csv')
st.write(pddf1)

chart_data1=pd.DataFrame(np.random.randn(20,3),
                         columns=['a','b','c'])

st.bar_chart(chart_data1)
st.line_chart(chart_data1)


df_jm1= pd.DataFrame(np.random.randn(20,3),columns=['a','b','c'])
st.header('Pandas Dataframe1')
st.write(df_jm1)

st.area_chart(df_jm1)
st.scatter_chart(df_jm1)

# display key metric|highligh key value using metric|
st.metric(label='current temperature',
          value="76 °F", delta="1.7 °F")
# value and delta can be either static or dynamic via updating 
# from other sources 

# display 3 cols of metrics
col1 , col2 ,col3 =st.columns(3)

with col1:
    st.metric(label='current temperature',
          value="76 °F", delta="1.7 °F")
with col2:
    st.metric(label='current temperature',
          value="76 °F", delta="1.7 °F")
with col3:
    st.metric(label='current temperature',
          value="76 °F", delta="1.7 °F")
    
# container -fluid  parameters:border=Bool   key(id)=srt 
# height|width=stretch|content horizontal=bool horizontal|left_alignment
# gap=(between element) autoscroll=bool |only effective if the container has a flexible height|
simple_container= st.container(border=True)
simple_container.write('this is inside the container')
st.write('this is outside the container')
simple_container.write('this is added value')

# tabs  |very helpful for you to display different data |
st.subheader('tabbed container with images')

tab1, tab2, tab3 = st.tabs(
    [":cat: Cat", ":dog: Dog", ":rainbow[Owl]"], default=":rainbow[Owl]"
)
with tab1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg", 
             width=1200)
with tab2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg", 
             width=1200)
with tab3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg", 
             width=1200)
    
# container elemnts that are initially collapsed
# and expanded on licks (its great to hide reference or figure 
# content that's not meant to shown at the initial launch of 
#  the browser 

st.subheader('Expandable container')
# create bar chart to display a series of number  
bar_df11=pd.DataFrame({'data' : [3,5,2,4,6,2]},
                      index=['One',
                             'Two',
                             'Three',
                             'Four',
                             'Five',
                             'Six'])
st.bar_chart( bar_df11 ,color='red')
# create an expandable container
with st.expander('Display figure explantion'):
    st.write('This chart displays a \
             a series of random numbers between 1 and 6')

# sidebar 
st.sidebar.header('sidebar title')
st.sidebar.write('This is a sidebar where you can add elements \
                 and widgets ')

# collection input widgets insightful and engaging 
# button toggle check box 
st.header('using streamlit input widgets')
reg_form1=st.form('user_registration_form')
first_name=reg_form1.text_input('first_name: ',
                                key='fname_reg_form1')
last_name=reg_form1.text_input('last_name: ',
                                key='lname_reg_form1')
passowrd =reg_form1.text_input('password', 
                                type='password',# mask the character 
                                key='password_reg_form1')
age=reg_form1.slider('what is your current age ')
level=reg_form1.radio('what is your membership level?' ,
                      ['silver','gold','platinum'])
status =reg_form1.checkbox('active member?')


    
st.divider()
submit_button=reg_form1.form_submit_button('submit')
if submit_button:
    st.success('Welcom' +first_name+' '\
                +last_name+' . You are a valued '+  level+'member')
    
on_act = st.toggle("Activate feature")  # toggle button can't be wrapped inside a form
if on_act:
    st.write("Feature activated!")
###### feedback
st.subheader('please provide your feeeback')
sentiment_mapping1 = [":material/thumb_down:", ":material/thumb_up:"]
selected = st.feedback("thumbs")

if selected is not None:
    st.markdown(f"You selected: {sentiment_mapping1[selected]}")

sentiment_mapping2 = ["one", "two", "three", "four", "five"]

selected = st.feedback("stars")
if selected is not None:
    st.markdown(f"You selected {sentiment_mapping2[selected]} star(s).")
    

sentiment_mapping3 = [0,1,2,3,4]

selected = st.feedback("faces")
if selected is not None:
    st.markdown(f"You selected level{sentiment_mapping3[selected]} .")
    
    
# pill

option_map = {
                0: ":material/add:",
                1: ":material/zoom_in:",
                2: ":material/zoom_out:",
                3: ":material/zoom_out_map:",}
selection = st.pills(
                        "Tool",
                        options=option_map.keys(),
                        format_func=lambda option: option_map[option],
                        selection_mode="single",
                    )
st.write(
            "Your selected option: "
            f"{None if selection is None else option_map[selection]}"
        )


sales_df=pd.read_csv('walmart_sales_data.csv')
st.subheader('sales records')
# st.dataframe(sales_df)
sales_df['Date']=pd.to_datetime(sales_df['Date'],format='mixed').dt.date
# avoid problems if datatime types are inconsistant 
st.dataframe(sales_df)

#---------------filter select box-------------------------------
st.subheader('Sales Records Filtered by Holiday')
# single out unique values in holiday flag to use them as filtering conditions 
holiday_options = sales_df['Holiday_Flag'].unique()
# create a select box using return holiday flag unique values 
holiday_selection =st.selectbox('holiday week?(1=Yes, 0=No):',
                                options=holiday_options,key='holiday_select1')
# associate it with data 
filtered_df_selectbox = sales_df[sales_df['Holiday_Flag']==holiday_selection]

st.dataframe(filtered_df_selectbox)


#---------------multi select -------------------------------
st.subheader('sales records filtered by store')
store_options =sales_df['Store'].unique()
store_selection= st.multiselect('select store(s):',
                                options=store_options,
                                default=1)
filtered_df_multiselect= sales_df[sales_df['Store'].isin(store_selection)]
st.dataframe(filtered_df_multiselect)

#-------------date picker pop up ---------------------------
st.subheader('sales records filtered by data range')
# logic between this date picker is to use the existing dataframe's min 
# date as lower boundary and max upper , so that any random picked date will 
# fall into that range making it valid 
min_date=sales_df['Date'].min()
max_date=sales_df['Date'].max()

# default value when the webbrowser loaded , prior to the selection 
# initiated by the user
start_date=min_date  # default value
end_date=max_date    # default value 

# actual selection 
start_date_s=st.date_input('select start date', min_date, 
                         min_value=min_date,
                         max_value=max_date) #default range 

end_date_s=st.date_input('select end date', max_date, 
                         min_value=min_date,
                         max_value=max_date)
st.write(end_date_s)
st.write(f'start_date_s is {start_date_s}')
# make sure the user input data format matches the the one in df by overriding
# start_date_input=pd.to_datetime(start_date_s)
# end_date_input  =pd.to_datetime(end_date_s)
st.write(sales_df['Date'][0])
# st.write(end_date_input)

# make sure start and end date have been selected , and stat date less 
if start_date_s and end_date_s and start_date_s < end_date_s:
    filter_df_date=sales_df[  (sales_df['Date'] >= start_date_s) &
                              (sales_df['Date'] <= end_date_s  )  ]
    st.write('Filtered DataFrame by date range')
    st.dataframe(filter_df_date)
else:
    st.error('please select valid date range')
    
# create a file uploade ==================================
st.subheader('file uploader')
uploaded_file=st.file_uploader('please select a valid csv data file for import')
if uploaded_file is not None:
    imported_df=pd.read_csv(uploaded_file)   
    st.dataframe(imported_df)
    
    

####------------plotly visuals----------------------------
# from numpy.random import default_rng as rng

# df_map1 = pd.DataFrame(
#     rng(0).standard_normal((10, 2)) / [50, 50] + [37.76, -122.4],
#     columns=["lat", "lon"],
# # )

# st.map(df_map1)

df_map2 = pd.DataFrame(  {'longitude':[151.2082848,8.8702368,114.0545429,-73.989308,114.1582831,13.3951309,121.4700152],
                          'latitude':[-33.8698439,48.682336622924254,22.5445741,40.741895,22.2818333,52.5173885,31.2312707]}
                          )
st.map(df_map2)
df_map2['City']=['A','C','D','E','F','F','G']
################### plotting

# import built-in Iris dataset into dataframe
import plotly.express as px
iris_df =px.data.iris()

st.subheader('Iris Dataset')
st.dataframe(iris_df)
# st.write(iris_df.columns)
# scatter plot 
#### df columns 
# sepal_length
# sepal_width
# petal_length
# petal_width
# species
# species_id
basic_scatter_fig1= px.scatter(iris_df , 
                              x='sepal_width',
                              y='sepal_length',
                              color='petal_length') # continuous color bar
st.subheader('Iris Dataset: Basic Scatter Plot1')
st.plotly_chart(basic_scatter_fig1)

basic_scatter_fig2= px.scatter(iris_df , 
                              x='sepal_width',
                              y='sepal_length',
                              color='species') # catagorical data better use of the color parameter
st.subheader('Iris Dataset: Basic Scatter Plot2')
st.plotly_chart(basic_scatter_fig2)

basic_scatter_fig3= px.scatter(iris_df , 
                              x='sepal_width',
                              y='sepal_length',
                              color='species',     # catagorical data better use of the color parameter
                              size='petal_length') # size of the bubble is correlated to the petal_length
st.subheader('Iris Dataset: Basic Scatter Plot3')
st.plotly_chart(basic_scatter_fig3)

basic_scatter_fig4= px.scatter(iris_df , 
                              x='sepal_width',
                              y='sepal_length',    ##----differentiation ----
                              color='species',     ## catagorical data better use of the color parameter
                              size='petal_length', ## size of the bubble is correlated to the petal_length
                              symbol='species',    ## marker
                              hover_data=['petal_width'])   
st.subheader('Iris Dataset: Basic Scatter Plot4')
st.plotly_chart(basic_scatter_fig4)


##### selection = for user interaction 
x_axis1= st.selectbox('Choose a variable for the x-axis', iris_df.columns,index=0,key='iris_df_xaxis1')
y_axis1= st.selectbox('Choose a variable for the y-axis', iris_df.columns,index=1,key='iris_df_yaxis1')


# create bubble chart with color , different symbols and hover data
color_bubble_hover_fig = px.scatter(iris_df,
                                     x=x_axis1, 
                                     y=y_axis1,
                                     color='species',
                                     size='petal_length',
                                     hover_data=['petal_width'])
# display the figure in streamlit
st.subheader('Iris Dataset " bubble chart with selectable axes')
color_bubble_hover_fig.update_layout(font_family='Courier New',
                                     title='Iris Dataset Bubble Chart',
                                     xaxis_title=x_axis1,
                                     yaxis_title=y_axis1,
                                     legend_title='Species')

st.plotly_chart(color_bubble_hover_fig)

import plotly.graph_objects as go
# calculate a correlation matrix 
corr=iris_df.iloc[:,:4].corr()

# create a heatmap
fig = go.Figure(data=go.Heatmap(    z=corr,
                                    x=corr.columns,
                                    y=corr.columns,
                                    colorscale='rainbow'    )  )
                                #   cmap
fig.update_layout(title='Heatmap of iris feature correlation')
st.plotly_chart(fig)

#############################################################
#############################################################
#############################################################
#### -----------select button -----------------------------
st.subheader('please select your chart type')
chart_type=st.selectbox(' chart type dropdown box :' ,[     'Scatter Plot',
                                                            'Line Chart',
                                                            'Bar Chart',
                                                            'Histogram',
                                                            'Box Plot',
                                                            'Pie Chart',
                                                            '3D Scatter Plot'] ,
                        key='chart_type_select_box1')


# visualize the relationship between sepal length and sepal width , colored by species
if chart_type =='Scatter Plot':
    fig = px.scatter(iris_df, 
                     x='sepal_length',
                     y= 'sepal_width',
                     color='species',
                     title='Iris Scatter Plot')
    st.plotly_chart(fig)
    
# since line charts typically require time-series data 
# lets simulate a line chart using the iris dataset index as a faux time-axis
elif chart_type=='Line Chart':
    iris_df_sorted = iris_df.sort_values(by='sepal_length').reset_index()
    fig = px.line(iris_df_sorted, 
                  x=iris_df_sorted.index,
                  y='sepal_length',
                  markers=True,
                  line_dash_map={"setosa": "dash", 
                                 "versicolor": "solid",
                                 'virginica':'dot'}, 
                  color='species',
                  title='Iris sepal length line chart')
    st.plotly_chart(fig)
     
# display the average sepal length of each species using a bar chart 
elif chart_type=='Bar Chart':
    avg_sepal_length =iris_df.groupby('species')['sepal_length'].mean().reset_index()
    fig = px.bar(avg_sepal_length, 
                 x=avg_sepal_length['species'],
                 y=avg_sepal_length['sepal_length'],
                 color=['magenta','cyan','indigo'],
                 title='average sepal length of iris species')
    st.plotly_chart(fig)    
    
# show distribution of sepal lengths across all species
elif chart_type=='Histogram':
    fig=px.histogram(iris_df, 
                     x='sepal_length',
                     title='sepal length distribution')
    st.plotly_chart(fig)
    
# visulize the distribution of sepal lengths for each species using a box plot
elif chart_type =='Box Plot':
    fig = px.box( iris_df,
                  x='species',
                  y='sepal_length',
                  title='sepal length by species')
    st.plotly_chart(fig)
    
# display the distribution of species in the dataset 
elif chart_type=='Pie Chart':
    species_count =iris_df['species'].value_counts().reset_index()
    # ----------------------------------------------.re
    fig = px.pie( species_count,
                  names=species_count['species'],    # label|legend
                  values=species_count['count'],
                  hover_data=[('count'),('species')],
                  hole=True,
                  title='iris species distribution')
    st.plotly_chart(fig)
    
# create a 3D scatter plot showing the sepal length , sepal width, and petal length color by species
elif chart_type=='3D Scatter Plot':
    fig=px.scatter_3d(iris_df,
                     x='sepal_length',
                     y='sepal_width',
                     z='petal_length',
                     color='species',
                     size='sepal_length',
                     title='3D Scatter Plot of Iris dataset') 
    st.plotly_chart(fig)
    
import plotly.graph_objects as go
##### hover template
fig_go_obj1 = go.Figure(go.Scatter(
                                    x=np.arange(0,30,3),
                                    y=np.linspace(1,200,10),
                                    hovertemplate='<i>Price</i>: $%{y:.2f}<br><b>X</b>: %{x}<br><b>%{text}</b>',
                                    text=['customer No {}'.format(i+1) for i in range(10)],
                                    showlegend=False,
                                    line=dict(color='green',
                                              width=13,
                                              dash='dot'
                                              )
                                    ))
st.plotly_chart(fig_go_obj1)