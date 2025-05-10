import streamlit as st
import pandas as pd

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("cleaned_data_small.csv")
    df['rating'] = pd.to_numeric(df['rating'], errors='coerce')
    df['cost'] = df['cost'].str.replace('₹', '').str.strip().astype(float)
    return df.dropna(subset=['rating', 'cost'])

df = load_data()

st.title("🍽️ Restaurant Recommendation App")

# Sidebar filters
st.sidebar.header("Filter Your Preferences")

city = st.sidebar.selectbox("Select City", sorted(df['city'].unique()))
cuisine = st.sidebar.text_input("Cuisine (e.g., Pizza, Chinese, Indian)")
min_rating = st.sidebar.slider("Minimum Rating", 0.0, 5.0, 3.5, 0.1)
max_cost = st.sidebar.slider("Maximum Cost (₹)", 50, 1000, 300, 50)

# Filter logic
filtered_df = df[df['city'] == city]
if cuisine:
    filtered_df = filtered_df[filtered_df['cuisine'].str.contains(cuisine, case=False, na=False)]
filtered_df = filtered_df[(filtered_df['rating'] >= min_rating) & (filtered_df['cost'] <= max_cost)]

# Results
st.subheader(f"Recommended Restaurants in {city}")
if not filtered_df.empty:
    for _, row in filtered_df.iterrows():
        st.markdown(f"### [{row['name']}]({row['link']})")
        st.write(f"📍 {row['address']}")
        st.write(f"🍽️ Cuisine: {row['cuisine']}")
        st.write(f"⭐ Rating: {row['rating']} | 💰 Cost: ₹{int(row['cost'])}")
        st.markdown("---")
else:
    st.warning("No restaurants found with your preferences.")
