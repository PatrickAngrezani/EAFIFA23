import streamlit as st

st.set_page_config(page_title="Players", page_icon="🏃‍♂️", layout="wide")

df_data = st.session_state["data"]

teams = df_data["Club"].value_counts().index
team = st.sidebar.selectbox("Team", teams)

df_players = df_data[df_data["Club"] == team]
players = df_players["Name"].value_counts().index
player = st.sidebar.selectbox("Player", players)

player_stats = df_data[df_data["Name"] == player].iloc[0]
st.image(player_stats["Photo"])
st.title(f"{player_stats['Name']}")

st.markdown(f"**Team:** {player_stats['Club']}")
st.markdown(f"**Position:** {player_stats['Position']}")

col1, col2, col3, col4 = st.columns(4)
col1.markdown(f"**Age:** {player_stats['Age']}")
col2.markdown(f"**Height:** {player_stats['Height(cm.)']/100}")
col3.markdown(f"**Weight:** {player_stats['Weight(lbs.)']* 0.453:.2f}")

st.divider()
st.subheader(f"Overall {player_stats['Overall']}")
st.progress(int(player_stats["Overall"]))

col1, col2, col3 = st.columns(3)
col1.metric(label="Market Value", value=f"£{player_stats['Value(£)']:,.2f}")
col2.metric(label="Weekly Wage", value=f"£{player_stats['Wage(£)']:,.2f}")
col3.metric(label="Resignation Penalty",
            value=f"£{player_stats['Release Clause(£)']:,.2f}")
