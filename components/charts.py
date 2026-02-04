import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

def create_activity_chart():
    """Create weekly activity chart"""
    data = pd.DataFrame({
        'Day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
        'Speaking': [25, 30, 20, 35, 40, 25, 30],
        'Listening': [15, 20, 25, 15, 20, 30, 25],
        'Vocabulary': [10, 15, 10, 20, 15, 10, 15],
        'Grammar': [5, 10, 15, 10, 5, 20, 10]
    })
    
    fig = go.Figure(data=[
        go.Bar(name='Speaking', x=data['Day'], y=data['Speaking'], marker_color='#667eea'),
        go.Bar(name='Listening', x=data['Day'], y=data['Listening'], marker_color='#4facfe'),
        go.Bar(name='Vocabulary', x=data['Day'], y=data['Vocabulary'], marker_color='#43e97b'),
        go.Bar(name='Grammar', x=data['Day'], y=data['Grammar'], marker_color='#fa709a')
    ])
    
    fig.update_layout(
        barmode='stack',
        height=300,
        margin=dict(l=10, r=10, t=30, b=10),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    
    return fig

def create_skill_radar():
    """Create skill radar chart"""
    categories = ['Speaking', 'Listening', 'Vocabulary', 'Grammar', 'Pronunciation', 'Fluency']
    values = [85, 78, 92, 76, 82, 88]
    
    fig = go.Figure(data=go.Scatterpolar(
        r=values,
        theta=categories,
        fill='toself',
        fillcolor='rgba(102, 126, 234, 0.2)',
        line_color='#667eea'
    ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100]
            )),
        showlegend=False,
        height=300,
        margin=dict(l=10, r=10, t=30, b=10)
    )
    
    return fig

def create_progress_timeline():
    """Create progress timeline"""
    data = pd.DataFrame({
        'Date': pd.date_range('2024-01-01', periods=30, freq='D'),
        'Score': [50 + i*2 + (i%3)*5 for i in range(30)]
    })
    
    fig = px.line(data, x='Date', y='Score', 
                  title="Daily Assessment Scores",
                  line_shape='spline')
    
    fig.update_traces(line_color='#667eea', line_width=3)
    fig.update_layout(height=250, margin=dict(l=10, r=10, t=30, b=10))
    
    return fig