## step 1 Import the tools we need

import os
import streamlit as st
from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_groq import ChatGroq



## step 2 load our secret api key
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

# step 3 streamlit page

st.set_page_config(
    page_title="Zohaib Gen AI Chatbot",
    page_icon="🤖",
    layout="wide"
)

# ==============================================================================
# STEP 3.5: EXTREME ANIMATED CYBER TEAL / EMERALD GREEN UI
# ==============================================================================
import streamlit as st

st.markdown("""
<style>
    /* -------------------------------------------------------------------------
       1. FONTS IMPORT & GLOBAL ANIMATED CYBER TEAL BACKGROUND
    ------------------------------------------------------------------------- */
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700;900&family=Space+Grotesk:wght@400;600;700&display=swap');

    @keyframes gradientBG {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    html, body, [data-testid="stAppViewContainer"], .stApp {
        font-family: 'Space Grotesk', sans-serif !important;
        background: linear-gradient(-45deg, #041316, #09252a, #0d383e, #020b0d) !important;
        background-size: 400% 400% !important;
        animation: gradientBG 18s ease infinite !important;
        color: #e6fffa !important;
    }

    /* -------------------------------------------------------------------------
       2. EXTREME ANIMATED CYBER TEAL / EMERALD HEADING & TITLES
    ------------------------------------------------------------------------- */
    @keyframes glowPulse {
        0% { 
            text-shadow: 0 0 12px rgba(0, 242, 254, 0.8), 0 0 25px rgba(0, 242, 254, 0.5); 
            filter: hue-rotate(0deg); 
        }
        50% { 
            text-shadow: 0 0 30px rgba(16, 185, 129, 0.9), 0 0 50px rgba(52, 211, 153, 0.7); 
            filter: hue-rotate(25deg); 
        }
        100% { 
            text-shadow: 0 0 12px rgba(0, 242, 254, 0.8), 0 0 25px rgba(0, 242, 254, 0.5); 
            filter: hue-rotate(0deg); 
        }
    }

    h1, [data-testid="stHeader"] h1 {
        font-family: 'Orbitron', sans-serif !important;
        background: linear-gradient(90deg, #00f2fe, #10b981, #34d399, #00f2fe) !important;
        background-size: 300% auto !important;
        color: transparent !important;
        -webkit-background-clip: text !important;
        -webkit-text-fill-color: transparent !important;
        animation: glowPulse 4s infinite alternate, gradientBG 6s linear infinite !important;
        letter-spacing: 1.5px !important;
        font-weight: 900 !important;
        margin-bottom: 5px !important;
    }

    h2, h3, label {
        font-family: 'Space Grotesk', sans-serif !important;
        color: #2dd4bf !important;
        text-shadow: 0 0 10px rgba(45, 212, 191, 0.3) !important;
        font-weight: 700 !important;
    }

    /* -------------------------------------------------------------------------
       3. FLOATING CHAT MESSAGES WITH HOVER MINT / TEAL GLOW
    ------------------------------------------------------------------------- */
    @keyframes floatEffect {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-4px); box-shadow: 0 12px 30px rgba(0, 242, 254, 0.22); }
        100% { transform: translateY(0px); }
    }

    [data-testid="stChatMessage"] {
        background: rgba(9, 37, 42, 0.75) !important;
        border: 1px solid rgba(0, 242, 254, 0.3) !important;
        border-radius: 18px !important;
        backdrop-filter: blur(16px) !important;
        padding: 18px 22px !important;
        margin-bottom: 15px !important;
        animation: floatEffect 5s ease-in-out infinite !important;
        transition: all 0.3s ease-in-out !important;
    }

    [data-testid="stChatMessage"]:hover {
        border-color: #00f2fe !important;
        box-shadow: 0 0 30px rgba(0, 242, 254, 0.5) !important;
        transform: scale(1.01) translateY(-2px) !important;
    }

    /* -------------------------------------------------------------------------
       4. ANIMATED CHAT INPUT & SELECT BOXES (DEEP TEAL BACKGROUND)
    ------------------------------------------------------------------------- */
    @keyframes borderPulse {
        0% { 
            border-color: rgba(0, 242, 254, 0.7); 
            box-shadow: 0 0 15px rgba(0, 242, 254, 0.3); 
        }
        100% { 
            border-color: rgba(16, 185, 129, 0.9); 
            box-shadow: 0 0 25px rgba(16, 185, 129, 0.5); 
        }
    }

    [data-testid="stChatInput"], 
    div[data-testid="stChatInput"] > div {
        background: rgba(8, 30, 34, 0.95) !important;
        border: 2px solid rgba(0, 242, 254, 0.6) !important;
        border-radius: 22px !important;
        animation: borderPulse 3s infinite alternate !important;
        backdrop-filter: blur(12px) !important;
    }

    [data-testid="stChatInput"] textarea {
        background: transparent !important;
        color: #e6fffa !important;
        font-family: 'Space Grotesk', sans-serif !important;
    }

    [data-testid="stChatInput"] textarea::placeholder {
        color: rgba(230, 255, 250, 0.6) !important;
    }

    [data-testid="stChatInput"] button {
        background: #00f2fe !important;
        color: #041316 !important;
        border-radius: 50% !important;
    }

    div[data-baseweb="select"] > div, .stTextArea textarea {
        background: rgba(9, 37, 42, 0.85) !important;
        border: 1px solid rgba(0, 242, 254, 0.3) !important;
        border-radius: 14px !important;
        color: #e6fffa !important;
        backdrop-filter: blur(10px) !important;
    }

    /* -------------------------------------------------------------------------
       5. PULSING 3D EMERALD BUTTONS
    ------------------------------------------------------------------------- */
    .stButton > button {
        background: linear-gradient(135deg, #059669 0%, #00f2fe 100%) !important;
        color: #ffffff !important;
        border: none !important;
        border-radius: 12px !important;
        font-weight: 700 !important;
        font-size: 1rem !important;
        padding: 12px 24px !important;
        box-shadow: 0 4px 15px rgba(5, 150, 105, 0.5) !important;
        transition: all 0.3s ease-in-out !important;
    }

    .stButton > button:hover {
        transform: translateY(-3px) scale(1.02) !important;
        box-shadow: 0 0 25px rgba(0, 242, 254, 0.8) !important;
    }

    .stButton > button:active {
        transform: translateY(1px) scale(0.98) !important;
    }

    /* -------------------------------------------------------------------------
       6. SIDEBAR FROSTED TEAL ENHANCEMENT
    ------------------------------------------------------------------------- */
    [data-testid="stSidebar"] {
        background: rgba(4, 19, 22, 0.75) !important;
        backdrop-filter: blur(25px) !important;
        border-right: 1px solid rgba(0, 242, 254, 0.3) !important;
        box-shadow: 10px 0 30px rgba(0, 0, 0, 0.8) !important;
    }

    
    /* -------------------------------------------------------------------------
       7. CUSTOM NEON MINT SCROLLBAR & CLEANUP
    ------------------------------------------------------------------------- */
    ::-webkit-scrollbar { width: 10px; }
    ::-webkit-scrollbar-track { background: #020b0d; }
    ::-webkit-scrollbar-thumb { 
        background: linear-gradient(180deg, #059669, #00f2fe); 
        border-radius: 10px; 
    }
    ::-webkit-scrollbar-thumb:hover { background: #34d399; }

    header { background-color: transparent !important; }
    footer { visibility: hidden !important; }
</style>
""", unsafe_allow_html=True)



