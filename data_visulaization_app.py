import streamlit as st
import pandas as pd
import datetime

data = pd.read_csv("customer_records.csv")

# title of the app

st.title("Data Visulization App")

# Add a sidebar

st.sidebar.subheader("Visualization Settings")
value = st.sidebar.selectbox("Select the option", ["Home", "Visualise"])

# Navigation

if value == "Home":
    tab1, tab2, tab3 = st.tabs(["Ladies", "Men", "Kid"])
    with tab1:
        st.header("Ladies")
        img1, text1 = st.columns(2)
        with img1:
            st.image("https://th.bing.com/th/id/OIP.uPHBSd2XJwHOEcSw88SNPgHaMV?w=193&h=322&c=7&r=0&o=5&dpr=1.3&pid=1.7",
                     width=200)
        with text1:
            st.subheader("999")
            month = datetime.datetime.now().month
            ex = month
            sal = "999"
            if st.button(label="Order now", key=1):
                to_add = {"Timeline": [ex], "Cost": [sal]}
                to_add = pd.DataFrame(to_add)
                to_add.to_csv("customer_records.csv", mode='a', header=False, index=False)
                st.success("Submitted")

        img2, text2 = st.columns(2)
        with img2:
            st.image("https://th.bing.com/th?id=OPA.AsTkiL0zmE%2ft1w474C474&w=195&h=253&o=5&dpr=1.3&pid=1.7", width=200)
        with text2:
            st.subheader("799")
            month = datetime.datetime.now().month
            ex = month
            sal = "799"
            if st.button(label="Order now", key=2):
                to_add = {"Timeline": [ex], "Cost": [sal]}
                to_add = pd.DataFrame(to_add)
                to_add.to_csv("customer_records.csv", mode='a', header=False, index=False)
                st.success("Submitted")

        img3, text3 = st.columns(2)
        with img3:
            st.image("https://th.bing.com/th/id/OIP.u9lCVCCT0A7eBaoXLYCO5AHaJ_?w=203&h=274&c=7&r=0&o=5&dpr=1.3&pid=1.7"
                     , width=200)
        with text3:
            st.subheader("1999")
            month = datetime.datetime.now().month
            ex = month
            sal = "1999"
            if st.button(label="Order now", key=3):
                to_add = {"Timeline": [ex], "Cost": [sal]}
                to_add = pd.DataFrame(to_add)
                to_add.to_csv("customer_records.csv", mode='a', header=False, index=False)
                st.success("Submitted")

        img4, text4 = st.columns(2)
        with img4:
            st.image("https://th.bing.com/th?id=OPA.%2fwCfS4ynJ7sdxQ474C474&w=195&h=253&o=5&dpr=1.3&pid=1.7", width=200)
        with text4:
            st.subheader("599")
            month = datetime.datetime.now().month
            ex = month
            sal = "599"
            if st.button(label="Order now", key=4):
                to_add = {"Timeline": [ex], "Cost": [sal]}
                to_add = pd.DataFrame(to_add)
                to_add.to_csv("customer_records.csv", mode='a', header=False, index=False)
                st.success("Submitted")

    with tab2:
        st.header("Mens")
        img1, text1 = st.columns(2)
        with img1:
            st.image("https://th.bing.com/th/id/OIP.C24IFyy_aHV87_qpZLw6HQHaLI?pid=ImgDet&rs=1",
                     width=200)
        with text1:
            st.subheader("1999")
            month = datetime.datetime.now().month
            ex = month
            sal = "1999"
            if st.button(label="Order now", key=5):
                to_add = {"Timeline": [ex], "Cost": [sal]}
                to_add = pd.DataFrame(to_add)
                to_add.to_csv("customer_records.csv", mode='a', header=False, index=False)
                st.success("Submitted")

        img2, text2 = st.columns(2)
        with img2:
            st.image("https://th.bing.com/th/id/OIP._LQDX7Nj0SQz1jHnm9_H4wHaLG?w=203&h=304&c=7&r=0&o=5&dpr=1.3&pid=1.7", width=200)
        with text2:
            st.subheader("2799")
            month = datetime.datetime.now().month
            ex = month
            sal = "2799"
            if st.button(label="Order now", key=6):
                to_add = {"Timeline": [ex], "Cost": [sal]}
                to_add = pd.DataFrame(to_add)
                to_add.to_csv("customer_records.csv", mode='a', header=False, index=False)
                st.success("Submitted")

        img3, text3 = st.columns(2)
        with img3:
            st.image("https://images.squarespace-cdn.com/content/v1/54661df4e4b0c1af99306b69/1492348533703-6Y410GMSC4NWVTDRU2ON/ke17ZwdGBToddI8pDm48kMXRibDYMhUiookWqwUxEZ97gQa3H78H3Y0txjaiv_0fDoOvxcdMmMKkDsyUqMSsMWxHk725yiiHCCLfrh8O1z4YTzHvnKhyp6Da-NYroOW3ZGjoBKy3azqku80C789l0luUmcNM2NMBIHLdYyXL-Jww_XBra4mrrAHD6FMA3bNKOBm5vyMDUBjVQdcIrt03OQ/0G9A6814.jpg"
                     , width=200)
        with text3:
            st.subheader("3999")
            month = datetime.datetime.now().month
            ex = month
            sal = "3999"
            if st.button(label="Order now", key=7):
                to_add = {"Timeline": [ex], "Cost": [sal]}
                to_add = pd.DataFrame(to_add)
                to_add.to_csv("customer_records.csv", mode='a', header=False, index=False)
                st.success("Submitted")

        img4, text4 = st.columns(2)
        with img4:
            st.image("https://th.bing.com/th/id/OIP.xdOEoXBfyMxkePrqREzEMQHaLG?w=203&h=304&c=7&r=0&o=5&dpr=1.3&pid=1.7", width=200)
        with text4:
            st.subheader("2599")
            month = datetime.datetime.now().month
            ex = month
            sal = "2599"
            if st.button(label="Order now", key=8):
                to_add = {"Timeline": [ex], "Cost": [sal]}
                to_add = pd.DataFrame(to_add)
                to_add.to_csv("customer_records.csv", mode='a', header=False, index=False)
                st.success("Submitted")

    with tab3:
        st.header("Children")
        img1, text1 = st.columns(2)
        with img1:
            st.image("https://th.bing.com/th/id/OIP.8pTu-buFZig752fON-86agHaHa?w=213&h=213&c=7&r=0&o=5&dpr=1.3&pid=1.7",
                     width=200)
        with text1:
            st.subheader("599")
            month = datetime.datetime.now().month
            ex = month
            sal = "599"
            if st.button(label="Order now", key=9):
                to_add = {"Timeline": [ex], "Cost": [sal]}
                to_add = pd.DataFrame(to_add)
                to_add.to_csv("customer_records.csv", mode='a', header=False, index=False)
                st.success("Submitted")

        img2, text2 = st.columns(2)
        with img2:
            st.image("https://th.bing.com/th/id/OIP.qdGVJRI0s7mH2ni_7UR8cQHaHa?w=203&h=203&c=7&r=0&o=5&dpr=1.3&pid=1.7",
                     width=200)
        with text2:
            st.subheader("799")
            month = datetime.datetime.now().month
            ex = month
            sal = "799"
            if st.button(label="Order now", key=10):
                to_add = {"Timeline": [ex], "Cost": [sal]}
                to_add = pd.DataFrame(to_add)
                to_add.to_csv("customer_records.csv", mode='a', header=False, index=False)
                st.success("Submitted")

        img3, text3 = st.columns(2)
        with img3:
            st.image(
                "https://th.bing.com/th/id/OIP.2wYO4GLFVZJGGifAZopeawHaHa?w=203&h=203&c=7&r=0&o=5&dpr=1.3&pid=1.7"
                , width=200)
        with text3:
            st.subheader("999")
            month = datetime.datetime.now().month
            ex = month
            sal = "999"
            if st.button(label="Order now", key=11):
                to_add = {"Timeline": [ex], "Cost": [sal]}
                to_add = pd.DataFrame(to_add)
                to_add.to_csv("customer_records.csv", mode='a', header=False, index=False)
                st.success("Submitted")

        img4, text4 = st.columns(2)
        with img4:
            st.image("https://th.bing.com/th/id/OIP.03aV1tFcGBu1UADe79lcDAHaHa?w=213&h=213&c=7&r=0&o=5&dpr=1.3&pid=1.7",
                     width=200)
        with text4:
            st.subheader("599")
            month = datetime.datetime.now().month
            ex = month
            sal = "599"
            if st.button(label="Order now", key=12):
                to_add = {"Timeline": [ex], "Cost": [sal]}
                to_add = pd.DataFrame(to_add)
                to_add.to_csv("customer_records.csv", mode='a', header=False, index=False)
                st.success("Submitted")

if value == "Visualise":
    if st.checkbox("Show Table"):
        st.table(data)
    graph = st.selectbox("What kind of Graph?", ["Line", "Bar"])
    val = st.slider("Filter data using month", 1, 12)
    data = data.loc[data["Timeline"] == val]
    if graph == "Line":
        value = pd.DataFrame(data, columns=["Cost"])
        st.line_chart(value)
    if graph == "Bar":
        value = pd.DataFrame(data, columns=["Cost"])
        st.bar_chart(value)





