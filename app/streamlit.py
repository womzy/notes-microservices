import streamlit as st
import requests
import os

# API Base URL
#API_URL =  os.getenv("API_URL", "http://fastapi-service.default.svc.cluster.local")
API_URL="http://localhost:8000"

st.title("Task Management Frontend")
st.write("To manage Uwaoma's tasks")

# Create Task
st.header("Create a New Task")
task_title = st.text_input("Task Title")
task_description = st.text_area("Task Description")
if st.button("Create Task"):
    response = requests.post(f"{API_URL}/tasks", json={
        "title": task_title,
        "description": task_description
    })
    if response.status_code == 200:
        st.success("Task created successfully!")
    else:
        st.error(f"Error: {response.json()}")

# List All Tasks
st.header("List of Tasks")
response = requests.get(f"{API_URL}/tasks")
if response.status_code == 200:
    tasks = response.json()
    for task in tasks:
        st.write(f"**{task['title']}** - {task['description']}")
        st.write(f"Completed: {task['completed']}")
        if st.button("Mark as Completed", key=f"complete-{task['title']}"):
            update_response = requests.put(f"{API_URL}/tasks/{task['id']}", json={
                "title": task["title"],
                "description": task["description"],
                "completed": True
            })
            if update_response.status_code == 200:
                st.success("Task marked as completed!")
            else:
                st.error(f"Error: {update_response.json()}")
else:
    st.error(f"Error fetching tasks: {response.json()}")

# Delete a Task
st.header("Delete a Task")
task_id_to_delete = st.text_input("Task ID to Delete")
if st.button("Delete Task"):
    delete_response = requests.delete(f"{API_URL}/tasks/{task_id_to_delete}")
    if delete_response.status_code == 200:
        st.success("Task deleted successfully!")
    else:
        st.error(f"Error: {delete_response.json()}")

