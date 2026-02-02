import streamlit as st
from urllib.parse import quote
from scholarly import scholarly

# Set page title
st.set_page_config(page_title="Cameron Green", layout="wide")

# Sidebar Menu
st.sidebar.title("Navigation")
# menu = st.sidebar.radio(
#     "Go to:",
#     ["Profile", "Employment History", "Education", "Publications", "Contact"],
# )

# menu = st.sidebar.selectbox(
#     "Go to:",
#     ["Profile", "Employment History", "Education", "Publications", "Contact"]
# )

if "page" not in st.session_state:
    st.session_state.page = "Profile"

if st.sidebar.button("Profile"):
    st.session_state.page = "Profile"
if st.sidebar.button("Employment History"):
    st.session_state.page = "Employment History"
if st.sidebar.button("Education"):
    st.session_state.page = "Education"
if st.sidebar.button("Work Case Studies"):
    st.session_state.page = "Work Case Studies"
if st.sidebar.button("Publications"):
    st.session_state.page = "Publications"
if st.sidebar.button("Contact"):
    st.session_state.page = "Contact"

# Use the stored state to control layout
page = st.session_state.page

# Initialize session state for pseudo-popup control
if "publications_confirmed" not in st.session_state:
    st.session_state.publications_confirmed = False

# Sections based on menu selection
if page == "Profile":
    st.title("Cameron Green")

    # Side-by-side layout with image on the left
    col1, col2 = st.columns([3, 1])  # 1:3 width ratio (adjust if needed)

    with col2:
        st.image(
            "./assets/CameronGreen_professional.jpg",
            width=300,  # width in pixels
            # height=250  # optional: set if you want to force height  # ✅ Updated parameter
        )

    with col1:
        st.write("**Geospatial Developer | Geospatial Data Scientist | R&D Engineer | GeoAI & Machine Learning**")

        st.write(
            "Experienced Geospatial Developer and Spatial Data Infrastructure (SDI) Engineer with a strong background "
            "in research, development, and applied geospatial technologies. I have worked extensively across the "
            "precision agriculture, commercial forestry, and property sectors. My expertise includes spatial data "
            "engineering, property cadastre management, and AI-based remote sensing analysis. I hold a Master’s "
            "degree in Geoinformatics from the University of Pretoria, and I’ve successfully delivered complex, "
            "data-driven geospatial solutions in both academic and commercial settings. I'm proficient in Python, "
            "AWS, and geospatial analysis tools, and currently Head of GeoAI & Machine Learning Infrastructure."
        )

