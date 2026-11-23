import pandas as pd
import streamlit as st
from pathlib import Path

# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="AbroadMate",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# HELPERS
# =========================================================

ROOT = Path(__file__).resolve().parent.parent

def read_csv(relative_path):
    path = ROOT / relative_path
    if not path.exists():
        st.error(f"Required file not found: {relative_path}")
        st.stop()
    return pd.read_csv(path)

def money(value):
    if pd.isna(value):
        return "Not available"
    return f"৳{value:,.0f}"

def get_periods(df):
    """Calculate total tuition using the number in program_duration."""
    df = df.copy()
    duration_number = pd.to_numeric(
        df["program_duration"].astype(str).str.extract(r"(\d+)")[0],
        errors="coerce"
    ).fillna(1)

    df["number_of_periods"] = duration_number
    df["total_tuition"] = pd.to_numeric(
        df["tuition_fee"], errors="coerce"
    )

    periodic = df["fee_period"].isin(
        ["Per Semester", "Per Trimester", "Per Year"]
    )
    df.loc[periodic, "total_tuition"] = (
        df.loc[periodic, "tuition_fee"] *
        df.loc[periodic, "number_of_periods"]
    )
    return df

def theme_css(mode):
    if mode == "Dark":
        colors = {
            "bg": "#0B1220",
            "surface": "#111C2E",
            "surface2": "#17243A",
            "text": "#F1F5F9",
            "muted": "#A7B4C7",
            "border": "#2A3A52",
            "accent": "#60A5FA",
            "input": "#17243A"
        }
    else:
        colors = {
            "bg": "#F4F7FB",
            "surface": "#FFFFFF",
            "surface2": "#EDF3FA",
            "text": "#172033",
            "muted": "#64748B",
            "border": "#DCE5F0",
            "accent": "#2563EB",
            "input": "#FFFFFF"
        }

    st.markdown(f"""
    <style>
    :root {{
        color-scheme: {"dark" if mode == "Dark" else "light"};
    }}

    .stApp {{
        background: {colors["bg"]};
        color: {colors["text"]};
    }}

    [data-testid="stHeader"] {{
        background: transparent;
    }}

    [data-testid="stSidebar"] {{
        background: {colors["surface"]};
        border-right: 1px solid {colors["border"]};
    }}

    [data-testid="stSidebar"] * {{
        color: {colors["text"]};
    }}

    .block-container {{
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1200px;
    }}

    h1, h2, h3, h4, p, label, li {{
        color: {colors["text"]};
    }}

    [data-testid="stCaptionContainer"],
    .stCaption {{
        color: {colors["muted"]} !important;
    }}

    [data-testid="stMetric"] {{
        background: {colors["surface"]};
        border: 1px solid {colors["border"]};
        border-radius: 14px;
        padding: 16px;
        min-width: 0;
    }}

    [data-testid="stMetricValue"] {{
        font-size: clamp(20px, 2.2vw, 30px);
        overflow-wrap: anywhere;
        word-break: break-word;
    }}

    [data-testid="stMetricLabel"] {{
        font-size: 14px;
    }}

    [data-testid="stVerticalBlockBorderWrapper"] {{
        background: {colors["surface"]};
        border-color: {colors["border"]} !important;
        border-radius: 16px;
    }}

    div[data-baseweb="select"] > div,
    div[data-baseweb="input"] > div,
    textarea {{
        background: {colors["input"]};
        border-color: {colors["border"]};
    }}

    .hero {{
        background: linear-gradient(120deg, #172554, #2563EB);
        padding: 38px;
        border-radius: 20px;
        margin-bottom: 26px;
    }}

    .hero h1 {{
        color: #FFFFFF !important;
        font-size: clamp(28px, 4vw, 42px);
        margin-bottom: 10px;
    }}

    .hero p {{
        color: #DBEAFE !important;
        font-size: 17px;
        max-width: 760px;
    }}

    .kicker {{
        color: {colors["accent"]};
        font-size: 12px;
        font-weight: 800;
        letter-spacing: 1.5px;
        margin-bottom: 6px;
    }}

    .tuition-card {{
        background: {colors["surface2"]};
        border: 1px solid {colors["border"]};
        border-radius: 14px;
        padding: 18px 20px;
        margin: 12px 0;
    }}

    .tuition-label {{
        color: {colors["muted"]};
        font-size: 14px;
        margin-bottom: 7px;
    }}

    .tuition-value {{
        color: {colors["text"]};
        font-size: clamp(23px, 3vw, 32px);
        line-height: 1.25;
        font-weight: 800;
        overflow-wrap: anywhere;
        word-break: break-word;
    }}

    .small-note {{
        color: {colors["muted"]};
        font-size: 13px;
    }}

    div.stButton > button,
    div.stLinkButton > a {{
        border-radius: 10px;
    }}
    </style>
    """, unsafe_allow_html=True)

