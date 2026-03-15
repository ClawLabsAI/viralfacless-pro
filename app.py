import streamlit as st
import plotly.graph_objects as go
from datetime import datetime, timedelta

st.set_page_config(page_title="🎬 ViralFaceless Pro", page_icon="🎬", layout="wide")

# Simple CSS
st.markdown("""
    <style>
    .main-header { text-align: center; font-size: 3rem; color: #6366f1; }
    .metric-card { background: #1e293b; padding: 20px; border-radius: 15px; text-align: center; }
    </style>
""", unsafe_allow_html=True)

# Session State
if 'videos' not in st.session_state: st.session_state.videos = []
if 'page' not in st.session_state: st.session_state.page = 'Dashboard'

# Sidebar
with st.sidebar:
    st.title("🎬 Menu")
    if st.button("📊 Dashboard"): st.session_state.page = 'Dashboard'
    if st.button("🎬 Generate"): st.session_state.page = 'Generate'
    if st.button("📱 Social"): st.session_state.page = 'Social'
    if st.button("📚 Library"): st.session_state.page = 'Library'
    st.markdown("---")
    st.metric("Videos", len(st.session_state.videos))

# Pages
if st.session_state.page == 'Dashboard':
    st.markdown('<h1 class="main-header">🎬 ViralFaceless Pro</h1>', unsafe_allow_html=True)
    c1, c2, c3, c4 = st.columns(4)
    c1.markdown('<div class="metric-card"><h2>24</h2><p>Videos</p></div>', unsafe_allow_html=True)
    c2.markdown('<div class="metric-card"><h2>125K</h2><p>Views</p></div>', unsafe_allow_html=True)
    c3.markdown('<div class="metric-card"><h2>$1,250</h2><p>Revenue</p></div>', unsafe_allow_html=True)
    c4.markdown('<div class="metric-card"><h2>8.5%</h2><p>Engagement</p></div>', unsafe_allow_html=True)
    
    st.markdown("### 📈 Trends")
    dates = [(datetime.now() - timedelta(days=i)).strftime('%Y-%m-%d') for i in range(30, 0, -1)]
    views = [1000 + i*50 for i in range(30)]
    fig = go.Figure(go.Scatter(x=dates, y=views, fill='tozeroy', line=dict(color='#6366f1')))
    fig.update_layout(template='plotly_dark', height=400)
    st.plotly_chart(fig, use_container_width=True)

elif st.session_state.page == 'Generate':
    st.title("🎬 Generate Video")
    topic = st.text_input("Topic")
    lang = st.selectbox("Language", ["English", "Spanish"])
    if st.button("🚀 Generate"):
        if topic:
            st.session_state.videos.append({"topic": topic, "lang": lang, "time": datetime.now()})
            st.success(f"✅ Created: {topic}")
            st.rerun()
        else:
            st.error("Enter a topic!")

elif st.session_state.page == 'Social':
    st.title("📱 Social Media")
    st.button("🔗 Connect YouTube")
    st.button("🔗 Connect Instagram")
    st.button("🔗 Connect TikTok")

elif st.session_state.page == 'Library':
    st.title("📚 Library")
    if st.session_state.videos:
        for v in st.session_state.videos[::-1]:
            st.write(f"🎬 {v['topic']} ({v['lang']}) - {v['time']}")
    else:
        st.info("No videos yet.")