elif page == "Employment History":
    st.title("Employment History")
    # 1️⃣ Job: Riskscape
    st.markdown("### **Spatial Data Infrastructure (SDI) Engineer**  \n*Riskscape, Pretoria*")
    st.markdown("<span style='font-size: 90%; color: grey;'>September 2024 – Present</span>", unsafe_allow_html=True)
    st.write("At Riskscape, I work as part of the development team focused on improving national-scale property "
             "valuation systems and maintaining accurate, up-to-date cadastral data. My role involves designing and "
             "implementing workflows for updating property cadastre information and supporting valuation processes "
             "across South Africa. I led the upgrade project of the in-house geocoder that uses fuzzy matching and "
             "natural language models to provide accurate address matching and spatial referencing. More recently, "
             "my work has expanded into the development and training of AI models capable of detecting thatch roofs "
             "and solar panels from high-resolution satellite imagery; projects that support risk profiling for "
             "insurances and infrastructure planning. I also contribute to the broader spatial data infrastructure "
             "efforts at Riskscape by helping integrate our tools and models into insurance systems to ensure "
             "interoperability and long-term scalability.")

    # 2️⃣ Job: Swift Geospatial (Geospatial Developer)
    st.markdown("### **Geospatial Developer**  \n*Swift Geospatial, Pretoria*")
    st.markdown("<span style='font-size: 90%; color: grey;'>January 2024 – August 2024</span>", unsafe_allow_html=True)
    st.write(
        "In my role as a Geospatial Developer at Swift Geospatial, I spearheaded the development and deployment of "
        "geospatial solutions and applications, catering specifically to precision agricultural, "
        "commercial forestry, and natural forestry sectors. Leveraging my proficiency in geoinformatics and "
        "python, I analyzed and visualized geospatial data, and engineered custom tools and algorithms. "
        "I actively collaborated with cross-functional teams, engaged with clients to understand requirements "
        "thoroughly and ensuring that the solutions aligned precisely with client needs. Furthermore, I harnessed "
        "AWS technologies to optimize geospatial solutions for enhanced performance and scalability.")

    # 3️⃣ Job: Swift Geospatial (R&D Engineer)
    st.markdown("### **Research & Development Engineer**  \n*Swift Geospatial*")
    st.markdown("<span style='font-size: 90%; color: grey;'>January 2021 – December 2023</span>",
                unsafe_allow_html=True)
    st.write("As a Research & Development Engineer at Swift Geospatial, I spearheaded pioneering research and crafted "
             "state-of-the-art technologies within the realm of geospatial science. Drawing upon my expertise in "
             "geoinformatics and python, I engineered algorithms, models, and systems tailored to elevate the analysis "
             "and visualization of geospatial data, particularly in precision agricultural, commercial forestry, "
             "and natural forestry applications. I fostered collaborative efforts within a dynamic team to innovate "
             "and bring forth novel products and solutions to market, integrating advanced Amazon Web Services (AWS) "
             "technologies for optimal performance and scalability.")

    # 4️⃣ Job: University of Pretoria
    st.markdown("### **Research Assistant**  \n*University of Pretoria*")
    st.markdown("<span style='font-size: 90%; color: grey;'>January 2019 – December 2020</span>",
                unsafe_allow_html=True)
    st.write("As a Research Assistant at the University of Pretoria, I assisted in conducting research projects in the "
             "field of geoinformatics. I worked closely with research teams to collect, analyze, and interpret "
             "geospatial data, and contributed to the development of research papers and publications. I utilized my "
             "knowledge of geoinformatics and data analysis techniques to support the research objectives and "
             "contribute to the advancement of knowledge in the field.")


