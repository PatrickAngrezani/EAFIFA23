import streamlit as st

st.set_page_config(page_title="Teams", page_icon="⚽", layout="wide")

df_data = st.session_state["data"]

teams = df_data["Club"].value_counts().index
team = st.sidebar.selectbox("Team", teams)

df_players_filtered = df_data[df_data["Club"] == team].set_index("Name")

st.image(df_players_filtered.iloc[0]["Club Logo"])
st.markdown(f"## {team}")

colums = ["Age", "Photo", "Flag", "Overall",
          "Value(£)", "Wage(£)", "Joined", "Height(cm.)",
          "Weight(lbs.)", "Contract Valid Until", "Release Clause(£)"]

st.dataframe(
    df_players_filtered[colums],
    column_config={
        "Overall": st.column_config.ProgressColumn("Overall", format="%d", min_value=0, max_value=99),
        "Value(£)": st.column_config.NumberColumn(),
        "Wage(£)": st.column_config.ProgressColumn("Weekly Wage", format="£%f", min_value=0, max_value=df_players_filtered["Wage(£)"].max()),
        "Photo": st.column_config.ImageColumn(),
        "Flag": st.column_config.ImageColumn("Country")
    }, height=1000
)