# =========================================================
# LOAD CORE DATA
# =========================================================

countries_df = read_csv("data/raw/countries.csv")
universities_df = read_csv("data/raw/universities.csv")
programs_raw = read_csv("data/raw/programs.csv")
scholarships_df = read_csv("data/raw/scholarships.csv")

# =========================================================
# SIDEBAR NAVIGATION AND THEME
# =========================================================

with st.sidebar:
    st.title("🌍 AbroadMate")
    st.caption("Your journey from Bangladesh to the world.")
    st.divider()

    appearance = st.radio(
        "Appearance",
        ["Light", "Dark"],
        horizontal=True,
        key="appearance_mode"
    )

    st.divider()

    option = st.radio(
        "EXPLORE",
        [
            "Home",
            "Country Explorer",
            "University Finder",
            "Scholarship Finder",
            "Living Cost Explorer",
            "Budget Calculator"
        ],
        key="main_navigation"
    )

    st.divider()
    st.caption("Made for Bangladeshi students 🇧🇩")

theme_css(appearance)

# =========================================================
# HOME
# =========================================================

if option == "Home":
    st.markdown("""
    <div class="hero">
        <h1>Your Study Abroad Journey Starts Here 🌍</h1>
        <p>
            Discover international universities, explore scholarships,
            compare living expenses and plan your future abroad.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("📊 AbroadMate Overview")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Countries", countries_df["country_id"].nunique())
    c2.metric("Universities", universities_df["university_id"].nunique())
    c3.metric("Programmes", programs_raw["program_id"].nunique())
    c4.metric("Scholarships", scholarships_df["scholarship_id"].nunique())

    st.divider()
    st.subheader("Explore popular destinations")

    destination_images = {
        "Germany": "https://images.unsplash.com/photo-1467269204594-9661b134dd2b?w=900",
        "Canada": "https://images.unsplash.com/photo-1517935706615-2717063c2225?w=900",
        "Australia": "https://images.unsplash.com/photo-1506973035872-a4",
        "United Kingdom": "https://images.unsplash.com/photo-1513635269975-59663e0ac1ad?w=900",
        "Italy": "https://images.unsplash.com/photo-1516483638261-f4dbaf036963?w=900",
        "Hungary": "https://images.unsplash.com/photo-1541849546-216549ae216d?w=900"
    }
    descriptions = {
        "Germany": "Explore public universities and master's programmes.",
        "Canada": "Discover universities and postgraduate opportunities.",
        "Australia": "Explore study options and student life.",
        "United Kingdom": "Find universities and scholarship opportunities.",
        "Italy": "Discover universities and affordable study destinations.",
        "Hungary": "Explore European study opportunities."
    }

    cols = st.columns(3)
    for i, row in countries_df.iterrows():
        name = row["country_name"]
        with cols[i % 3]:
            image_url = destination_images.get(name)
            if image_url and not image_url.endswith("a4"):
                st.image(image_url, use_container_width=True)
            st.markdown(f"**{name}**")
            st.caption(descriptions.get(name, "Explore study opportunities."))
            st.write("")

    st.info("Choose a section from the sidebar to start exploring AbroadMate.")

# =========================================================
# COUNTRY EXPLORER
# =========================================================

elif option == "Country Explorer":
    st.markdown('<div class="kicker">CHOOSE YOUR DESTINATION</div>', unsafe_allow_html=True)
    st.title("🌍 Country Explorer")
    st.write("Explore the countries currently included in AbroadMate.")

    selected_country = st.selectbox(
        "Choose a country",
        sorted(countries_df["country_name"].dropna().unique())
    )
    country = countries_df[
        countries_df["country_name"] == selected_country
    ].iloc[0]

    st.subheader(selected_country)
    st.write(f"**Currency:** {country['currency_name']} ({country['currency_code']})")

    country_unis = universities_df[
        universities_df["country_id"] == country["country_id"]
    ]
    st.metric("Universities listed", len(country_unis))

    st.markdown("### Universities in this destination")
    if country_unis.empty:
        st.info("University information is not available yet.")
    else:
        for _, uni in country_unis.iterrows():
            with st.container(border=True):
                st.subheader(uni["university_name"])
                if pd.notna(uni.get("website")) and str(uni["website"]).strip():
                    st.link_button("Visit university website", uni["website"])

# =========================================================
# UNIVERSITY FINDER
# =========================================================

elif option == "University Finder":
    st.markdown('<div class="kicker">FIND YOUR NEXT CAMPUS</div>', unsafe_allow_html=True)
    st.title("🎓 University Finder")
    st.write("Browse programmes and compare published tuition fees in BDT.")

    programs = get_periods(read_csv("data/processed/abroadmate_programs.csv"))
    rates = read_csv("data/raw/exchange_rates.csv")
    df = programs.merge(rates, on="currency_code", how="left")

    df["period_tuition_bdt"] = df["tuition_fee"] * df["bdt_per_unit"]
    df["total_tuition_bdt"] = df["total_tuition"] * df["bdt_per_unit"]

    countries = ["All Countries"] + sorted(df["country_name"].dropna().unique())
    selected = st.selectbox("Filter by destination", countries)
    result = df if selected == "All Countries" else df[df["country_name"] == selected]

    st.caption(f"{len(result)} programme(s) found.")

    if result.empty:
        st.info("No programmes are listed for this destination yet.")

    for _, r in result.iterrows():
        with st.container(border=True):
            st.subheader(f"🎓 {r['university_name']}")
            st.write(f"📍 **{r['country_name']}**")
            st.divider()

            st.write(f"**Programme:** {r['program_name']}")
            st.write(f"**Degree:** {r['degree']}")
            st.write(f"**Subject:** {r['subject']}")
            st.write(f"**Duration:** {r['program_duration']}")
            st.write(
                f"**Published fee:** {r['currency_code']} "
                f"{r['tuition_fee']:,.2f} ({r['fee_period']})"
            )

            st.link_button("View official programme page", r["source_url"])

            st.markdown(
                f"""
                <div class="tuition-card">
                    <div class="tuition-label">Estimated total programme tuition</div>
                    <div class="tuition-value">{money(r['total_tuition_bdt'])}</div>
                </div>
                """,
                unsafe_allow_html=True
            )

            if r["fee_period"] in ["Per Semester", "Per Trimester", "Per Year"]:
                st.write(
                    f"**Fee {r['fee_period'].lower()}:** "
                    f"{money(r['period_tuition_bdt'])}"
                )

            if pd.notna(r["bdt_per_unit"]):
                st.caption(
                    f"Exchange rate: 1 {r['currency_code']} = "
                    f"৳{r['bdt_per_unit']:.4f} | Rate date: {r['rate_date']}"
                )

    st.caption(
        "Converted amounts are estimates based on stored exchange rates. "
        "Always verify current fees on official university websites."
    )

# =========================================================
# SCHOLARSHIP FINDER
# =========================================================

elif option == "Scholarship Finder":
    st.markdown('<div class="kicker">FUND YOUR EDUCATION</div>', unsafe_allow_html=True)
    st.title("🎓 Scholarship Finder")
    st.write("Explore scholarship opportunities for Bangladeshi students.")

    df = scholarships_df.merge(
        countries_df[["country_id", "country_name"]],
        on="country_id",
        how="left"
    )
    df["country_name"] = df["country_name"].fillna("Multiple Countries")

    all_countries = sorted(countries_df["country_name"].dropna().unique())
    choices = ["All Countries"] + all_countries + ["Multiple Countries"]
    selected = st.selectbox("Filter by destination", choices)

    if selected == "All Countries":
        result = df
    elif selected == "Multiple Countries":
        result = df[df["country_name"] == "Multiple Countries"]
    else:
        result = df[
            (df["country_name"] == selected) |
            (df["country_name"] == "Multiple Countries")
        ]

    st.caption(f"{len(result)} scholarship opportunity/opportunities found.")

    if result.empty:
        st.info("No scholarships are listed for this destination yet.")
    else:
        for _, r in result.iterrows():
            with st.container(border=True):
                st.subheader(r["scholarship_name"])
                st.write(f"🌍 **Destination:** {r['country_name']}")
                st.write(f"**Degree:** {r['degree_level']}")
                st.write(f"**Coverage:** {r['coverage']}")
                st.write(f"**Eligibility:** {r['eligibility']}")
                st.write(f"**Application deadline:** {r['application_deadline']}")
                st.link_button("Official scholarship website", r["source_url"])
                st.caption(f"Information status: {r['verification_status']}")

    st.caption("Always verify eligibility and deadlines on the official scholarship website.")

# =========================================================
# LIVING COST EXPLORER
# =========================================================

elif option == "Living Cost Explorer":
    st.markdown('<div class="kicker">PLAN YOUR MONTHLY EXPENSES</div>', unsafe_allow_html=True)
    st.title("🏙️ Living Cost Explorer")
    st.write("Compare estimated monthly living expenses in popular student cities.")

    df = read_csv("data/processed/living_costs_bdt.csv")
    cities = sorted(df["city"].dropna().unique())
    selected_city = st.selectbox("Select a city", cities)
    city = df[df["city"] == selected_city].iloc[0]

    st.subheader(f"Living costs in {selected_city}")

    expense_fields = [
        ("Accommodation", "accommodation_min", "accommodation_max"),
        ("Food", "food_min", "food_max"),
        ("Transportation", "transport_min", "transport_max"),
        ("Other expenses", "other_min", "other_max")
    ]

    cols = st.columns(2)
    for i, (label, min_col, max_col) in enumerate(expense_fields):
        with cols[i % 2]:
            with st.container(border=True):
                st.markdown(f"**{label}**")
                low = city[min_col]
                high = city[max_col]
                rate = city["bdt_per_unit"]
                st.write(f"Minimum: {money(low * rate) if pd.notna(low) and pd.notna(rate) else 'Not provided'}")
                st.write(f"Maximum: {money(high * rate) if pd.notna(high) and pd.notna(rate) else 'Not provided'}")

    st.divider()
    a, b = st.columns(2)
    with a:
        st.metric("Minimum monthly estimate", money(city["total_monthly_min_bdt"]))
    with b:
        st.metric("Maximum monthly estimate", money(city["total_monthly_max_bdt"]))

    st.subheader("Compare cities")
    min_chart = ROOT / "assets/living_cost_minimum_bdt.png"
    range_chart = ROOT / "assets/living_cost_range_bdt.png"
    if min_chart.exists():
        st.image(str(min_chart), use_container_width=True)
    if range_chart.exists():
        st.image(str(range_chart), use_container_width=True)

    st.caption("These are indicative estimates. Actual expenses depend on housing, lifestyle and location.")

# =========================================================
# BUDGET CALCULATOR
# =========================================================

elif option == "Budget Calculator":
    st.markdown('<div class="kicker">PLAN YOUR STUDY ABROAD BUDGET</div>', unsafe_allow_html=True)
    st.title("💰 Study Abroad Budget Calculator")
    st.write("Estimate tuition and living expenses in Bangladeshi Taka.")

    programs = get_periods(read_csv("data/processed/abroadmate_programs.csv"))
    rates = read_csv("data/raw/exchange_rates.csv")
    living = read_csv("data/processed/living_costs_bdt.csv")

    programs = programs.merge(rates, on="currency_code", how="left")
    programs["total_tuition_bdt"] = programs["total_tuition"] * programs["bdt_per_unit"]

    st.subheader("1. Select your programme")
    program_labels = programs.apply(
        lambda r: f"{r['program_name']} — {r['university_name']}",
        axis=1
    ).tolist()
    selected_label = st.selectbox("Programme", program_labels)
    p = programs.iloc[program_labels.index(selected_label)]

    with st.container(border=True):
        st.write(f"**University:** {p['university_name']}")
        st.write(f"**Country:** {p['country_name']}")
        st.markdown(
            f"""
            <div class="tuition-card">
                <div class="tuition-label">Estimated total tuition</div>
                <div class="tuition-value">{money(p['total_tuition_bdt'])}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.subheader("2. Select your destination city")
    available = living[
        (living["country_id"] == p["country_id"]) &
        (living["total_monthly_min_bdt"].notna())
    ]

    if available.empty:
        st.warning("Living-cost information is not available for this programme's country yet.")
    else:
        city_name = st.selectbox("City", sorted(available["city"].unique()))
        city = available[available["city"] == city_name].iloc[0]

        st.subheader("3. Enter your study duration")
        default_months = 12
        duration_text = str(p["program_duration"])
        import re
        match = re.search(r"(\d+)", duration_text)
        if match:
            n = int(match.group(1))
            if "month" in duration_text.lower():
                default_months = n
            elif "year" in duration_text.lower():
                default_months = n * 12
            elif "semester" in duration_text.lower():
                default_months = n * 6
            elif "trimester" in duration_text.lower():
                default_months = n * 4

        months = st.number_input(
            "Study duration (months)",
            min_value=1,
            max_value=120,
            value=max(1, min(default_months, 120)),
            step=1
        )

        min_monthly = city["total_monthly_min_bdt"]
        max_monthly = city["total_monthly_max_bdt"]
        total_living_min = min_monthly * months
        total_budget_min = p["total_tuition_bdt"] + total_living_min

        st.subheader("4. Your estimated budget")
        c1, c2 = st.columns(2)
        with c1:
            st.metric("Monthly living cost (minimum)", money(min_monthly))
            st.metric("Total living cost (minimum)", money(total_living_min))
        with c2:
            if pd.notna(max_monthly):
                total_living_max = max_monthly * months
                st.metric("Monthly living cost (maximum)", money(max_monthly))
                st.metric("Total living cost (maximum)", money(total_living_max))
            else:
                st.info("Maximum living-cost estimate unavailable.")

        st.divider()
        st.subheader("🎯 Total estimated study budget")
        st.markdown(
            f"""
            <div class="tuition-card">
                <div class="tuition-label">Minimum estimated budget (tuition + living)</div>
                <div class="tuition-value">{money(total_budget_min)}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

        if pd.notna(max_monthly):
            total_budget_max = p["total_tuition_bdt"] + total_living_max
            st.markdown(
                f"""
                <div class="tuition-card">
                    <div class="tuition-label">Maximum estimated budget (tuition + living)</div>
                    <div class="tuition-value">{money(total_budget_max)}</div>
                </div>
                """,
                unsafe_allow_html=True
            )

        st.caption(
            "Estimates exclude visa fees, airfare, application fees, deposits "
            "and initial settlement costs. Actual costs may vary."
        )

# =========================================================
# FOOTER
# =========================================================

st.divider()
st.caption("AbroadMate | Your journey from Bangladesh to the world. 🇧🇩")
