
# 🎬 Movie Recommender System

A Streamlit web app that recommends movies based on content similarity.

## 🚀 Quick Start
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the app:
   ```bash
   streamlit run app.py
   ```

## 📦 Requirements
- Python 3.8+
- Libraries: `streamlit`, `pandas`, `numpy`, `scikit-learn`

  📂 Data Files
movies.pkl: Pickle file containing the movie dataset with titles and metadata.
Download here : https://drive.google.com/file/d/1NdM9oOzUxihNngjGaQsHT_42wUasqBAB/view?usp=sharing

similarity.pkl: Pickle file containing the precomputed similarity matrix used for recommendations.
Download here : https://drive.google.com/file/d/1AeWcfVrj8f9EcK1Xt79pq_mZLILh_kzZ/view?usp=sharing


## 🛠️ Project Structure
```
.
├── app.py             # Main application
├── movies.pkl         # Movie dataset
├── similarity.pkl     # Similarity matrix
└── requirements.txt   # Dependencies
```




