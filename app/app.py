
import streamlit as st

# Page configuration
st.set_page_config(
    page_title="AbroadMate",
    page_icon="🌍",
    layout="wide"
)

# Main heading
st.title("🌍 AbroadMate")

st.subheader("Your journey from Bangladesh to the world.")

st.write(
    """
    AbroadMate helps Bangladeshi students explore
    international universities, scholarships,
    tuition fees and study-abroad opportunities.
    """
)

st.divider()

# Dashboard metrics
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Target Countries", "6")

with col2:
    st.metric("Universities", "Coming Soon")

with col3:
    st.metric("Scholarships", "Coming Soon")

st.divider()

# Explore section
st.header("Explore AbroadMate")

option = st.selectbox(
    "What would you like to explore?",
    [
        "Select an option",
        "Country Explorer",
        "University Finder",
        "Scholarship Finder",
        "Budget Calculator"
    ]
)

if option != "Select an option":
    st.info(f"{option} will be available soon!")

st.divider()

st.caption("AbroadMate | Built for Bangladeshi students 🇧🇩")
