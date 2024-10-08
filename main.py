import streamlit as st
from scrape import scrape_website, split_dom_content, clean_body_content, extract_body_content

st.title("AI Web Scraper")
url = st.text_input("Enter a website URL: ")

if st.button("Scraper Site"):
    st.write("Scraping the website")
    
    result = scrape_website(url)
    body_content = extract_body_content(result)
    cleaned_content = clean_body_content(body_content)
    
    # Store the cleaned content in the streamlit session 
    # so we can access it later.
    st.session_state.dom_content = cleaned_content
    
    # Expander (dropdown) that says "View more content".  When clicked...
    with st.expander("View DOM Content"):
        # ... display a text area containing the cleaned content.
        st.text_area("DOM Content", cleaned_content, height=300)

    
if "dom_content" in st.session_state:
    # Create a new text area with the following label "Describe..." to allow
    # the user to write their prompt for the LLM.
    parse_description = st.text_area("Describe what you want to parse")  
    
    # Create a "Parse Content" button.
    if st.button("Parse Content"):
        if parse_description:
            st.write("Parsing the content...")
            
            dom_chunks = split_dom_content(st.session_state.dom_content)
    
