import pickle
import streamlit as st


# load data 
def load_data():
    # Open the pickle file in read-binary mode and load the data
    with open('Model/data.pkl', 'rb') as f:
        loaded_data = pickle.load(f)

    print(loaded_data.columns)


# A side bar
def add_side_bar():
    st.sidebar.header('County Parameters.')


def main():
    st.set_page_config(
    page_title="Election Predictor",
    page_icon="🗳️",
    layout="wide",
    initial_sidebar_state="expanded"
    )
    
    with st.container():
        st.title('US Elections Predictor.')
        st.write("This application predicts the outcome of U.S. elections at the county level using a Random Forest Regressor model. The prediction is based on a variety of input features, including: \
                Voter turnout, Population demographics, Age distribution, Socioeconomic factors. \
                 By combining these variables, the model can provide a statistical estimate of how different factors influence electoral outcomes at the county level, offering valuable insights into voting patterns and potential election results.")

    add_side_bar()
    load_data()



if __name__ == '__main__':
    main()