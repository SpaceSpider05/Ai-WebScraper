import streamlit as st
from scraper import scrape_website, split_dom_content, clean_body_content, extract_body_content
from parseai import parse_with_openai  # Updated import for correct function
import time 
st.title("AI Web Scraper")

web_site_url = st.text_input("Enter the website URL you want to scrape:")

if st.button("Scrape site"):
    st.write("wait a moment ")
    time.sleep(2)
    st.write("Collecting data...")
    result = scrape_website(web_site_url)
    body_content = extract_body_content(result)
    cleaned_content = clean_body_content(body_content)

    st.session_state.dom_content = cleaned_content

    with st.expander("View Keys content"):
        st.text_area("Keys content", value=cleaned_content, height=600)

if "dom_content" in st.session_state:
    parse_description = st.text_area("Describe what you want to parse from the content:", height=100)

    if st.button("Parse content"):
        if parse_description:
            st.write("Parsing content...")
            dom_chunks = split_dom_content(st.session_state.dom_content)
            result = parse_with_openai(dom_chunks, parse_description)
            st.write(result)
