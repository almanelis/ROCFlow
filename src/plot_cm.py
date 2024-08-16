import streamlit as st
import plotly.graph_objs as go


def plot_cm(cm_df, colorscale):
    fig_cm = go.Figure(data=go.Heatmap(
                        z=cm_df.values,
                        x=cm_df.columns,
                        y=cm_df.index,
                        hoverongaps=False,
                        texttemplate="%{z}",
                        colorscale=colorscale))

    fig_cm.update_layout(
        title="Confusion Matrix Heatmap",
        xaxis_title="Predicted",
        yaxis_title="Actual",
        width=600,
        height=500
    )

    st.plotly_chart(fig_cm)
