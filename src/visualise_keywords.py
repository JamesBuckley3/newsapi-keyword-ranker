import matplotlib.pyplot as plt


def fetch_keywords(conn, target_date, limit):
    """
    Fetches the top N keyword rankings for the target date from the database.

    Args:
        limit (int): Number of top keywords to return

    Returns:
        list of (keyword, count) tuples
    """
    query = """
        SELECT keyword, count
        FROM keyword_rankings
        WHERE collected_at = %s
        ORDER BY rank ASC
        LIMIT %s;
    """
    with conn.cursor() as cur:
        cur.execute(query, (target_date, limit))
        return cur.fetchall()


def plot_keywords(keywords, output_path):
    """
    Plots a bar chart of the most common keywords and saves it as a PNG.

    Args:
        keywords (list): List of (keyword, count) tuples
        output_path (str): File path to save the chart image
    """
    if not keywords:
        print("⚠️ No keyword data found to plot.")
        return

    # Split data into labels and values
    labels, values = zip(*keywords)

    # Create bar chart
    plt.figure(figsize=(10, 6))
    bars = plt.bar(labels, values, color="royalblue")

    plt.title("Top News Keywords (Yesterday)")
    plt.xlabel("Keyword")
    plt.ylabel("Mentions")
    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()

    # Add value labels above bars
    for bar in bars:
        height = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            height + 0.5,
            str(height),
            ha="center",
            va="bottom",
            fontsize=9,
        )

    plt.savefig(output_path)
    print(f"📊 Chart saved to {output_path}")
