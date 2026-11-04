import streamlit as st
import pandas as pd

st.title("Electrical Ticket Manager")

To_do = {
    "Task": ["Task", "Task", "Task"],
    "Difficulty": [0, 0, 0,],
    "Check off": [False, False, False]
}

df = pd.DataFrame(To_do)


# Configure columns (optional)
column_config = {
    "Task": st.column_config.TextColumn("Task", help="Enter a Task"),
    "Task": st.column_config.TextColumn("Task", help="Enter a Task"),
    "Task": st.column_config.TextColumn("Task", help="Enter a Task"),
    "Task": st.column_config.TextColumn("Task", help="Enter a Task"),
    "Task": st.column_config.TextColumn("Task", help="Enter a Task"),
    "Task": st.column_config.TextColumn("Task", help="Enter a Task"),
    "Task": st.column_config.TextColumn("Task", help="Enter a Task"),
    "selected": st.column_config.CheckboxColumn(
            label="Select",
            help="Check to include this row in the filtered results.",
            default=False,
    )
}

edited_df = st.data_editor(
    df,
    column_config=column_config,
    hide_index=True,
    num_rows="dynamic"  # Allows adding/removing rows
)