import streamlit as st
import pandas as pd

st.title("Electrical Ticket Manager")

tab1, tab2, tab3 = st.tabs(["To-do", "Pending", "Completed"])

with tab1:

    To_do = {
        "Timestamp": ["00:00"],
        "Email": [""],
        "Name": [" "],
        "Contact": [" "],
        "Location": [" "],
        "Free Period": [" "],
        "Description": [" "],
        "Handled?": [False]
    }

    tdf = pd.DataFrame(To_do)


    # Configure columns (optional)
    column_config = {
        "Timestamp": st.column_config.TextColumn("Task", help="Time entered"),
        "Email": st.column_config.TextColumn("Email", help="Contact info"),
        "Name": st.column_config.TextColumn("Name", help="(First, Last)"),
        "Contact": st.column_config.TextColumn("Contact", help="Phone Number or Extension"),
        "Location": st.column_config.TextColumn("Location", help="Locations"),
        "Free Period": st.column_config.TextColumn("Free Period", help=""),
        "Description": st.column_config.TextColumn("Description", help="Description of Work"),
        "selected": st.column_config.CheckboxColumn(
                label="Select",
                help="Check to eliminate this to pending",
                default=False,
        )
    }

    edited_df = st.data_editor(
        tdf,
        column_config=column_config,
        hide_index=True,
        num_rows="dynamic"  # Allows adding/removing rows
        )

with tab2:

    Pending = {
        "Timestamp": ["00:00"],
        "Name": [" "],
        "Location": [" "],
        "Group": [" "],
        "Description": [" "],
        "Time sent out": [" "],
    }

    pdf = pd.DataFrame(Pending)


    # Configure columns (optional)
    column_config = {
        "Timestamp": st.column_config.TextColumn("Timestamp", help="Time entered"),
        "Name": st.column_config.TextColumn("Name", help="(First, Last)"),
        "Location": st.column_config.TextColumn("Location", help="Locations"),
        "Group": st.column_config.TextColumn("Group", help=""),
        "Description": st.column_config.TextColumn("Description", help="Description of Work"),
        "Time Out": st.column_config.TextColumn("Time out", help="Time group left"),
    }


    edited_df = st.data_editor(
        tdf,
        column_config=column_config,
        hide_index=True,
        num_rows="dynamic"  # Allows adding/removing rows
        )

with tab3:

    Completed = {
        "Timestamp": ["00:00"],
        "Email": ["@worcesterschools.net"],
        "Name": [" "],
        "Contact": [" "],
        "Location": [" "],
        "Description": [" "],
    }

    cdf = pd.DataFrame(Completed)


    # Configure columns (optional)
    column_config = {
        "Timestamp": st.column_config.TextColumn("Task", help="Time entered"),
        "Email": st.column_config.TextColumn("Task", help="Contact info"),
        "Name": st.column_config.TextColumn("Task", help="(First, Last)"),
        "Contact": st.column_config.TextColumn("Task", help="Phone Number or Extension"),
        "Location": st.column_config.TextColumn("Task", help="Locations"),
        "Free Period": st.column_config.TextColumn("Task", help=""),
        "Description": st.column_config.TextColumn("Task", help="Description of Work"),
        "selected": st.column_config.CheckboxColumn(
                label="Select",
                help="Check to include this row in the filtered results.",
                default=False,
        )
    }
    
    edited_df = st.data_editor(
        tdf,
        column_config=column_config,
        hide_index=True,
        num_rows="dynamic"  # Allows adding/removing rows
        )