# step 4 show the app title
st.title("🤖 Zohaib Gen AI Chatbot — Karachi Urban & Real Estate Advisor")
st.caption("Specialized AI Assistant for Karachi Urban & Real Estate Intelligence — Powered by GPT-OSS")


# Step 5 check the api key 🤖

if not groq_api_key:
    st.error("Groq_api_key not available")
    st.info(
        "create .env file in project folder and add your key like this:"
    )
    st.code("GROQ_API_KEY=your_real_key_here", language="Text")
    st.stop()

# step 6 : Crate simple model option

model_options = {
    "GPT 20B TP":"openai/gpt-oss-20b",
    "GPT 120B TP": "openai/gpt-oss-120b"
}

# STEP 7 : Create a chat memory with session state

# total tokens = input ( prompt + question + history) + output

if "messages" not in st.session_state:
    st.session_state.messages = []

if "input_tokens" not in st.session_state:
    st.session_state.input_tokens = 0


if "output_tokens" not in st.session_state:
    st.session_state.output_tokens = 0


if "total_tokens" not in st.session_state:
    st.session_state.total_tokens = 0

## Step 8 : Build sidebar controls

with st.sidebar:
    st.header("💠 Chatbot Controls")

    selected_model_name = st.selectbox(
        "Choose AI Model",
        options=list(model_options.keys())
    )
    model_id = model_options[selected_model_name]


    temperature = st.slider(
        "Creativity",
        min_value=0.0,
        max_value=1.0,
        value=0.3,
        step=0.1,
        help="Low = more focused. High = more varied"
    )

    max_tokens = st.slider(
        "Maximum answer tokens",
        min_value=128,
        max_value=1024,
        value=512,
        step=128,
        help="This controls the approximate maximum response length"
    )

    st.divider()

    if st.button("🪥 Clear Chat", use_container_width=True):
        st.session_state.messages = []

        st.session_state.input_tokens = 0
        st.session_state.output_tokens = 0
        st.session_state.total_tokens = 0
        st.rerun()

