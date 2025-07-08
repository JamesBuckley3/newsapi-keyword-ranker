import pandas as pd
import spacy


def load_and_clean():
    """
    Loads the keyword ranking data from a CSV file.

    Returns:
        pandas.DataFrame: A DataFrame containing keyword rankings,
        including at least a 'keyword' column.
    """
    keywords_df = pd.read_csv(
        "C:\\Users\\You\\newsapi-keyword-ranker\\data\\keyword_rankings_.csv"
    )  # Change to your keyword_rankings CSV path
    return keywords_df


def nlp_tagging_to_csv(keywords):
    """
    Applies NLP tagging to unique keywords and exports the results to a CSV file.

    Performs part-of-speech tagging, lemmatisation, and named entity recognition
    using spaCy's transformer-based English model (`en_core_web_trf`).

    Args:
        keywords (pandas.DataFrame): DataFrame containing a 'keyword' column.

    Outputs:
        A CSV file named 'keyword_nlp_analysis.csv' saved to disk, containing:
            - keyword
            - pos (coarse POS tag)
            - tag (fine-grained POS tag)
            - lemma (base word form)
            - entity (entity label, if applicable)
            - is_entity (boolean indicating entity presence)
            - extracted_entity_text (named entity text if applicable)
    """
    nlp = spacy.load("en_core_web_trf")
    records = []

    unique_keywords = (
        keywords["keyword"].dropna().drop_duplicates().reset_index(drop=True)
    )

    for keyword in unique_keywords:
        doc = nlp(keyword)

        token = doc[0]
        pos = token.pos_
        tag = token.tag_
        lemma = token.lemma_

        if doc.ents:
            ent_label = doc.ents[0].label_
            ent_text = doc.ents[0].text
            is_entity = True
        else:
            ent_label = ""
            ent_text = ""
            is_entity = False

        records.append(
            {
                "keyword": keyword,
                "pos": pos,
                "tag": tag,
                "lemma": lemma,
                "entity": ent_label,
                "is_entity": is_entity,
                "extracted_entity_text": ent_text,
            }
        )

    output_df = pd.DataFrame(records)
    output_df.to_csv(
        "C:\\Users\\You\\newsapi-keyword-ranker\\data\\keyword_nlp_analysis.csv",
        index=False,
    )  # Change to your output path
    print("✅ Unique keyword tagging complete and saved to CSV.")


def main():
    """
    Orchestrates the NLP tagging pipeline:
    - Loads keyword data
    - Processes each unique keyword with NLP
    - Saves results to CSV
    """
    keywords = load_and_clean()
    nlp_tagging_to_csv(keywords)


if __name__ == "__main__":
    main()
