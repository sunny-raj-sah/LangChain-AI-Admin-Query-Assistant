import streamlit as st
from data_loader import DataLoader
from access_control import AccessControl
from query_engine import QueryEngine

# Page config
st.set_page_config(
    page_title="Dumroo AI Admin Panel",
    page_icon="🎓",
    layout="wide"
)

# Initialize session state
if 'selected_admin' not in st.session_state:
    st.session_state.selected_admin = None
if 'query_history' not in st.session_state:
    st.session_state.query_history = []

# Load data
@st.cache_resource
def load_data():
    loader = DataLoader()
    return loader.load_students(), loader.load_admins()

students_df, admins_list = load_data()

# UI Layout
st.title("🎓 Dumroo AI Admin Panel")
st.markdown("### Ask questions about your students in plain English")

# Sidebar - Admin Selection
with st.sidebar:
    st.header("👤 Admin Login")
    
    admin_options = {admin['admin_name']: admin for admin in admins_list}
    selected_admin_name = st.selectbox(
        "Select Admin Profile",
        options=list(admin_options.keys())
    )
    
    st.session_state.selected_admin = admin_options[selected_admin_name]
    
    st.divider()
    st.subheader("🔐 Your Access Scope")
    
    admin_profile = st.session_state.selected_admin
    st.info(f"""
    **Grades:** {', '.join(map(str, admin_profile['allowed_grades']))}
    
    **Classes:** {', '.join(admin_profile['allowed_classes'])}
    
    **Regions:** {', '.join(admin_profile['allowed_regions'])}
    """)
    
    # Data preview
    st.divider()
    st.subheader("📊 Accessible Records")
    access_control = AccessControl(admin_profile)
    filtered_df = access_control.filter_data(students_df)
    st.metric("Total Students", len(filtered_df))

# Main content area
if st.session_state.selected_admin:
    admin_profile = st.session_state.selected_admin
    
    # Apply access control
    access_control = AccessControl(admin_profile)
    filtered_df = access_control.filter_data(students_df)
    
    # Example queries
    st.markdown("### 💡 Example Queries")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("📝 Students without homework"):
            st.session_state.current_query = "Which students haven't submitted their homework?"
    
    with col2:
        if st.button("📊 Performance data"):
            st.session_state.current_query = "Show me average quiz scores by class"
    
    with col3:
        if st.button("📅 Upcoming quizzes"):
            st.session_state.current_query = "List quizzes scheduled after November 10"
    
    # Query input
    st.divider()
    query_input = st.text_area(
        "Ask your question:",
        value=st.session_state.get('current_query', ''),
        height=100,
        placeholder="e.g., Which students in class 8A scored above 80 in quizzes?"
    )
    
    col1, col2 = st.columns([1, 5])
    with col1:
        ask_button = st.button("🔍 Ask", type="primary", use_container_width=True)
    with col2:
        if st.button("🗑️ Clear History", use_container_width=True):
            st.session_state.query_history = []
            st.rerun()
    
    # Process query
    if ask_button and query_input:
        with st.spinner("🤔 Thinking..."):
            # Initialize query engine with filtered data
            query_engine = QueryEngine(filtered_df)
            
            # Get response
            response = query_engine.query(query_input)
            
            # Save to history
            st.session_state.query_history.append({
                "query": query_input,
                "response": response
            })
            
            # Display response
            st.success("✅ Response:")
            st.markdown(response)
            
            # Show filtered dataframe if relevant
            with st.expander("📋 View Full Filtered Data"):
                st.dataframe(filtered_df, use_container_width=True)
    
    # Query history
    if st.session_state.query_history:
        st.divider()
        st.markdown("### 📜 Query History")
        
        for i, item in enumerate(reversed(st.session_state.query_history)):
            with st.expander(f"Q{len(st.session_state.query_history) - i}: {item['query'][:60]}..."):
                st.markdown(f"**Query:** {item['query']}")
                st.markdown(f"**Response:** {item['response']}")

else:
    st.warning("Please select an admin profile from the sidebar to continue.")