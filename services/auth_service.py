import streamlit as st
import firebase_admin
from firebase_admin import credentials, auth
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize Firebase Admin SDK (only once)
if not firebase_admin._apps:
    cred = credentials.Certificate(os.getenv("FIREBASE_ADMIN_CREDENTIALS_PATH")) # Replace with your service account key path
    firebase_admin.initialize_app(cred)

def sign_in_with_google():
    #This is an example, in order for Google SignIn to work, you'll need to generate the token, and verify them
    token = st.session_state.get('token')
    try:
        # Verify the ID token
        decoded_token = auth.verify_id_token(token)
        # Get user information
        uid = decoded_token['uid']
        user = auth.get_user(uid)

        # User is authenticated
        st.success(f"Signed in as {user.email}")
        st.session_state['user'] = user
        st.session_state['name'] = user.displayName
        st.session_state['logged_in'] = True
    except auth.InvalidIdTokenError as e:
        st.error(f"Authentication Error: {e}")
    except Exception as e:
        st.error(f"Error getting Firebase user: {e}")