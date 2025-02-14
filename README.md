# Bonus Dashboard Streamlit
A Bonus Dashboard built using Python and Streamlit, designed for interactive data visualization and exploration. This project leverages arsentievalex's `DynamicFilters` package to to create dynamic multiselect filters. 

The idea for this project was inspired by my girlfriend. In her job, she can earn commission, i.e. a bonus. This bonus is calculated on the basis of hours worked. In order to get a better overview of her earned bonus, this interactive dashboard was created to visualize the data with the help of the streamlit library. 

Link to the app: https://bonus-dashboard.streamlit.app/

https://github.com/user-attachments/assets/fef72c54-4e37-476e-9140-239b2d8e1003

## Bonus System
| Working Hours | Bonus %  | Bonus €  |
|-------------|----------|---------|
| 20-25      | 15 %     | 19.50   |
| 26-28      | 20 %     | 26.00   |
| 28 >       | 25 %     | 32.50   |

*Hourly Rate: 130 €

## Usage
- For testing purposes, the excel file  „Test_Data_Bonus‟ from the Guthub repository can be used.
- The upload file must be an excel file.  
- Do not change the format (names, tables, tabs) of the upload file. 

Disregarding the above points can lead to errors.

Example Input Data
| First Day of Week | Calendar Week | Working Hours |
|------------------|---------------|--------------|
| 2025-02-03       | 12            | 42.45        |
| 2025-02-10       | 33            | 50.20        |
| 2025-02-17       | 45            | 35.00        |

## Technologies Used

- Streamlit: Framework for building interactive web applications in Python.
- Streamlit Dynamic Filters: Custom component to create dynamic multiselect filters in Streamlit.
- Pandas: Data manipulation and transformation.
- Plotly: Create beautiful, interactive and browser based visualisations.
