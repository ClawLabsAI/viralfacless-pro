import streamlit as st
from datetime import datetime

st.set_page_config(page_title="🎬 ViralFaceless Pro", page_icon="🎬", layout="wide")

# Session State
if 'videos' not in st.session_state: 
    st.session_state.videos = []
if 'page' not in st.session_state: 
    st.session_state.page = 'Dashboard'

# Sidebar
with st.sidebar:
    st.title("🎬 Menu")
    if st.button("📊 Dashboard"): 
        st.session_state.page = 'Dashboard'
    if st.button("🎬 Generate"): 
        st.session_state.page = 'Generate'
    if st.button("📱 Social"): 
        st.session_state.page = 'Social'
    if st.button("📚 Library"): 
        st.session_state.page = 'Library'
    st.markdown("---")
    st.metric("Videos Generated", len(st.session_state.videos))

# Dashboard Page
if st.session_state.page == 'Dashboard':
    st.title("🎬 ViralFaceless Pro")
    st.markdown("### Automated Viral Content Generation")
    
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("📹 Videos", "24")
    c2.metric("👁️ Views", "125K")
    c3.metric("💰 Revenue", "$1,250")
    c4.metric("📊 Engagement", "8.5%")
    
    st.markdown("---")
    st.info("📈 Charts will appear after you generate videos!")

# Generate Page
elif st.session_state.page == 'Generate':
    st.title("🎬 Generate Video")
    
    topic = st.text_input("Topic", placeholder="e.g., Artificial Intelligence")
    lang = st.selectbox("Language", ["English", "Spanish"])
    niche = st.selectbox("Niche", ["Facts", "Quiz", "Motivation", "History", "Tech"])
    duration = st.slider("Duration (seconds)", 30, 90, 60)
    
    col1, col2 = st.columns(2)
    with col1:
        yt = st.checkbox("YouTube", value=True)
    with col2:
        ig = st.checkbox("Instagram", value=False)
    
    if st.button("🚀 Generate Video", type="primary"):
        if topic:
            st.session_state.videos.append({
                "topic": topic, 
                "lang": lang, 
                "niche": niche,
                "duration": duration,
                "time": datetime.now().strftime("%Y-%m-%d %H:%M")
            })
            st.success(f"✅ Created: {topic}")
            st.rerun()
        else:
            st.error("⚠️ Please enter a topic!")

# Social Page
elif st.session_state.page == 'Social':
    st.title("📱 Social Media Integrations")
    
    st.markdown("### ▶️ YouTube")
    if st.button("🔗 Connect YouTube"):
        st.success("✅ YouTube connected!")
    
    st.markdown("### 📷 Instagram")
    if st.button("🔗 Connect Instagram"):
        st.success("✅ Instagram connected!")
    
    st.markdown("### 🎵 TikTok")
    if st.button("🔗 Connect TikTok"):
        st.success("✅ TikTok connected!")

# Library Page
elif st.session_state.page == 'Library':
    st.title("📚 Video Library")
    
    if st.session_state.videos:
        for v in reversed(st.session_state.videos):
            with st.expander(f"🎬 {v['topic']} - {v['time']}", expanded=False):
                st.write(f"**Language:** {v['lang']}")
                st.write(f"**Niche:** {v['niche']}")
                st.write(f"**Duration:** {v['duration']}s")
    else:
        st.info("📹 No videos yet. Go to Generate tab!")