# ==============================================================================
# SIDEBAR PROFESSIONAL DISCLAIMER CARD
# ==============================================================================
st.sidebar.markdown("---")

st.sidebar.markdown("""
<div style="
    background: rgba(9, 37, 42, 0.8);
    border: 1px solid rgba(0, 242, 254, 0.3);
    border-radius: 14px;
    padding: 15px;
    backdrop-filter: blur(10px);
    margin-top: 20px;
">
    <h4 style="
        color: #00f2fe;
        font-family: 'Orbitron', sans-serif;
        font-size: 0.95rem;
        font-weight: 700;
        margin-bottom: 8px;
        display: flex;
        align-items: center;
        gap: 6px;
    ">
        ⚠️ AI Information Disclaimer
    </h4>
    <p style="
        color: #c2e2dd;
        font-family: 'Space Grotesk', sans-serif;
        font-size: 0.80rem;
        line-height: 1.45;
        margin: 0;
    ">
        Responses generated by this AI model are intended strictly for <b>educational, research, and informational guidance</b>. 
        <br><br>
        • Market valuations, property rates, and locality details are estimations and may fluctuate.<br>
        • Legal, documentation, and land-lease insights should always be cross-verified with official authorities (e.g., SBCA, KDA, Sub-Registrar).
        <br><br>
        <i>Do not treat generated output as definitive legal or financial advice. Perform independent due diligence before making real estate investments.</i>
    </p>
</div>
""", unsafe_allow_html=True)        

## step 9 create the AI Model Connection

llm = ChatGroq(
    api_key = groq_api_key,
    model = model_id,
    temperature=temperature,
    max_tokens=max_tokens
)


# ==============================================================================
# SMART URBAN & REAL ESTATE ADVISOR (GPT-OSS 20B / 120B ENGINE)
# ==============================================================================
import streamlit as st
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_groq import ChatGroq

# Model Selector & Focus Area UI
c1, c2 = st.columns([1, 2])

with c1:
    selected_model_tag = st.selectbox(
        "🔰 Select AI Model:",
        ["openai/gpt-oss-120b", "openai/gpt-oss-20b"],
        key="selected_gpt_oss_model"
    )

with c2:
    focus_area = st.selectbox(
        "🌐 Choose Focus Area:",
        [
            "💎 Property Valuation & Rates",
            "⚠️ Investment Risk Analyzer",
            "📍 Locality & Amenity Insights",
            "🗺️ Legal & Buying Basics"
        ],
        key="real_estate_focus_area"
    )

