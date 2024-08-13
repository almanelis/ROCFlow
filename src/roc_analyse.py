import streamlit as st
import pandas as pd
import numpy as np
from sklearn.metrics import roc_curve, auc
import plotly.graph_objs as go

from .LEXICON import translations


def plot_interactive_roc_curve(fpr, tpr, roc_auc, thresholds, lang):
    fig = go.Figure(
        layout=dict(
            autosize=True
        )
    )

    # Add ROC curve
    fig.add_trace(go.Scatter(x=fpr, y=tpr,
                             mode='lines+markers',
                             name=f'ROC (AUC={roc_auc:.2f})',
                             hovertemplate='FPR: %{x:.3f}<br>TPR: %{y:.3f}'
                             '<br>Threshold: %{text:.3f}',
                             text=thresholds,
                             line=dict(color='red', width=2)))

    # Add diagonal line
    fig.add_trace(go.Scatter(x=[0, 1], y=[0, 1],
                             mode='lines',
                             name='Random Classifier',
                             line=dict(color='blue', width=2, dash='dash')))

    fig.update_layout(
        title='Receiver Operating Characteristic (ROC) Curve',
        xaxis_title=translations[lang]['specificity'],
        yaxis_title=translations[lang]['sensitivity'],
        legend=dict(
            orientation='v',
            yanchor="bottom",  # Разместите легенду в нижней части графика
            xanchor="center",
            x=0.6,
            y=0.2,
            bgcolor='rgba(255, 255, 255, 0.5)',
            font=dict(size=12),
            ),
        width=800,  # Increased width
        height=800,  # Increased height
    )

    fig.update_xaxes(range=[0, 1], constrain='domain')
    fig.update_yaxes(range=[0, 1], constrain='domain', scaleanchor="x",
                     scaleratio=1)

    return fig


def validate_input_data(y_true, y_pred, lang):
    unique_labels = np.unique(y_true)
    if len(unique_labels) != 2:
        st.error(f"{translations[lang]['input_error_1']}"
                 f" {len(unique_labels)}"
                 f" {translations[lang]['input_error_11']}: {unique_labels}")
        return False

    if not np.all((y_pred >= 0) & (y_pred <= 1)):
        st.error(translations[lang]['input_error_2'])
        return False

    return True


def roc_analysis(lang):
    # st.title("Interactive ROC Analysis Service")
    st.title(translations[lang]['title'])

    st.write(translations[lang]['description'])

    # File upload
    uploaded_file = st.file_uploader(translations[lang]['choose_file'],
                                     type=["csv", "xlsx"])

    if uploaded_file is not None:
        # Read the file
        try:
            if uploaded_file.name.endswith('.csv'):
                df = pd.read_csv(uploaded_file)
            else:
                df = pd.read_excel(uploaded_file)
        except Exception as e:
            st.error(f"{translations[lang]['file_reading_error']}: {str(e)}")
            return

        st.write(translations[lang]['data_preview'])
        st.write(df.head())

        # Select columns for true labels and predicted probabilities
        true_label_col = st.selectbox(translations[lang]['input_label_1'],
                                      df.columns)
        pred_prob_col = st.selectbox(translations[lang]['input_label_2'],
                                     df.columns)

        # Extract true labels and predicted probabilities
        y_true = df[true_label_col].values
        y_pred = df[pred_prob_col].values

        # Validate input data
        if not validate_input_data(y_true, y_pred, lang):
            return

        # Ensure y_true is binary (0 and 1)
        y_true_binary = np.where(y_true == y_true.min(), 0, 1)

        try:
            # Calculate ROC curve and AUC
            fpr, tpr, thresholds = roc_curve(y_true_binary, y_pred)
            roc_auc = auc(fpr, tpr)
        except Exception as e:
            st.error(f"Error calculating ROC curve: {str(e)}")
            st.error("Please ensure that your true labels are binary and "
                     "predicted probabilities are continuous values between"
                     " 0 and 1.")
            return

        # Plot interactive ROC curve
        fig = plot_interactive_roc_curve(fpr, tpr, roc_auc, thresholds, lang)
        st.plotly_chart(fig)

        # Calculate and display AUC metric
        st.subheader(f":white_check_mark: AUC: {roc_auc:.4f}")

        # Find the optimal threshold using Youden's J statistic
        j_scores = tpr - fpr
        best_threshold = thresholds[np.argmax(j_scores)]

        # Add interactive threshold selector
        st.subheader(translations[lang]['treshold_title'])
        selected_threshold = st.slider(translations[lang]['treshold_select'],
                                       min_value=0.0, max_value=1.0,
                                       value=float(best_threshold), step=0.01)

        # Find the closest threshold in our calculated thresholds
        closest_idx = np.argmin(np.abs(thresholds - selected_threshold))
        current_threshold = thresholds[closest_idx]
        current_sensitivity = tpr[closest_idx]
        current_specificity = 1 - fpr[closest_idx]

        st.write(f"{translations[lang]['current_treshold']}:"
                 f" {current_threshold:.4f}")
        st.write(f"{translations[lang]['sensitivity_treshold']}:"
                 f" {current_sensitivity:.4f}")
        st.write(f"{translations[lang]['specificity_treshold']}:"
                 f" {current_specificity:.4f}")

        # Display confusion matrix for the selected threshold
        st.subheader(translations[lang]['cmatrix_title'])
        y_pred_binary = (y_pred >= current_threshold).astype(int)
        tn = np.sum((y_true_binary == 0) & (y_pred_binary == 0))
        fp = np.sum((y_true_binary == 0) & (y_pred_binary == 1))
        fn = np.sum((y_true_binary == 1) & (y_pred_binary == 0))
        tp = np.sum((y_true_binary == 1) & (y_pred_binary == 1))

        cm_df = pd.DataFrame([[tn, fp], [fn, tp]],
                             columns=['Predicted Negative',
                                      'Predicted Positive'],
                             index=['Actual Negative', 'Actual Positive'])
        st.write(cm_df)

        # Calculate additional metrics
        accuracy = (tp + tn) / (tp + tn + fp + fn)
        precision = tp / (tp + fp) if (tp + fp) > 0 else 0
        recall = tp / (tp + fn) if (tp + fn) > 0 else 0
        f1_score = 2 * (precision * current_sensitivity) / \
                       (precision + current_sensitivity) \
            if (precision + current_sensitivity) > 0 else 0

        st.subheader(translations[lang]['additional_metrics'])
        st.write(f":one:**Accuracy**: {accuracy:.4f}")
        st.write(f":two:**Precision**: {precision:.4f}")
        st.write(f":three:**Recall**: {recall:.4f}")
        st.write(f":four: **F1 Score**: {f1_score:.4f}")

        # Visualize confusion matrix
        st.subheader(translations[lang]['cmatrix_visualization'])
        fig_cm = go.Figure(data=go.Heatmap(
                    z=cm_df.values,
                    x=cm_df.columns,
                    y=cm_df.index,
                    hoverongaps=False,
                    texttemplate="%{z}",
                    colorscale="darkmint"))

        fig_cm.update_layout(
            title="Confusion Matrix Heatmap",
            xaxis_title="Predicted",
            yaxis_title="Actual",
            width=600,
            height=500
        )

        st.plotly_chart(fig_cm)
