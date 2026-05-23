import streamlit as st

# PAGE SETTINGS

st.set_page_config(
    page_title="SkinSense AI",
    page_icon="✨",
    layout="centered"
)

# CUSTOM CSS

st.markdown("""
<style>

body {
    background-color: #0f1117;
}

.stApp {
    background: linear-gradient(to bottom right, #1e1e2f, #121212);
    color: white;
}

h1 {
    color: #ff4b91;
    text-align: center;
}

.stButton>button {
    background-color: #ff4b91;
    color: white;
    border-radius: 12px;
    height: 3em;
    width: 100%;
    font-size: 18px;
    border: none;
}

.stButton>button:hover {
    background-color: #ff75a0;
    color: white;
}

[data-testid="stMarkdownContainer"] {
    font-size: 16px;
}

</style>
""", unsafe_allow_html=True)

# TITLE

st.title("✨ SkinSense AI")
st.write("Your AI-powered skincare recommendation assistant")

# SIDEBAR

st.sidebar.title("🌸 SkinSense AI")

page = st.sidebar.radio(
    "Navigate",
    [
        "Skin Analysis",
        "Skincare Tips",
        "About App"
    ]
)

# SKIN ANALYSIS PAGE

if page == "Skin Analysis":

    # USER INPUTS

    name = st.text_input("Enter your name")

    age = st.number_input(
        "Enter your age",
        min_value=10,
        max_value=60
    )

    skin_type = st.selectbox(
        "Select your skin type",
        ["Oily", "Dry", "Combination", "Sensitive", "Normal"]
    )

    concerns = st.multiselect(
        "Select your skin concerns",
        [
            "Acne",
            "Pigmentation",
            "Dryness",
            "Dullness",
            "Large Pores",
            "Redness",
            "Wrinkles",
            "Sensitive Skin"
        ]
    )

    experience = st.selectbox(
        "Select your skincare experience level",
        ["Beginner", "Intermediate", "Advanced"]
    )

    # ANALYZE BUTTON

    if st.button("Analyze My Skin"):

        st.success("Skin Analysis Completed")

        # USER PROFILE

        st.subheader("👤 User Profile")

        st.write(f"Name: {name}")
        st.write(f"Age: {age}")
        st.write(f"Skin Type: {skin_type}")
        st.write(f"Concerns: {concerns}")
        st.write(f"Experience Level: {experience}")

        # RECOMMENDATIONS

        st.subheader("🧪 Recommended Ingredients")

        recommendations = []

        # ACNE

        if "Acne" in concerns:

            if experience == "Beginner":

                recommendations.append({
                    "ingredient": "Niacinamide",
                    "reason": "Controls oil and helps reduce acne marks",
                    "usage": "AM / PM",
                    "warning": "Start slowly and patch test before regular use"
                })

                recommendations.append({
                    "ingredient": "Tea Tree Extract",
                    "reason": "Helps reduce acne-causing bacteria",
                    "usage": "PM",
                    "warning": "Avoid overuse to prevent skin dryness"
                })

            elif experience == "Intermediate":

                recommendations.append({
                    "ingredient": "Salicylic Acid",
                    "reason": "Unclogs pores and treats acne",
                    "usage": "PM",
                    "warning": "Use sunscreen during daytime"
                })

                recommendations.append({
                    "ingredient": "Niacinamide",
                    "reason": "Helps control excess oil",
                    "usage": "AM",
                    "warning": "Use consistently for best results"
                })

            else:

                recommendations.append({
                    "ingredient": "Benzoyl Peroxide",
                    "reason": "Targets severe acne and bacteria",
                    "usage": "PM",
                    "warning": "Can cause dryness and irritation if overused"
                })

                recommendations.append({
                    "ingredient": "Salicylic Acid",
                    "reason": "Deep exfoliation for acne-prone skin",
                    "usage": "PM",
                    "warning": "Always apply sunscreen while using exfoliants"
                })

        # PIGMENTATION

        if "Pigmentation" in concerns:

            if experience == "Beginner":

                recommendations.append({
                    "ingredient": "Vitamin C",
                    "reason": "Brightens skin and reduces pigmentation",
                    "usage": "AM",
                    "warning": "Store away from direct sunlight"
                })

            else:

                recommendations.append({
                    "ingredient": "Alpha Arbutin",
                    "reason": "Helps fade dark spots and pigmentation",
                    "usage": "PM",
                    "warning": "Results take time, use consistently"
                })

                recommendations.append({
                    "ingredient": "Vitamin C",
                    "reason": "Improves skin brightness",
                    "usage": "AM",
                    "warning": "Use sunscreen for better protection"
                })

        # DRYNESS

        if "Dryness" in concerns:

            recommendations.append({
                "ingredient": "Hyaluronic Acid",
                "reason": "Provides deep hydration to the skin",
                "usage": "AM / PM",
                "warning": "Apply on slightly damp skin for better hydration"
            })

            recommendations.append({
                "ingredient": "Ceramides",
                "reason": "Strengthens the skin barrier",
                "usage": "PM",
                "warning": "Works best when used regularly"
            })

        # DULLNESS

        if "Dullness" in concerns:

            recommendations.append({
                "ingredient": "Vitamin C",
                "reason": "Boosts glow and improves skin radiance",
                "usage": "AM",
                "warning": "Use sunscreen to maintain brightening effects"
            })

        # LARGE PORES

        if "Large Pores" in concerns:

            recommendations.append({
                "ingredient": "Niacinamide",
                "reason": "Helps minimize the appearance of pores",
                "usage": "AM / PM",
                "warning": "Visible improvements require consistent usage"
            })

        # REDNESS

        if "Redness" in concerns:

            recommendations.append({
                "ingredient": "Centella Asiatica",
                "reason": "Calms irritation and reduces redness",
                "usage": "AM / PM",
                "warning": "Gentle ingredient suitable for sensitive skin"
            })

        # WRINKLES

        if "Wrinkles" in concerns:

            if age >= 20:

                if experience == "Advanced":

                    recommendations.append({
                        "ingredient": "Retinol",
                        "reason": "Improves wrinkles and boosts collagen",
                        "usage": "PM",
                        "warning": "Use sunscreen daily and start slowly"
                    })

                else:

                    recommendations.append({
                        "ingredient": "Peptides",
                        "reason": "Supports skin elasticity and firmness",
                        "usage": "AM / PM",
                        "warning": "Best used consistently for long-term results"
                    })

        # SENSITIVE SKIN

        if "Sensitive Skin" in concerns:

            recommendations.append({
                "ingredient": "Ceramides",
                "reason": "Protects and repairs sensitive skin barrier",
                "usage": "AM / PM",
                "warning": "Avoid mixing with harsh exfoliants"
            })

            recommendations.append({
                "ingredient": "Panthenol",
                "reason": "Soothes irritation and hydrates skin",
                "usage": "AM / PM",
                "warning": "Very beginner-friendly ingredient"
            })

        # REMOVE DUPLICATES

        unique_recommendations = []

        added_ingredients = []

        for item in recommendations:

            if item["ingredient"] not in added_ingredients:

                unique_recommendations.append(item)

                added_ingredients.append(item["ingredient"])

        # ROUTINE GENERATOR

        morning_routine = [
            "Cleanser",
            "Moisturizer",
            "Sunscreen"
        ]

        night_routine = [
            "Cleanser",
            "Moisturizer"
        ]

        for item in unique_recommendations:

            if "AM" in item["usage"]:

                morning_routine.append(item["ingredient"])

            if "PM" in item["usage"]:

                night_routine.append(item["ingredient"])

        # DISPLAY RESULTS

        if unique_recommendations:

            for item in unique_recommendations:

                st.markdown(f"""
                <div style="
                padding:20px;
                border-radius:20px;
                background: rgba(255,255,255,0.05);
                margin-bottom:20px;
                border:1px solid rgba(255,255,255,0.1);
                box-shadow: 0 8px 32px rgba(0,0,0,0.3);
                ">

                <h2 style='color:#ff4b91;'>✅ {item['ingredient']}</h2>

                <p style='font-size:17px;'>
                <b>Why this ingredient?</b><br>
                {item['reason']}
                </p>

                <p style='font-size:17px;'>
                <b>Recommended Usage:</b><br>
                {item['usage']}
                </p>

                <p style='font-size:17px; color:#ffb3c6;'>
                ⚠ {item['warning']}
                </p>

                </div>
                """, unsafe_allow_html=True)

        else:

            st.warning("No recommendations available.")

        # DISPLAY ROUTINES

        st.subheader("🌞 Morning Routine")

        for step in morning_routine:

            st.write(f"✅ {step}")

        st.subheader("🌙 Night Routine")

        for step in night_routine:

            st.write(f"✅ {step}")

# SKINCARE TIPS PAGE

elif page == "Skincare Tips":

    st.header("🌿 Daily Skincare Tips")

    st.write("""
    - Always wear sunscreen ☀️
    - Stay hydrated 💧
    - Patch test new ingredients 🧪
    - Avoid over-exfoliation 🚫
    - Be consistent with skincare ✨
    """)

# ABOUT PAGE

elif page == "About App":

    st.header("💡 About SkinSense AI")

    st.write("""
    SkinSense AI is a beginner-friendly AI skincare recommendation system.

    It analyzes:
    - Skin type
    - Skin concerns
    - Experience level
    - Age

    and provides ingredient recommendations accordingly.
    """)