# System Prompts for Urban Real Estate Domain
system_prompts = {
    "💎 Property Valuation & Rates": """
    You are an expert Karachi Real Estate Valuator. Provide comprehensive, detailed, and realistic estimated per-square-foot market rates, square-yard pricing conversions, and property valuation breakdowns for Karachi localities (e.g., DHA, Clifton, Gulshan-e-Iqbal, PECHS, Bahria Town, Scheme 33).
    """,
    
    "⚠️ Investment Risk Analyzer": """
    You are a Real Estate Risk & Growth Analyst for Karachi. Provide a thorough risk and opportunity assessment including security, capital appreciation potential, ROI timelines, builder/society reputation, legal dispute history, and infrastructure development status for Karachi real estate sectors.
    """,
    
    "📍 Locality & Amenity Insights": """
    You are an Urban Infrastructure & Spatial Analyst specializing in Karachi neighborhoods. Provide exhaustive details on water supply mechanisms (KW&SC / Tanker dependency), electricity load-shedding, gas availability, road network connectivity, monsoon flood risks, and proximity to major commercial hubs.
    """,
    
    "🗺️ Legal & Buying Basics": """
    You are a Legal & Documentation Property Consultant for Sindh/Karachi real estate. Give a step-by-step complete legal guide covering SBCA/KDA/DHA/SDA approvals, Leased vs Unleased status, Transfer Letters, Sub-Registrar Registry processes, Mutation procedures, and legal checks.
    """
}

# User Query Box
user_input = st.text_area(f"💬 Enter your question for [{focus_area}]:", placeholder="e.g. What are the legal checks before buying a plot in Gulshan-e-Iqbal?", key="re_user_input")

if st.button("🛰️ Consult AI Advisor", key="btn_consult_re"):
    if not user_input.strip():
        st.warning("⚠️ Please enter a question first.")
    elif 'groq_api_key' in globals() and groq_api_key:
        with st.spinner(f"🤖 Querying {selected_model_tag}..."):
            try:
                # Initialize ChatGroq dynamically with selected model
                active_llm = ChatGroq(
                    groq_api_key=groq_api_key,
                    model_name=selected_model_tag,
                    temperature=0.3
                )

                active_system_prompt = system_prompts[focus_area]
                
                # Query the Model
                response = active_llm.invoke([
                    SystemMessage(content=active_system_prompt),
                    HumanMessage(content=user_input)
                ])
                
                # Render Response
                st.markdown("---")
                st.markdown(f"### 📋 {focus_area} Analysis (`{selected_model_tag}`)")
                st.markdown(response.content)

            except Exception as e:
                st.error(f"❌ Error communicating with {selected_model_tag}: {e}")
    else:
        st.warning("⚠️ GROQ API Key not found. Please verify your `.env` file.")


# ==========================================
# STREAMLIT NATIVE CSV ANALYTICS (Zero Errors)
# ==========================================

import pandas as pd

with st.expander(" 📊 Advanced Data Analytics & Visualizer", expanded=False):
    st.markdown("### Upload your CSV dataset for instant analysis!")
    
    # Sirf CSV allow kiya hai taake openpyxl ka error kabhi na aaye
    uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])
    
    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
                
            st.success("File successfully loaded!")
            st.write("### 🔍 Dataset Preview", df.head())
            
            # Basic stats
            col_a, col_b, col_c = st.columns(3)
            with col_a:
                st.metric("Total Rows", df.shape[0])
            with col_b:
                st.metric("Total Columns", df.shape[1])
            with col_c:
                st.metric("Missing Values", int(df.isnull().sum().sum()))
                
            st.divider()
            st.markdown("### 📈 Built-in Streamlit Visualizer")
            
            numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
            
            if len(numeric_columns) > 0:
                chart_choice = st.selectbox("Select Chart Type", ["Line Chart", "Bar Chart", "Area Chart"])
                selected_col = st.multiselect("Select columns to plot", numeric_columns, default=numeric_columns[:2] if len(numeric_columns) >= 2 else numeric_columns)
                
                if selected_col:
                    if chart_choice == "Line Chart":
                        st.line_chart(df[selected_col])
                    elif chart_choice == "Bar Chart":
                        st.bar_chart(df[selected_col])
                    else:
                        st.area_chart(df[selected_col])
            else:
                st.warning("No numeric columns found to display charts.")
                
        except Exception as e:
            st.error(f"Error reading file: {e}")




