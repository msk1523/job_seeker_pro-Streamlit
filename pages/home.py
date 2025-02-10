import streamlit as st
from services import auth_service

def app():
    st.title("Welcome to Job Seeker Pro")
    auth_service.sign_in_with_google() #Displays the sign in state