import streamlit as st

st.title("AI Traveller APP")

Destination =st.text_input("Enter Destination:")
Travel_date=st.text_input("Enter Travel Date:")
budget=st.number_input("Enter Budget: ")

travel_type=st.selectbox(
    "Travel Type",
    ["Solo","Family","Couple","Business"]
    )

interest =st.multiselect(
    "Interest",
    ["Beach","Temple","Adventure","Nature"]
)

if st.button("Submit"):
    st.write(f"""
    ###Travel Summary

    Destination \t : {Destination}

    Travel Date \t : {Travel_date}

    Budgent \t : ₹{budget}

    Travel_type \t : {travel_type}

    Interst \t :{interest}

    """)

print("Thank you")
