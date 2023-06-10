import streamlit as st
from PIL import Image
import requests
import yaml

PATH_CONFIG = "/home/muhfaridansutariya/asistensi_mlprocess/MLProcess/Asistensi/streamlit/config.yaml"

config = yaml.safe_load(open(PATH_CONFIG))

st.set_page_config(
    page_title="Iris Classifier",
    page_icon=":bar_chart:",
    layout="centered"
)

# upload image
img_path = Image.open(config['assets']['img'])
st.image(img_path)
st.title("IRIS Classifier")

# create an empty list to store the results
results = []

# create form
with st.form(key="iris_classifier_form",clear_on_submit=True):
    sepal_length = st.number_input(
        label="input your sepal length value:",
        min_value=0.0,
        help="Example value: 5.1"
    )

    sepal_width = st.number_input(
        label="input your sepal width value:",
        min_value=0.0,
        help="Example value: 3.1"
    )

    petal_length = st.number_input(
        label="input your petal length value:",
        min_value=0.0,
        help="Example value: 1.1"
    )

    petal_width = st.number_input(
        label="input your petal width value:",
        min_value=0.0,
        help="Example value: 2.1"
    )

    submitted = st.form_submit_button('predict')

    if submitted:
        # collect data from form
        form_data = {
            "sepal_length": sepal_length,
            "sepal_width": sepal_width,
            "petal_length": petal_length,
            "petal_width": petal_width
        }

        # sending the data to the prediction server
        with st.spinner("Sending data to the prediction server... please wait..."):
            res = requests.post("{}".format(config['server']['url']), json=form_data).json()

        # parse the prediction result
        if res['status'] == 200:
            results.append(res['message'])  # add the result to the list of results
            st.success(f"Result: {res['message']}")
        else:
            st.error(f"Error in prediction. Please check your code: {res}")