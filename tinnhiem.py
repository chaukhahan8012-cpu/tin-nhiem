import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# 1. Cấu hình trang
st.set_page_config(page_title="AgriLoop Credit Engine", layout="wide")

st.title("🛡️ AgriLoop Credit Intelligence Engine")
st.write("Hệ thống mô phỏng thẩm định và xếp hạng tín nhiệm đối tác dựa trên dữ liệu chuỗi cung ứng.")

# 2. Giả lập Database đối tác
data = {
    "Nông dân Châu Hân": {"Q": 95, "R": 90, "V": 85, "F": 100, "Tier": "Platinum", "Risk": "Rất thấp"},
    "Hợp tác xã An": {"Q": 70, "R": 65, "V": 90, "F": 60, "Tier": "Silver", "Risk": "Trung bình"},
    "Tài xế Vĩnh Khang": {"Q": 85, "R": 95, "V": 75, "F": 80, "Tier": "Gold", "Risk": "Thấp"},
    "Nhà máy Alpha": {"Q": 90, "R": 85, "V": 95, "F": 90, "Tier": "Platinum", "Risk": "Rất thấp"}
}

# 3. Giao diện chọn đối tác
st.sidebar.header("🔍 Truy xuất hồ sơ")
selected_name = st.sidebar.selectbox("Chọn đối tác để kiểm tra:", list(data.keys()))
p_info = data[selected_name]

# 4. Hiển thị Dashboard Tín nhiệm
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader(f"Hồ sơ đối tác: {selected_name}")
    # Hiển thị thẻ tín nhiệm (UI/UX kiểu Card)
    st.markdown(f"""
        <div style="background-color: #ffffff; padding: 20px; border-radius: 15px; border-left: 10px solid #1e3a8a; box-shadow: 2px 2px 10px rgba(0,0,0,0.1);">
            <h2 style="color: #1e3a8a; margin: 0;">{p_info['Tier']} Partner</h2>
            <p style="color: #64748b;">Mã định danh: AG-2026-X10</p>
            <hr>
            <p><b>Mức độ rủi ro:</b> {p_info['Risk']}</p>
            <p><b>Trạng thái:</b> Đang hoạt động</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.write("---")
    st.write("**Khuyến nghị từ hệ thống:**")
    if p_info['Tier'] == "Platinum":
        st.success("Hệ thống đề xuất: Cho phép ứng tiền trước 50% giá trị đơn hàng.")
    elif p_info['Tier'] == "Gold":
        st.info("Hệ thống đề xuất: Áp dụng mức phí vận chuyển ưu đãi loại 2.")
    else:
        st.warning("Hệ thống đề xuất: Yêu cầu kiểm định hàng hóa 100% tại điểm thu gom.")

with col2:
    st.subheader("📊 Ma trận năng lực (Ability Matrix)")
    
    # Vẽ biểu đồ Radar bằng Plotly
    categories = ['Chất lượng (Q)', 'Đúng hẹn (R)', 'Sản lượng (V)', 'Tài chính (F)']
    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
        r=[p_info['Q'], p_info['R'], p_info['V'], p_info['F']],
        theta=categories,
        fill='toself',
        name=selected_name,
        line_color='#1e3a8a'
    ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(visible=True, range=[0, 100])
        ),
        showlegend=False
    )
    st.plotly_chart(fig, use_container_width=True)

# 5. Phân tích học thuật (Academic Insight)
st.markdown("---")
with st.expander("📚 Xem cơ chế phân tích học thuật (Model Mechanism)"):
    st.write("""
    Hệ thống sử dụng mô hình **Multi-Criteria Decision Analysis (MCDA)** kết hợp với lịch sử giao dịch thực tế để mô phỏng năng lực đối tác:
    - **Quality Index (Q):** Phân tích từ dữ liệu kiểm định độ ẩm/tạp chất.
    - **Reliability Index (R):** Đánh giá dựa trên độ lệch thời gian thực tế so với cam kết (Lead-time variance).
    - **Volume Consistency (V):** Khả năng duy trì nguồn cung ổn định theo quý.
    - **Financial Health (F):** Tốc độ xoay vòng vốn và lịch sử thanh toán giữa các bên.
    """)
