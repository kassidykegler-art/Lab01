import streamlit as st
st.title("Quiz")#NEW
st.subheader("What kind of cake are you?")
st.subheader("This quiz will tell you what kind of cake you are!")
st.divider()#NEW
st.subheader("Question 1")
st.radio("Do you go with the flow or have everything planned out?",["Go with the flow", "Plan everything out"]) #NEW
st.header("Question 2")
st.selectbox("How do you feel about carrots", ("Hate them", "Love them"))
st.header("Question 3")
st.slider("How many slices of cake do you have in a day?",0,10)
st.header("Question 4")
st.selectbox("Do you like chocolate?",("Yes", "No", "Kinda"))
st.header("Question 5")
cake_type = st.radio("Be honest, what kind of cake do you want to be?",["Red Velvet Cake", "Chocolate Cake", "Carrot Cake", "Vanilla Cake", "Pineapple Upside Down Cake"])
complete = st.button("Submit")
if complete:
    if cake_type == "Red Velvet Cake":
        st.divider()
        st.subheader("You're a Red Velvet Cake!")
        st.image("Images/red.jpeg")
        st.write("Mysterious, elegant, dependable")
    elif cake_type == "Chocolate Cake":
        st.divider()
        st.subheader("You're a Chocolate Cake!")
        st.image("Images/chocolate.jpeg")
        st.write("Reliable, caring, iconic")
    elif cake_type == "Vanilla Cake":
        st.divider()
        st.subheader("You're a Vanilla Cake!")
        st.image("Images/vanilla.jpeg")
        st.write("Classic, calm, reliable")
    elif cake_type == "Carrot Cake":
        st.divider()
        st.balloons()
        st.subheader("You're a Carrot Cake!")
        st.image("Images/carrot.jpeg")
        st.write("Unique, unpredictable, warm")
    else:
        st.divider()
        st.subheader("You're a Pineapple Upside Down Cake!")
        st.image("Images/pineapple.jpeg")
        st.write("Unconventional, bold, playful")
