import streamlit as st
from engine import engine

st.set_page_config(page_title="Rulebook Contradiction Engine", page_icon="⚖️", layout="wide")

st.title("⚖️ The Rulebook That Argues With Itself")
st.caption("Deterministic multi-state regulatory retriever with exact clause citations and contradiction alerts.")

col1, col2 = st.columns([2, 1])

with col1:
    query = st.text_input(
        "Ask a regulatory question:", 
        placeholder="e.g. What is the minimum attendance required if I was hospitalized?"
    )
    
    # Pre-set buttons for quick demonstration
    st.markdown("**Quick Demos:**")
    b1 = st.button("🔴 Contradiction Demo: Hospitalization vs Attendance")
    b2 = st.button("🟢 Plain Answer Demo: Thesis Plagiarism Threshold")
    b3 = st.button("⚪ Refusal Demo: Sister's Wedding Absence")

    if b1:
        query = "What is the minimum attendance required to sit for exams if I was hospitalized?"
    elif b2:
        query = "What happens if my final year thesis has 20% plagiarism?"
    elif b3:
        query = "Can I miss an exam because of my sister's wedding?"

    if query:
        with st.spinner("Analyzing all regulatory clauses..."):
            res = engine.query(query)

        st.divider()
        if res.state == "CONTRADICTION":
            st.error(f"### ⚠️ CONTRADICTION DETECTED\n**Verdict:** {res.summary}")
        elif res.state == "ANSWER":
            st.success(f"### ✅ ANSWER\n{res.summary}")
        elif res.state == "REFUSAL":
            st.warning(f"### 🚫 REGULATORY SILENCE (REFUSAL)\n{res.summary}")

        st.metric("Confidence Score", f"{res.confidence * 100:.1f}%")

        if res.sources:
            st.subheader("📚 Verified Source Citations")
            for idx, src in enumerate(res.sources):
                with st.expander(f"Citation {idx+1}: {src.file} ({src.clause})", expanded=True):
                    st.markdown(f"> *\"{src.text}\"*")

with col2:
    st.info("### 📋 System Properties\n- **3 Deterministic States:** Answer, Refusal, Contradiction\n- **Zero Hallucination:** Rejects near-miss non-existent clauses\n- **Traceable:** Returns file + section number citations")
    st.markdown("---")
    st.markdown("### 🧪 Quick Eval Run")
    if st.button("Run Full 33-Case Benchmark"):
        with st.spinner("Running test cases..."):
            import eval_runner
            eval_runner.run_evals()
            st.success("Eval complete. Check the terminal for the full classification matrix.")