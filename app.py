import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Initialize Dash App
app = dash.Dash(__name__, suppress_callback_exceptions=True)
app.title = "Sovereign Gaza - Unified System Engine"

# ---------------------------------------------------------
# DATA SETS FOR TAB 2 (Sovereign Gaza Framework)
# ---------------------------------------------------------
pipeline_data = {
    "Humanitarian Sector": [
        "Clean Water Tankers & Solar Desalination",
        "High-Energy Food Rations & Wheat Grain",
        "Trauma Kits & Essential Surgery Supplies",
        "Mobile Health Units & Field Hospitals",
        "Infant Nutrition & Medical Formula"
    ],
    "Stock Level (%)": [88, 92, 85, 90, 86],
    "Status": [
        "ACTIVE DISTRIBUTION", 
        "ACTIVE DISTRIBUTION", 
        "PRIORITY DISPATCH", 
        "DEPLOYED ON SITE", 
        "ACTIVE DISTRIBUTION"
    ]
}
df_pipeline = pd.DataFrame(pipeline_data)

# ---------------------------------------------------------
# MAIN LAYOUT WITH TABS
# ---------------------------------------------------------
app.layout = html.Div(style={
    'backgroundColor': '#090d16',
    'color': '#f8fafc',
    'fontFamily': 'Segoe UI, Arial, sans-serif',
    'padding': '20px'
}, children=[

    # Header
    html.Div([
        html.H1("🇶🇦 SOVEREIGN GAZA & HPC TELEMETRY SYSTEM", style={'color': '#ffffff', 'margin': '0', 'fontWeight': 'bold', 'display': 'inline-block'}),
        html.P("Unified Multi-Module Digital Twin & Monitoring Core", style={'color': '#94a3b8', 'marginTop': '5px', 'fontSize': '14px'})
    ], style={'borderBottom': '1px solid #1e293b', 'paddingBottom': '15px'}),

    # Navigation Tabs
    dcc.Tabs(id="system-tabs", value="sovereign-gaza-tab", children=[
        dcc.Tab(label="🌐 Sovereign Gaza Framework", value="sovereign-gaza-tab", 
                style={'backgroundColor': '#1e293b', 'color': '#cbd5e1'}, 
                selected_style={'backgroundColor': '#0284c7', 'color': '#ffffff', 'fontWeight': 'bold'}),
        dcc.Tab(label="⚡ System Telemetry Engine (Previous App)", value="previous-app-tab", 
                style={'backgroundColor': '#1e293b', 'color': '#cbd5e1'}, 
                selected_style={'backgroundColor': '#0284c7', 'color': '#ffffff', 'fontWeight': 'bold'}),
    ], style={'marginTop': '20px'}),

    # Tab Content Container
    html.Div(id="tab-content", style={'marginTop': '20px'})
])


