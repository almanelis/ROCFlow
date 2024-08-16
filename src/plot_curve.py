import plotly.graph_objs as go

from .LEXICON import translations


def plot_interactive_roc_curve(fpr, tpr, roc_auc, thresholds, roc_curve_color,
                               pred_prob_col, lang):
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
                             line=dict(color=roc_curve_color, width=2)))

    # Add diagonal line
    fig.add_trace(go.Scatter(x=[0, 1], y=[0, 1],
                             mode='lines',
                             name='Random Classifier',
                             line=dict(color=pred_prob_col, width=2,
                                       dash='dash')))

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