## step 12 Display old chat messages

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        if message["role"] == "assistant" and "usage" in message:
            usage = message["usage"]
            st.caption(
                f"🔄 This response used {usage['input_tokens']} input tokens + "
                f"{usage['output_tokens']} output tokens = "
                f"{usage['total_tokens']} total tokens"
            )


# step 13 Take a new question 
# Direct Chat Input (Starter Prompts removed)
user_prompt = st.chat_input("Ask a question...")

# step 14
# 1. user message memory main save hoga
# 2. user message screen par show hoga
# 3. system instruction banaygi
# 4. old history langchain messages main convert hogi
# 5. GroqCloud ko request jaygi
# 6. AI ka answer milega
# 7. Answer screen par show hoga
# 8. Answer memory main save hoga


if user_prompt:

    # 14a : save the new user message
    st.session_state.messages.append(
        {
            "role":"user",
            "content": user_prompt,
        }
    )

    # 14 b show the user message
    with st.chat_message("user"):
        st.markdown(user_prompt)


    # 14C create the system message

    langchain_messages = [
        SystemMessage(
            content=(
                "You are Analytix camp friendly classroom assistant."
                "Explain things axccurately in simple language."
                "Use short examples wwhen helpful."
                "If you are unsure, say you are unsure instead of inventing facts."
            )
        )
    ]

    # 14 D add the full conversation history

    for message in st.session_state.messages:
        if message["role"] == "user":
            langchain_messages.append(
                HumanMessage(content=message ["content"])
            )
        else:
            langchain_messages.append(
                AIMessage(content=message["content"])
            )

    # 14 E : Ask the mpodel for an answer

    with st.chat_message("assistant"):
        with st.spinner("AI is thinking...."):
            try:
                response = llm.invoke(langchain_messages)
                answer = response.content

                usage = response.usage_metadata or {}

                input_tokens = usage.get("input_tokens",0)
                output_tokens = usage.get("output_tokens",0)
                total_tokens = usage.get("total_tokens",0)


                st.session_state.input_tokens += input_tokens
                st.session_state.output_tokens += output_tokens
                st.session_state.total_tokens += total_tokens
                st.markdown(answer)
            except Exception as error:
                st.error("Can't provide you AI Response. Sorry")
                st.caption("Kindly check your API Key or Internet or model setting.")
                st.exception(error)
                answer=""


    # 14 f. save the ai answer

    if answer:
        st.session_state.messages.append(
            {
                "role":"assistant",
                "content": answer,
                "usage": {
                    "input_tokens": input_tokens,
                    "output_tokens": output_tokens,
                    "total_tokens": total_tokens,
                },
            }
        )
        st.rerun()
       

# step 15 add how it works


with st.expander(" How does this chatbot works"):
    st.markdown(
        """

* **🏢 Karachi Real Estate & Urban Domain:** Localized AI advisor for property rates, SBCA/KDA legal checks, lease verification, and locality infrastructure (water/power) insights.
* **💬 General AI Assistant:** Powered by high-speed GPT-OSS models (20B / 120B Engine) to answer any general knowledge, coding, or complex analytical question.
* **📊 Interactive CSV Data Analytics:** Upload any custom CSV file to generate instant dataset metrics, statistical summaries, and dynamic visual charts automatically.


"""
    )


    # step 16 end of project

    st.caption(
        "Zohaib Ahmed Khan | Gen AI Chatbot & Real State Advisor "
    )