# ---------------------------------------------------------
# TAB RENDERING CALLBACK
# ---------------------------------------------------------
@app.callback(
    Output("tab-content", "children"),
    Input("system-tabs", "value")
)
def render_tab_content(tab_name):
    if tab_name == "sovereign-gaza-tab":
        return html.Div([
            # Leadership Board
            html.Div([
                html.H3("👥 LEADERSHIP BOARD", style={'color': '#f8fafc', 'marginBottom': '15px', 'fontSize': '16px'}),
                html.Div([
                    html.Div([
                        html.H4("HH Sheikh Tamim Sir", style={'color': '#38bdf8', 'margin': '0'}),
                        html.P("Strategic Director", style={'color': '#cbd5e1', 'fontSize': '13px', 'margin': '5px 0 0 0'})
                    ], style={'backgroundColor': '#131b2e', 'padding': '15px', 'borderRadius': '6px', 'width': '30%', 'borderLeft': '4px solid #38bdf8'}),

                    html.Div([
                        html.H4("Father Amir Sheikh Hamad (R.A.)", style={'color': '#fbbf24', 'margin': '0'}),
                        html.P("Foundational Visionary", style={'color': '#cbd5e1', 'fontSize': '13px', 'margin': '5px 0 0 0'})
                    ], style={'backgroundColor': '#131b2e', 'padding': '15px', 'borderRadius': '6px', 'width': '30%', 'borderLeft': '4px solid #fbbf24'}),

                    html.Div([
                        html.H4("Abdul Majeed", style={'color': '#34d399', 'margin': '0'}),
                        html.P("Technical Architect", style={'color': '#cbd5e1', 'fontSize': '13px', 'margin': '5px 0 0 0'})
                    ], style={'backgroundColor': '#131b2e', 'padding': '15px', 'borderRadius': '6px', 'width': '30%', 'borderLeft': '4px solid #34d399'}),
                ], style={'display': 'flex', 'justify': 'space-between'})
            ]),

            # Status Banner
            html.Div([
                html.Span("✔ SYSTEM STATUS: ", style={'fontWeight': 'bold', 'color': '#34d399'}),
                html.Span("OPERATIONAL & READY FOR PHASE 2 EXPANSION", style={'fontWeight': 'bold', 'color': '#ffffff'})
            ], style={'backgroundColor': '#064e3b', 'padding': '12px', 'borderRadius': '6px', 'marginTop': '20px', 'textAlign': 'center', 'border': '1px solid #10b981'}),

            # Main Grid
            html.Div([
                # Left Column
                html.Div([
                    html.H3("🚚 GAZA PHASE 1: EMERGENCY RELIEF PIPELINE STATUS", style={'color': '#38bdf8', 'fontSize': '16px'}),
                    dcc.Graph(
                        figure=px.bar(
                            df_pipeline,
                            x="Stock Level (%)",
                            y="Humanitarian Sector",
                            color="Status",
                            orientation='h',
                            template="plotly_dark",
                            color_discrete_map={
                                "ACTIVE DISTRIBUTION": "#34d399",
                                "PRIORITY DISPATCH": "#fbbf24",
                                "DEPLOYED ON SITE": "#38bdf8"
                            }
                        ).update_layout(
                            paper_bgcolor='#131b2e',
                            plot_bgcolor='#131b2e',
                            margin=dict(l=10, r=10, t=10, b=10),
                            font=dict(color='#f8fafc')
                        )
                    )
                ], style={'backgroundColor': '#131b2e', 'padding': '15px', 'borderRadius': '8px', 'width': '48%'}),

                # Right Column
                html.Div([
                    html.Div([
                        html.H3("🧠 AI & TELEMETRY ENGINE", style={'color': '#38bdf8', 'fontSize': '16px', 'margin': '0', 'display': 'inline-block'}),
                        html.Span("NODE ID: GAZA-CENTRAL-AI-01 [ONLINE]", style={'float': 'right', 'color': '#34d399', 'fontSize': '12px', 'fontWeight': 'bold'})
                    ]),
                    html.Hr(style={'borderColor': '#1e293b', 'margin': '10px 0'}),

                    html.Div([
                        # Card 1
                        html.Div([
                            html.H5("1. RESOURCE DEMAND SENSING", style={'color': '#fbbf24', 'margin': '0 0 10px 0'}),
                            html.P("💧 Water: 15,000.00 m³", style={'margin': '3px 0', 'fontSize': '13px'}),
                            html.P("🍲 Food Rations: 100,000", style={'margin': '3px 0', 'fontSize': '13px'}),
                            html.P("🏥 Medical Kits: 250.00", style={'margin': '3px 0', 'fontSize': '13px'}),
                        ], style={'backgroundColor': '#090d16', 'padding': '12px', 'borderRadius': '6px', 'width': '30%'}),

                        # Card 2
                        html.Div([
                            html.H5("2. MICRO-GRID BALANCER", style={'color': '#38bdf8', 'margin': '0 0 10px 0'}),
                            html.P("⚡ Solar Input: 500 kW", style={'margin': '3px 0', 'fontSize': '13px'}),
                            html.P("🔋 Battery: 60%", style={'margin': '3px 0', 'fontSize': '13px'}),
                            html.P("🏥 Hospitals: 200.00 kW", style={'margin': '3px 0', 'fontSize': '12px', 'color': '#34d399'}),
                        ], style={'backgroundColor': '#090d16', 'padding': '12px', 'borderRadius': '6px', 'width': '30%'}),

                        # Card 3
                        html.Div([
                            html.H5("3. MEDICAL TRIAGE AI", style={'color': '#f43f5e', 'margin': '0 0 10px 0'}),
                            html.P("💓 Heart Rate: 120 bpm", style={'margin': '3px 0', 'fontSize': '13px'}),
                            html.P("🫁 SpO2: 92%", style={'margin': '3px 0', 'fontSize': '13px'}),
                            html.Div("TRIAGE: YELLOW", style={'backgroundColor': '#854d0e', 'color': '#fef08a', 'padding': '4px', 'borderRadius': '4px', 'textAlign': 'center', 'fontSize': '11px', 'marginTop': '6px'})
                        ], style={'backgroundColor': '#090d16', 'padding': '12px', 'borderRadius': '6px', 'width': '30%'}),
                    ], style={'display': 'flex', 'justify': 'space-between', 'marginTop': '15px'})

                ], style={'backgroundColor': '#131b2e', 'padding': '15px', 'borderRadius': '8px', 'width': '48%'})
            ], style={'display': 'flex', 'justify': 'space-between', 'marginTop': '20px'})
        ])

    elif tab_name == "previous-app-tab":
        return html.Div([
            html.H3("⚡ PREVIOUS TELEMETRY MODULES", style={'color': '#38bdf8'}),
            html.P("এখানে আপনার পূর্বের app.py-এর গ্রাফ এবং অন্যান্য কম্পোনেন্টগুলো বসিয়ে নিন।"),
            # আগের app.py-এর কোড / layout কম্পোনেন্টগুলো এখানে যুক্ত হবে
        ], style={'backgroundColor': '#131b2e', 'padding': '20px', 'borderRadius': '8px'})


# ---------------------------------------------------------
# RUN SERVER
# ---------------------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=True, port=8050)