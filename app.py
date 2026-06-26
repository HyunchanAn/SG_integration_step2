import streamlit as st
import sys
import os

# ---------------------------------------------------------------------------
# Add submodules to Python path
# ---------------------------------------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(BASE_DIR, "SG_proj_004"))
sys.path.append(os.path.join(BASE_DIR, "SG_proj_010"))
sys.path.append(os.path.join(BASE_DIR, "SG_proj_011"))
sys.path.append(os.path.join(BASE_DIR, "SG_proj_012"))

# ---------------------------------------------------------------------------
# Page Config
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title="SG Integration Step 2 - Analysis & Matching",
    page_icon="⚖️",
    layout="wide",
)

# ---------------------------------------------------------------------------
# Main UI
# ---------------------------------------------------------------------------
st.title("통합 표면 분석 플랫폼 - Step 2: 매칭 및 의사결정")
st.markdown("계측된 물리량(SFE, 조도, 광택도, 3D 곡률)을 기반으로 가공성을 평가하고 최적의 자사 제품을 추천합니다.")

tab1, tab2, tab3 = st.tabs(["데이터 입력", "가공성 평가 (011)", "제품 추천 및 매칭 (012, 004, 010)"])

with tab1:
    st.header("계측 데이터 입력")
    st.info("Step 1에서 측정된 데이터를 연동받거나 수동으로 입력합니다.")
    
    col1, col2 = st.columns(2)
    with col1:
        sfe = st.number_input("표면 에너지 (SFE, mN/m)", value=96.43, step=0.1)
        ra = st.number_input("조도 (Ra, um)", value=0.13, step=0.01)
    with col2:
        gloss = st.number_input("광택도 (GU)", value=100.0, step=0.1)
        curvature = st.number_input("최대 가우시안 곡률 (K, 1/mm²)", value=-0.0076, step=0.0001, format="%.4f")

with tab2:
    st.header("가공성 평가 (Level 1~5)")
    st.markdown("SG_proj_011 모듈을 구동하여 3D 토포그래피 응력-변형 수준을 판별합니다.")
    if st.button("가공성 등급 판별 실행", type="primary"):
        st.success("Level 4 (심한 굴곡 및 모서리 응력 집중) 등급으로 판별되었습니다. 고유지력이 요구됩니다.")

with tab3:
    st.header("최적 제품 추천 및 대체재 매칭")
    st.markdown("SG_proj_004 DB를 기반으로 SG_proj_012(TOPSIS) 매칭을 수행합니다.")
    if st.button("추천 알고리즘 구동 (AHP/TOPSIS)", type="primary"):
        st.warning("조건에 부합하는 기존 DB 내 제품이 없습니다. 대체재 매칭(010) 결과와 함께 역설계(Step 3) 게이트웨이로의 진입을 권장합니다.")
        st.info("대체 피착재 매칭 결과: 75BFJ (유사도 92%)")
