import streamlit as st
import pandas as pd
import numpy as np

def show_academic_credit_scoring():
    st.title("🛡️ AgriLoop Credit Scoring System")
    st.markdown("---")

    # 1. GIẢI THÍCH CƠ CHẾ (HÀM TOÁN HỌC)
    st.subheader("1. Cơ chế tính điểm (Weighted Scoring Model)")
    st.latex(r'''
        Score = (Q \cdot 0.4) + (R \cdot 0.3) + (V \cdot 0.2) + (T \cdot 0.1)
    ''')
    st.info("""
    **Trong đó các trọng số (Weights) được quy định:**
    - **Q (Quality - 40%):** Chỉ số chất lượng (độ ẩm, tạp chất).
    - **R (Reliability - 30%):** Độ tin cậy (giao hàng đúng hẹn, không hủy đơn).
    - **V (Volume - 20%):** Sản lượng đóng góp cho hệ thống.
    - **T (Transparency - 10%):** Độ minh bạch trong khai báo dữ liệu.
    """)

    # 2. DỮ LIỆU THÔ (RAW DATA)
    st.subheader("2. Dữ liệu hiệu suất thực tế")
    
    raw_data = pd.DataFrame({
        'Đối tác': ['Nông dân Châu Hân', 'Hợp tác xã An', 'Tài xế Vĩnh Khang', 'Nhà máy Alpha'],
        'Chất lượng (Q)': [95, 80, 90, 85],
        'Đúng hẹn (R)': [98, 70, 95, 90],
        'Sản lượng (V)': [90, 85, 80, 95],
        'Minh bạch (T)': [100, 75, 90, 80]
    })

    # Tính toán điểm tổng kết dựa trên công thức weights
    raw_data['Điểm Tổng'] = (
        raw_data['Chất lượng (Q)'] * 0.4 + 
        raw_data['Đúng hẹn (R)'] * 0.3 + 
        raw_data['Sản lượng (V)'] * 0.2 + 
        raw_data['Minh bạch (T)'] * 0.1
    ).round(1)

    # Phân hạng dựa trên điểm (Tiering)
    def classify_tier(score):
        if score >= 90: return "💎 Platinum"
        elif score >= 80: return "🥇 Gold"
        else: return "🥈 Silver"

    raw_data['Xếp hạng (Tier)'] = raw_data['Điểm Tổng'].apply(classify_tier)

    # Hiển thị bảng kết quả chuyên nghiệp
    st.dataframe(raw_data.set_index('Đối tác').style.background_gradient(subset=['Điểm Tổng'], cmap='Greens'))

    # 3. CHI TIẾT CÁ NHÂN (DECISION SUPPORT)
    st.markdown("---")
    st.subheader("3. Truy xuất hồ sơ tín dụng cá nhân")
    selected_partner = st.selectbox("Chọn đối tác để xem chi tiết:", raw_data['Đối tác'])
    
    partner_info = raw_data[raw_data['Đối tác'] == selected_partner].iloc[0]
    
    col1, col2 = st.columns([1, 2])
    with col1:
        st.metric("Điểm Tín Nhiệm", partner_info['Điểm Tổng'])
        st.write(f"**Hạng:** {partner_info['Xếp hạng (Tier)']}")
    
    with col2:
        st.write("**Phân tích chuyên sâu:**")
        # Mô phỏng thanh tiến trình cho từng tiêu chí
        st.write(f"Chất lượng (Q): {partner_info['Chất lượng (Q)']}/100")
        st.progress(partner_info['Chất lượng (Q)'] / 100)
        
        st.write(f"Đúng hẹn (R): {partner_info['Đúng hẹn (R)']}/100")
        st.progress(partner_info['Đúng hẹn (R)'] / 100)

show_academic_credit_scoring()
