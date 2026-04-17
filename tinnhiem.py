import streamlit as st
import pandas as pd
import time

# 1. Cấu hình giao diện Dashboard
st.set_page_config(page_title="AgriLoop Enterprise Dashboard", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #f8fafc; }
    .stMetric { background-color: #ffffff; padding: 15px; border-radius: 10px; border: 1px solid #e2e8f0; }
    </style>
    """, unsafe_allow_html=True)

# 2. Sidebar Menu
st.sidebar.title("🌿 AgriLoop Hub")
st.sidebar.write("Hệ thống quản trị HUB - 2026")
menu = st.sidebar.radio("CHỨNG MINH Ý TƯỞNG:", 
    ["1. Luồng vận hành", "2. Hiệu suất kinh doanh", "3. Truy xuất & Tín nhiệm"])

# --- TAB 1: LUỒNG VẬN HÀNH (CHUYÊN NGHIỆP, KHÔNG ICON) ---
if menu == "1. Luồng vận hành":
    st.header("⚙️ Sơ đồ vận hành hệ thống AgriLoop")
    st.graphviz_chart('''
    digraph G {
        rankdir=LR;
        node [fontname="Arial", shape=box, style="filled, rounded", color="#1e3a8a", fontcolor=white];
        edge [fontname="Arial", color="#64748b", penwidth=1.5];

        A [label="Nông dân", fillcolor="#16a34a"];
        B [label="Hệ thống Trung tâm", fillcolor="#2563eb"];
        C [label="Tài xế Vận tải", fillcolor="#ea580c"];
        D [label="Nhà máy Tiêu thụ", fillcolor="#dc2626"];

        A -> B [label="Báo đơn hàng"];
        B -> C [label="Ghép chuyến tối ưu"];
        C -> D [label="Giao hàng thực tế"];
        D -> B [label="Số hóa hóa đơn"];
        B -> A [label="Thanh toán trực tiếp", style=dashed];
    }
    ''')
    st.info("Mô tả: Hệ thống tự động hóa từ lúc nông dân đăng tin đến khi nhà máy nhận hàng và trả tiền.")

# --- TAB 2: HIỆU SUẤT KINH DOANH (BIỂU ĐỒ) ---
elif menu == "2. Hiệu suất kinh doanh":
    st.header("📊 Báo cáo tăng trưởng Q1-2026")
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Tổng sản lượng", "1,520 Tấn", "+12%")
    col2.metric("Chi phí vận tải", "-15%", "Tối ưu Pooling")
    col3.metric("Tỷ lệ hài lòng", "4.8/5", "Sao uy tín")

    st.write("### Tỷ lệ cung ứng theo khu vực")
    chart_data = pd.DataFrame({
        'Tháng': ['Tháng 1', 'Tháng 2', 'Tháng 3', 'Tháng 4'],
        'Vỏ trấu': [300, 450, 400, 550],
        'Rơm rạ': [200, 250, 300, 350]
    }).set_index('Tháng')
    st.bar_chart(chart_data)

# --- TAB 3: TRUY XUẤT & TÍN NHIỆM ---
elif menu == "3. Truy xuất & Tín nhiệm":
    st.header("🆔 Mô phỏng Truy xuất & Đánh giá Tín nhiệm")
    
    tab_a, tab_b = st.tabs(["🔍 Truy xuất lô hàng", "⭐ Điểm tín nhiệm đối tác"])
    
    with tab_a:
        st.write("Dùng mã định danh để kiểm tra lịch sử hàng hóa.")
        col_q1, col_q2 = st.columns([1, 2])
        with col_q1:
            st.image("https://api.qrserver.com/v1/create-qr-code/?size=200x200&data=AgriLoop-HUB-2026", caption="Mã QR định danh lô hàng")
            scan = st.button("MÔ PHỎNG QUÉT MÃ (SCAN)")
        
        with col_q2:
            if scan:
                with st.spinner('Đang truy xuất dữ liệu...'):
                    time.sleep(1)
                    st.success("Thông tin lô hàng: AL-HUB-2026-001")
                    st.write("**Độ ẩm:** 12% | **Nhiệt độ:** 28°C")
                    st.write("**Lịch sử:** Thu gom tại Farm Hân (08:00) -> Nhập kho Alpha (16:00)")
    
    with tab_b:
        st.write("Bảng xếp hạng uy tín dựa trên lịch sử giao dịch.")
        trust_df = pd.DataFrame({
            'Đối tác': ['Nông dân Hân', 'Tài xế An', 'Nhà máy Alpha', 'Farm Bình'],
            'Điểm tín nhiệm': [98, 92, 95, 75],
            'Trạng thái': ['⭐ Bạch kim', '✅ Uy tín', '⭐ Bạch kim', '⚠️ Cần cải thiện']
        })
        st.table(trust_df)
