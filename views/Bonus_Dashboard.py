import pandas as pd
import streamlit as st
from streamlit_dynamic_filters import DynamicFilters
import plotly.express as px


# Bonus Calculation/Visualization Function
def Bonus(x):
    # First Part
    if x == 20:
        part_1 = 1
    elif x == 21:
        part_1 = 2
    elif x == 22:
        part_1 = 3
    elif x == 23:
        part_1 = 4
    elif x == 24:
        part_1 = 5
    elif x >= 25:
        part_1 = 6
    else:
        part_1 = 0
    
    part_1 *= 19.5 # commission per hour part 1
    # Second Part
    if 26 <= x < 27:
        part_2 = 1
    elif 27 <= x < 28:
        part_2 = 2
    elif x >= 28:
        part_2 = 3
    else:
        part_2 = 0
    
    part_2 *= 26 # commission per hour part 2
    # Third part
    if x > 28:
        part_3 = x - 20 - 5 - 3
    else:
        part_3 = 0
    part_3 *= 32.5 # commission per hour part 3
    # total
    total_bonus = part_1 + part_2 + part_3
    
    #return f"Calender Week {CW} - Bonus: {total_bonus}€"
    return total_bonus
def Vis(z):
  fig = px.bar(df_filtered.groupby(z).agg(Bonus = ('Bonus_amount_€' ,'sum')).reset_index(), x= z, y='Bonus',
              template='plotly_dark',
              text_auto='.1s'
              )

  # Data Labels
  fig.update_traces(textfont_size=12, textangle=0, textposition='outside',texttemplate="%{y:.2f} €", cliponaxis=False)
  
  # Chart Title
  fig.update_layout(title=f"Bonus € over {z}<br><sup></sup>", title_font_size = 20
                    #, title_x=0.5
                    )
  
  # Margin under Title - Top
  fig.update_layout(margin=dict(t=80))

  # Change Name and Position of Y Axes
  fig.update_yaxes(title='Bonus €', tickfont=dict(size=16))
 
  # Change Name and Position of x Axes
  fig.update_xaxes(tickfont=dict(size=16))
  
  #Y Axis Format
  fig.update_layout( yaxis_ticksuffix=' €')
 
  # Description Margin - Bottom
  fig.update_layout(margin=dict(b=70))
 
  #fig.show()
  st.plotly_chart(fig)


# Title
st.title('Bonus Dashboard')
upload_file = st.file_uploader('Input Excel File'
                              # , type = "xslx"
                               )

if upload_file is not None:
    
    # session_state
    if 'df' not in st.session_state:
    # Function to load and transform data
        @st.cache_data
        def load_data(upload_file):
            # Read Data
            df = pd.read_excel(upload_file,sheet_name='Data',header = 0)
            df = df[['First_day_of_week','Calender_week', 'Working_hours']]
            # Time Transformations
            df['Year'] = df['First_day_of_week'].dt.year.astype(str)
            df['Month'] = ('0'+ df['First_day_of_week'].dt.month.astype(str)).str[-2:]
            df['Year/Month'] = df['Year'].astype(str) + '/' + df['Month']
            df['Year/CW'] = df['Year'].astype(str) + '/' + ('0' + df['Calender_week'].astype(str)).str[-2:]
            df['First_day_of_week'] = df['First_day_of_week'].dt.date
            df['Calender_week'] = df['Calender_week'].astype(str)
            
            # After Decimal Number
            df['AfterDecimal'] = (df['Working_hours'] % 1) * 10**2  # Multiply for precesion
            df['AfterDecimal'] = df['AfterDecimal'].round(0)/60
            # Pre Decimal Number
            df['PreDecimal'] = df['Working_hours'].astype(int)
            df['Working_hours_converted'] = (df['AfterDecimal']+df['PreDecimal']).round(2)
            # Calculate Bonus Amount
            df['Bonus_amount_€'] = df.apply(lambda x: Bonus(x['Working_hours_converted']), axis=1).round(2)
            df = df[['Year', 'Year/Month', 'Month', 'Year/CW', 'Calender_week', 'First_day_of_week', 'Working_hours','Working_hours_converted','Bonus_amount_€']]
            return(df)
        
        # without session_state
        #df = load_data(upload_file)
        st.session_state.df = load_data(upload_file)
        
if 'df' in st.session_state:
    df = st.session_state.df

    # -- Config ---
    date_slicer = {
        'Year': df['Year'].tolist(),
        'Year/Month': df['Year/Month'].tolist(),
        'Year/CW': df['Year/CW'].tolist()
    }


    # -- Slicer & Filter --
    dynamic_filters = DynamicFilters(df, date_slicer) # filters=['Year', 'Year/Month', 'Year/CW']
    dynamic_filters.display_filters(location='columns', num_columns=3, gap='large')
    df_filtered = dynamic_filters.filter_df() # filters the dataframe based on session state values except for the specified filter


    # -- Calculations ---
    Ichiban_list = df.sort_values('Bonus_amount_€', ascending= False).reset_index()
    Ichiban_GRTH = (Ichiban_list.loc[0,'Bonus_amount_€']/Ichiban_list.loc[1,'Bonus_amount_€'])-1
    Bonus_Sum = df_filtered.agg(Sum_Bonus= ('Bonus_amount_€' ,'sum')).reset_index()


    # --- Key Metrcis ---
    first_col, second_col, third_col, fourth_col = st.columns(4)
    with first_col:
        st.metric(label = 'Ichiban: Bonus €', 
                value =f" {Ichiban_list.loc[0,'Bonus_amount_€']} €", 
                help = 'Highest Bonus € ever', 
                #delta= f" {Ichiban_list.loc[1,'Bonus_amount_€']} €" 
                delta= f"GRTH: {Ichiban_GRTH:.2%}"
                )
    with second_col:
        st.metric(label = 'Ichiban: Working Hours', 
                value =f" {Ichiban_list.loc[0,'Working_hours']} hr",
                help = 'Highest Working Hours ever', 
                delta = Ichiban_list.loc[1,'Working_hours'],
                delta_color='off'
                )
    with third_col:
        st.metric(label = 'Ichiban: Year/KW', 
                value = Ichiban_list.loc[0,'Year/CW'], 
                help = 'Most successful Year/CW ever', 
                delta = Ichiban_list.loc[1,'Year/CW'],
                delta_color='off'
                )
        
    with fourth_col:
            st.metric(label = 'Bonus € TTL', 
                    value =f" {Bonus_Sum.loc[0,'Bonus_amount_€']} €",
                    help = 'Bonus € of selected time period'
                    )

    # --- Tabs ---
    tab_year_cw,tab_year_month, tab_year = st.tabs(['Year/CW','Year/Month', 'Year'])
    with tab_year_cw:
        Vis('Year/CW')
    with tab_year_month:
        Vis('Year/Month')
    with tab_year:
        Vis('Year')
    

    # -- Display Data ---
    st.subheader("Data Overview")
    dynamic_filters.display_df(width = 1500, height = 800)
    #st.dataframe(df, width = 1200, height = 500)

else:
    # info text when no file is uploaded
    st.info("Please upload an excel file to continue.")
