import streamlit as st
import requests
import os

API_URL = os.getenv("API_URL")

st.title("Notes App")

def get_notes():
    response = requests.get(f"{API_URL}/notes/")
    if response.status_code == 200:
        return response.json()
    else:
        st.error("Failed to fetch notes")
        return []

def create_note(text):
    response = requests.post(f"{API_URL}/notes/", json={"text": text})
    if response.status_code == 200:
        st.success("Note added!")
    else:
        st.error("Failed to add note")

notes = get_notes()
st.subheader("Existing Notes")
for note in notes:
    st.write(f"{note['id']}: {note['text']}")

st.subheader("Add a New Note")
new_note = st.text_input("Note Text")
if st.button("Add Note"):
    if new_note:
        create_note(new_note)
    else:
        st.error("Note text cannot be empty")


