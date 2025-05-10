# 🍽️ Restaurant Recommendation System

An interactive Streamlit web application that recommends restaurants based on user preferences such as city, cuisine, rating, and cost. Built using a cleaned Swiggy dataset containing 65,000+ restaurant records across India.

---

## 🚀 Features

- ✅ User-friendly interface with dynamic filters
- 🔍 Real-time restaurant recommendations
- 🏙️ City and cuisine-based search
- ⭐ Minimum rating and 💰 maximum cost filters
- 📎 Direct links to Swiggy restaurant pages

---

## 📊 Dataset Overview

- **File:** `cleaned_data_small.csv`
- **Records:** 65,000 restaurants
- **Columns:** `id`, `name`, `city`, `rating`, `rating_count`, `cost`, `cuisine`, `lic_no`, `link`, `address`, `menu`

---

## 🧹 Data Cleaning & Preprocessing

1. **Null Handling**:
   - Dropped rows with missing or non-numeric values in `rating` and `cost`.
2. **Data Conversion**:
   - Converted `cost` from strings (₹) to float.
   - Converted `rating` from object to float using `pd.to_numeric()`.
3. **Text Normalization**:
   - Cleaned whitespaces and standardized city and cuisine names.

---

## 🧠 Recommendation Methodology

1. **User Input via Sidebar**:
   - Select city from dropdown
   - Enter preferred cuisine
   - Set minimum rating (slider)
   - Set maximum cost (slider)

2. **Filtering Logic**:
   - Filter dataset based on selected `city`.
   - Match `cuisine` using partial text match.
   - Filter numeric values (`rating`, `cost`) to meet thresholds.

3. **Output**:
   - Display recommended restaurants with:
     - Name (clickable link to Swiggy)
     - Address
     - Cuisine
     - Rating
     - Cost

---

## 📈 Key Insights

- Rating and Cost filters help users efficiently narrow down results.
- Flexible cuisine search supports broad and niche preferences.
- Handles missing or malformed data gracefully (e.g., "Too Few Ratings").

---

## 🛠️ How to Run Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/restaurant-recommendation.git
   cd restaurant-recommendation
2. pip install streamlit pandas

3. streamlit run app.py


├── app.py                  # Streamlit application code
├── cleaned_data_small.csv  # Preprocessed restaurant dataset
└── README.md               # Project documentation



# 🍽️ Restaurant Recommendation System

<p align="center">
  <img src="assets/screenshot.png" alt="App Screenshot" width="600"/>
</p>

An interactive Streamlit web application...
