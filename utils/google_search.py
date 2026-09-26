import streamlit as st
import requests


GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]
GOOGLE_CSE_ID = st.secrets["GOOGLE_CSE_ID"]


def google_search(query, max_results=10):
    search_url = "https://www.googleapis.com/customsearch/v1"

    params = {
        "key": GOOGLE_API_KEY,
        "cx": GOOGLE_CSE_ID,
        "q": query,
        "num": min(max_results, 10)
    }

    try:
        response = requests.get(
            search_url,
            params=params,
            timeout=15
        )

        response.raise_for_status()

        data = response.json()

        items = data.get("items", [])
        results = []

        for item in items:
            results.append({
                "title": item.get("title", "No title"),
                "link": item.get("link", ""),
                "description": item.get("snippet", "")
            })

        return results

    except Exception as e:
        print("Google Search API Error:", e)
        return []
