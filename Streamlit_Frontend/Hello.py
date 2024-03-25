import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

# Title with Icon
st.title("🍏 Welcome to Diet Recommendation System! 🥦")

# Sidebar with Icon
st.sidebar.success("👉 Select a recommendation app.")

# Main Content
st.markdown(
    """
    A diet recommendation web application using a content-based approach with Scikit-Learn, FastAPI, and Streamlit. 
    Whether you're looking to shed some pounds or just eat healthier, our system provides personalized diet recommendations tailored to your needs.
    """
)

# Additional Features Section
st.write("## 🌟 What I do Here 📊:")
st.write(
    """
    🥗 Personalized Recommendations: Discover recipes tailored to your taste preferences and dietary requirements.
    📋 Ingredient : Find ingredients for your recipes to suit your dietary restrictions or preferences.
    🥕 Nutritional Info: Access expert Nutritional info on every recipe.
    🍳 Community Recipes: Explore a vast collection of recipes shared by our vibrant community of food lovers.
    """
)

# Footer
st.markdown(
    """
    ---
    Built with ❤️
    """
)