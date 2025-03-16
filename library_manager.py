import streamlit as st
import pandas as pd
import json
import os
import plotly.express as px
from datetime import datetime


LIBRARY_FILE = "library.json"


def load_library():
    if os.path.exists(LIBRARY_FILE):
        with open(LIBRARY_FILE, "r") as file:
            return json.load(file)
    return []


def save_library(library):
    with open(LIBRARY_FILE, "w") as file:
        json.dump(library, file, indent=4)


st.set_page_config(page_title="Personal Library Manager",
                   page_icon="📚", layout="wide")

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown("""
        <h1 style='text-align: center; color: #1E88E5; margin-bottom: 30px;'>
            📚 Personal Library Manager
        </h1>
    """, unsafe_allow_html=True)

library = load_library()

# Sidebar
menu = st.sidebar.radio(
    "Menu", ["View Library", "Add a Book", "Search Books", "Library Statistics"])

# Add book
if menu == "Add a Book":
    st.subheader("➕ Add a New Book")
    title = st.text_input("Title")
    author = st.text_input("Author")
    year = st.number_input(
        "Publication Year", min_value=1000, max_value=9999, step=1)
    genre = st.text_input("Genre")
    read_status = st.checkbox("Have you read this book?")

    if st.button("Add Book"):
        new_book = {"title": title, "author": author, "publish_year": int(
            year), "genre": genre, "read_status": read_status, "added_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
        library.append(new_book)
        save_library(library)
        st.success(f"'{title}' added successfully!")

# Search book
elif menu == "Search Books":
    st.subheader("🔍 Search for a Book")
    search_query = st.text_input("Enter title or author")
    if search_query:
        results = [book for book in library if search_query.lower(
        ) in book["title"].lower() or search_query.lower() in book["author"].lower()]
        if results:
            for i in range(0, len(results), 2):
                col1, col2 = st.columns(2)

                for col, index in zip([col1, col2], [i, i+1]):
                    if index < len(results):
                        with col:
                            with st.container():
                                st.markdown(
                                    f"""
                                    <div style="
                                        padding: 20px;
                                        border-radius: 10px;
                                        margin: 10px 5px;
                                    ">
                                    """, unsafe_allow_html=True)

                                # Title
                                st.markdown(
                                    f"""
                                    <h3 style='margin: 0 0 10px 0; color: #333;'>{results[index]['title']}</h3>
                                    """, unsafe_allow_html=True)

                                # Books Detail
                                st.markdown(
                                    f"""
                                    <p style='color: #555;'><b>Author:</b> {results[index]['author']}</p>
                                    <p style='color: #555;'><b>Publication Year:</b> {results[index]['publish_year']}</p>
                                    <p style='color: #555;'><b>Genre:</b> {results[index]['genre']}</p>
                                    """, unsafe_allow_html=True)

                                # Status Badge
                                status = "Read" if results[index]["read_status"] else "Unread"
                                status_color = "#2E7D32" if results[index]["read_status"] else "#C62828"
                                st.markdown(
                                    f"""
                                    <div style='
                                        display: inline-block;
                                        padding: 6px 14px;
                                        border-radius: 12px;
                                        color: white;
                                        background-color: {status_color};
                                        font-size: 0.9em;
                                        font-weight: bold;
                                        margin-bottom: 10px;
                                    '>{status}</div>
                                    """, unsafe_allow_html=True)

                                st.markdown(f"""</div>""",
                                            unsafe_allow_html=True)

                                # Buttons
                                btn1, btn2 = st.columns(2)

                                with btn1:
                                    if st.button("Remove", key=f"remove_search_{index}", use_container_width=True):
                                        # Find the book in the original library and remove it
                                        book_to_remove = results[index]
                                        library.remove(book_to_remove)
                                        save_library(library)
                                        st.rerun()

                                with btn2:
                                    if st.button(
                                        "Mark as Unread" if results[index]["read_status"] else "Mark as Read",
                                        key=f"toggle_search_{index}",
                                            use_container_width=True):
                                        # Find the book in the original library and update its status
                                        book_to_update = results[index]
                                        lib_index = library.index(
                                            book_to_update)
                                        library[lib_index]["read_status"] = not library[lib_index]["read_status"]
                                        save_library(library)
                                        st.rerun()
        else:
            st.info("No matching books found.")

elif menu == "View Library":
    st.subheader("📖 Your Library Collection")

    if library:
        for i in range(0, len(library), 2):
            col1, col2 = st.columns(2)

            for col, index in zip([col1, col2], [i, i+1]):
                if index < len(library):
                    with col:
                        with st.container():
                            st.markdown(
                                f"""
                                <div style="
                                    padding: 20px;
                                    border-radius: 10px;
                                    margin: 10px 5px;
                                ">
                                """, unsafe_allow_html=True)

                            # Title
                            st.markdown(
                                f"""
                                <h3 style='margin: 0 0 10px 0; color: #333;'>{library[index]['title']}</h3>
                                """, unsafe_allow_html=True)

                            # Books Detail
                            st.markdown(
                                f"""
                                <p style='color: #555;'><b>Author:</b> {library[index]['author']}</p>
                                <p style='color: #555;'><b>Publication Year:</b> {library[index]['publish_year']}</p>
                                <p style='color: #555;'><b>Genre:</b> {library[index]['genre']}</p>
                                """, unsafe_allow_html=True)

                            # Status Badge
                            status = "Read" if library[index]["read_status"] else "Unread"
                            status_color = "#2E7D32" if library[index]["read_status"] else "#C62828"
                            st.markdown(
                                f"""
                                <div style='
                                    display: inline-block;
                                    padding: 6px 14px;
                                    border-radius: 12px;
                                    color: white;
                                    background-color: {status_color};
                                    font-size: 0.9em;
                                    font-weight: bold;
                                    margin-bottom: 10px;
                                '>{status}</div>
                                """, unsafe_allow_html=True)

                            st.markdown(f"""</div>""", unsafe_allow_html=True)

                            # Buttons
                            btn1, btn2 = st.columns(2)

                            with btn1:
                                if st.button("Remove", key=f"remove_{index}", use_container_width=True):
                                    library.pop(index)
                                    save_library(library)
                                    st.rerun()

                            with btn2:
                                if st.button(
                                    "Mark as Unread" if library[index]["read_status"] else "Mark as Read",
                                    key=f"toggle_{index}",
                                        use_container_width=True):
                                    library[index]["read_status"] = not library[index]["read_status"]
                                    save_library(library)
                                    st.rerun()

    else:
        st.info("Your library is empty. Start adding books!")

# Display statistics
elif menu == "Library Statistics":
    st.subheader("📊 Library Statistics")

    col1, col2, col3, col4 = st.columns(4)

    total_books = len(library)
    read_books = sum(1 for book in library if book["read_status"])
    unread_books = total_books - read_books
    read_percentage = (read_books / total_books *
                       100) if total_books > 0 else 0

    with col1:
        st.metric(
            "Total Books",
            total_books,
            delta=None,
            help="Total number of books in your library"
        )

    with col2:
        st.metric(
            "Read Books",
            read_books,
            delta=f"{read_percentage:.1f}%",
            delta_color="normal",
            help="Number of books you've read"
        )

    with col3:
        st.metric(
            "Unread Books",
            unread_books,
            delta=f"{100-read_percentage:.1f}%",
            delta_color="inverse",
            help="Number of books yet to read"
        )

    with col4:
        current_month = datetime.now().strftime("%Y-%m")
        books_this_month = sum(1 for book in library if book.get(
            "added_date", "").startswith(current_month))
        st.metric(
            "Added This Month",
            books_this_month,
            help="Books added in the current month"
        )

    chart_col1, chart_col2 = st.columns(2)

    with chart_col1:
        st.markdown("### Reading Status Distribution")
        status_data = pd.DataFrame({
            "Status": ["Read", "Unread"],
            "Count": [read_books, unread_books]
        })
        fig_status = px.pie(
            status_data,
            names="Status",
            values="Count",
            color="Status",
            color_discrete_map={"Read": "#2E7D32", "Unread": "#C62828"},
            hole=0.4
        )
        fig_status.update_layout(
            showlegend=True,
            legend=dict(orientation="h", yanchor="bottom",
                        y=1.02, xanchor="right", x=1),
            margin=dict(l=20, r=20, t=40, b=20),
            height=300
        )
        st.plotly_chart(fig_status, use_container_width=True)

    with chart_col2:
        st.markdown("### Top Genres")
        genre_counts = pd.DataFrame(
            [[book["genre"], 1] for book in library],
            columns=["Genre", "Count"]
        ).groupby("Genre").sum().reset_index().sort_values("Count", ascending=True)

        fig_genres = px.bar(
            genre_counts.tail(5),
            x="Count",
            y="Genre",
            orientation='h',
            color="Count",
            color_continuous_scale=["#C62828", "#2E7D32"]
        )
        fig_genres.update_layout(
            showlegend=False,
            margin=dict(l=20, r=20, t=40, b=20),
            height=300
        )
        st.plotly_chart(fig_genres, use_container_width=True)

    st.markdown("### 📚 Top Authors")
    author_stats = {}
    for book in library:
        author = book["author"]
        if author in author_stats:
            author_stats[author]["total"] += 1
            if book["read_status"]:
                author_stats[author]["read"] += 1
        else:
            author_stats[author] = {
                "total": 1,
                "read": 1 if book["read_status"] else 0
            }

    author_df = pd.DataFrame([
        {
            "Author": author,
            "Total Books": stats["total"],
            "Read Books": stats["read"],
            "Unread Books": stats["total"] - stats["read"],
            "Reading Progress": f"{(stats['read']/stats['total']*100):.1f}%"
        }
        for author, stats in author_stats.items()
    ]).sort_values("Total Books", ascending=False)

    if not author_df.empty:
        top_authors = author_df.head(5)

        def color_progress(val):
            """Color the Reading Progress column based on percentage"""
            try:
                percentage = float(val.strip('%'))
                if percentage >= 75:
                    return 'background-color: #a8e6cf'
                elif percentage >= 50:
                    return 'background-color: #dcedc1'
                elif percentage >= 25:
                    return 'background-color: #ffd3b6'
                else:
                    return 'background-color: #ffaaa5'
            except:
                return ''

        styled_df = top_authors.style\
            .apply(lambda x: ['background-color: #f0f2f6' if i % 2 == 0 else '' for i in range(len(x))], axis=0)\
            .applymap(color_progress, subset=['Reading Progress'])\
            .set_properties(**{
                'text-align': 'center',
                'font-size': '14px',
                'padding': '10px'
            })\
            .hide(axis="index")

        st.dataframe(
            styled_df,
            use_container_width=True,
            height=min(len(top_authors) * 35 + 38, 300)
        )
    else:
        st.info("Add some books to see author statistics!")

    st.markdown("### Monthly Reading Progress")
    if library:
        monthly_progress = {}
        for book in library:
            if "added_date" in book:
                month = book["added_date"][:7]
                if month in monthly_progress:
                    monthly_progress[month]["total"] += 1
                    if book["read_status"]:
                        monthly_progress[month]["read"] += 1
                else:
                    monthly_progress[month] = {
                        "total": 1,
                        "read": 1 if book["read_status"] else 0
                    }

        progress_df = pd.DataFrame([
            {
                "Month": month,
                "Total Books": stats["total"],
                "Read Books": stats["read"]
            }
            for month, stats in monthly_progress.items()
        ]).sort_values("Month")

        fig_progress = px.line(
            progress_df,
            x="Month",
            y=["Total Books", "Read Books"],
            title="Monthly Reading Progress",
            markers=True
        )
        fig_progress.update_layout(
            xaxis_title="Month",
            yaxis_title="Number of Books",
            legend=dict(orientation="h", yanchor="bottom",
                        y=1.02, xanchor="right", x=1),
            margin=dict(l=20, r=20, t=40, b=20),
            height=300
        )
        st.plotly_chart(fig_progress, use_container_width=True)