elif page == "Work Case Studies":
    st.title("Work Case Studies")
    st.write("Due to highly confidential Non-disclosure Agreements (NDA's) between me and clients, I cannot openly share work intelectual property (IP), client names and scope of work. "
             If you wish to know, please contact me direclty via my work email address and I will happilly discuss what I can with you.")


elif page == "Publications":
    st.title("Publications")
    # Simulated popup/message box
    if not st.session_state.publications_confirmed:
        st.warning(
            "⚠️ This is a live web scrape of my publications. It may take a few seconds to load.\n\nClick OK to continue."
        )
        if st.button("Okay"):
            st.session_state.publications_confirmed = True
            # No need for rerun—next loop will skip message
    else:
        st.write("**This is a live web scrape of all publications, please allow some time for the scraping to complete.**")

        # Scholar scraping process
        author = scholarly.search_author_id("EmcpSGoAAAAJ")
        author = scholarly.fill(author, sections=['publications'])

        for pub in author['publications'][:10]:
            pub_filled = scholarly.fill(pub)
            title = pub_filled.get('bib', {}).get('title', 'No title')
            year = pub_filled.get('bib', {}).get('pub_year', 'Unknown year')
            url = pub_filled.get('pub_url', None)

            if url:
                if title == ('Managing, organising and sharing fine-grained data in the spatial design disciplines–An '
                             'evaluation of a GeoNode prototype'):
                    st.markdown(
                        f'• **{title} (Masters Dissertation)** ({year}) — <a href="{url}" target="_blank">Link</a>',
                        unsafe_allow_html=True)
                else:
                    st.markdown(
                        f'• **{title}** ({year}) — <a href="{url}" target="_blank">Link</a>',
                        unsafe_allow_html=True)

            else:
                st.markdown(f'• **{title}** ({year})')

elif page == 'Education':
    st.title("Education")

    # 1️⃣ Masters
    st.markdown("### **Master of Science in Geoinformatics**  \n*University of Pretoria, South Africa*")
    st.markdown("<span style='font-size: 90%; color: grey;'>January 2019 – December 2020</span>",
                unsafe_allow_html=True)
    st.write("During my Master's in Geoinformatics, I embarked on an ambitious project, conceptualizing and developing "
             "a cutting-edge GeoNode prototype. This endeavor showcased my adeptness in harnessing geospatial technologies "
             "for innovative solutions. Through meticulous research and hands-on implementation, I engineered a functional "
             "prototype demonstrating GeoNode's potential in efficient geospatial data management and sharing. This project, "
             "coupled with graduating with distinction, not only honed my technical skills but also enhanced problem-solving "
             "and innovation in the field. It served as a testament to my dedication to pushing boundaries and contributing "
             "meaningfully to the advancement of geospatial science and technology.")

    # 2️⃣ Honours
    st.markdown("### **Honours Degree in Geoinformatics**  \n*University of Pretoria, South Africa*")
    st.markdown("<span style='font-size: 90%; color: grey;'>January 2018 – December 2018</span>",
                unsafe_allow_html=True)
    st.write(
        "Completed an Honours degree in Geoinformatics, exhibiting a strong foundation in the interdisciplinary field "
        "of geographic information systems (GIS), remote sensing, and spatial analysis. Proficiently applied advanced "
        "geospatial technologies to address complex spatial challenges. Demonstrated expertise in geospatial data management, "
        "analysis, and visualization, along with a solid understanding of spatial modeling and cartography. Successfully "
        "completed a comprehensive research project, showcasing analytical skills and the ability to generate meaningful "
        "insights from spatial data, specifically OpenStreetMap (OSM) data.")

    # 3️⃣ Undergraduate
    st.markdown("### **Bachelor of Science in Geoinformatics**  \n*University of Pretoria, South Africa*")
    st.markdown("<span style='font-size: 90%; color: grey;'>January 2015 – December 2017</span>",
                unsafe_allow_html=True)
    st.write(
        "Completed an undergraduate degree in Geoinformatics, establishing a solid groundwork in the multifaceted domain "
        "of geographic information systems (GIS), remote sensing, and spatial analysis. Developed proficiency in utilizing "
        "geospatial technologies to address spatial challenges across various industries. Acquired fundamental skills in "
        "geospatial data management, analysis, and visualization, coupled with a basic understanding of spatial modeling "
        "and cartography. Engaged in coursework that emphasized practical applications of geoinformatics principles.")

elif page == "Contact":
    # Add a contact section
    st.title("Contact Information")
    # Define contact details
    work_email = "cameron.green@riskscape.pro"
    private_email = "camerongreen.me@gmail.com"
    linkedin = "https://www.linkedin.com/in/cameronlgreen/"
    github = "https://github.com/CamGreen"

    # Display LinkedIn as a clickable link
    st.markdown(
        f'<a href="{linkedin}" target="_blank">LinkedIn</a>',
        unsafe_allow_html=True
    )

    st.markdown(
        f'<a href="{github}" target="_blank">Github</a>',
        unsafe_allow_html=True
    )

    # Prepare subject and body (URL encoded)
    subject = quote("Inquiry about your professional services")
    body = quote("Hello,\n\nI would like to set up a meeting to discuss future projects")

    # Display mailto link properly
    st.markdown(
        f'<a href="mailto:{work_email}?subject={subject}&body={body}">Email me at work</a>',
        unsafe_allow_html=True
    )

    st.markdown(
        f'<a href="mailto:{private_email}?subject={subject}&body={body}">Email me privately</a>',
        unsafe_allow_html=True

    )



