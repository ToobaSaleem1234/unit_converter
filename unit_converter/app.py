import streamlit as st

st.markdown(
   """
   <style>
   body 
   {
   background-color: black;
   color: white;
   }
   .stButton>button
   {
   background: linear-gradient (45deg, #0b5394, #351c75 );
   color: black;
   border-radius: 10px;
   padding: 7px;
   transition: 0.3s;
   box-shadow: 0px 5px 15px rgba(0, 201, 255, 0.4);
   }
   .stButton>button:hover
   {
   tranform : scale(1.05);
   background: linear-gradient(to left, #33ccff 0%, #ff99cc 100%);
   color: black;
   }
   
   .footer 
   {
   text-align:center;
   margin-top :70px;
   font-size: 30px;
   color: purple;
   text-decoration :underline
   }
   </style>
   """,
   unsafe_allow_html= True
   
)

st.title("🔄 Unit Converter App:")
st.markdown(" ### Converts Length, Weight And Time Instantly")
st.write("Welcome! Select a category, enter a value and get the results in real-time")

category = st.selectbox("Choose Category:",["Length", "Weight", "Time", "Temperature"])

def convert_units(category, value, unit):
    # length
    if(category == 'Length'):
        if unit == "Kilometers to Miles":
            return value * 2.20462
        elif unit =="Miles to Kilometers":
            return value / 2.20462
        elif unit =="Meter to Centimeter":
            return value * 100
        elif unit =="Centimeter to Meter":
            return value / 100
    
    # weight
    elif (category == 'Weight'):
        if unit == "Kilogram to Pounds":
         return value * 2.20462
        elif unit == "Pounds to Kilogram":
            return value / 2.20462
        elif unit == 'Kilogram to Gram':
            return value * 1000
        elif unit == "Gram to Kilogram":
            return value / 1000
    
    # time
    elif (category == 'Time'):
        if unit == "Hours to Minutes":
            return value * 60
        elif unit == "Seconds to Minutes":
            return value / 60
        elif unit == "Minutes to Hours":
            return value / 60
        elif unit == "Minutes to Seconds":
            return value * 60
        elif unit == "Hours to Days":
            return value / 24
        elif unit == "Hours to Minutes":
            return value * 60
        elif unit == "Hours to Seconds":
            return value * 3600
        elif unit == "Days to Hours":
            return value * 24
        elif unit == "Days to Weeks":
            return value / 7
        elif unit == "Days to Months":
            return value / 30
        elif unit == "Months to Year":
            return value / 12
        elif unit == "Year to Days":
            return value * 365
        elif unit == "Weeks to Days":
            return value * 7
    
    # temperature
    elif(category == 'Temperature'):
        if unit == 'Degree Celcius to Fahreneit':
            return value * 9/5 + 32
        elif unit == 'Fahreneit to Degree Celcius':
            return value -32 * 5/9

    return 0
if (category == 'Length'):
        unit = st.selectbox("Select Conversation", ["Kilometers to Miles", "Miles to Kilometers", "Meter to Centimeter", "Centimeter to Meter" ])

elif ( category == 'Weight'):
    unit = st.selectbox("Select Conversation",["Kilogram to Pounds", "Pounds to Kilogram", 'Kilogram to Gram', "Gram to Kilogram" ])

elif (category == 'Time'):
    unit = st.selectbox("Select Conversation",["Hours to Minutes", "Seconds to Minutes", "Minutes to Hours", "Minutes to Seconds" , "Hours to Days" , "Hours to Minutes", "Hours to Seconds", "Days to Hours", "Days to Weeks","Days to Months", "Months to Year","Year to Days", "Weeks to Days" ])

elif ( category == 'Temperature'):
    unit = st.selectbox("Select Conservation", ['Degree Celcius to Fahreneit', 'Fahreneit to Degree Celcius'])

value = st.number_input("Enter value to convert:")

# button
if st.button("Convert"):
    result = convert_units(category, value, unit)
    st.success(f"Converted value is:{result: 2f}")

# footer
st.markdown("<div class='footer'> Created by Tooba Saleem </div>",unsafe_allow_html = True)
