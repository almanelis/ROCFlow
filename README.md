# [:sparkles: ROCFlow](https://rocflow.streamlit.app/)
## :chart_with_upwards_trend: WEB service for ROC analysis based on Streamlit framework
![Static Badge](https://img.shields.io/badge/python-3.12-green)
![Static Badge](https://img.shields.io/badge/Streamlit-1.36-blue)
![Static Badge](https://img.shields.io/badge/scipy-1.14-blue)
![Static Badge](https://img.shields.io/badge/plotly-5.22-blue)

This application will allow you to create an interactive graph with an ROC curve and calculate AUC. You can also choose a Threshold value to see how it affects the model's performance. A beautiful Error Matrix will be generated, and accuracy, precision, recall, and F1 score will be calculated. You can experiment with different thresholds to find the optimal balance between sensitivity and specificity for your specific use case.

## Getting Started
1) Clone the repository.
   ```
   git clone git@github.com:almanelis/ROCFlow.git
   ```
2) Create a virtual environment and install the required packages.
   ```
   python -m venv venv
   source venv/Scripts/activate
   pip install -r requirements.txt
   ```
3) Launch the app.
   ```
   streamlit run app.py
   ```
