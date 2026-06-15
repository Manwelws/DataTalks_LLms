from sqlitesearch import TextSearchIndex
from ingest import load_faq_data
documents = load_faq_data()

index = TextSearchIndex(
    text_fields= ['question','section','answer'],
    keyword_fields=['course'],
    db_path="FAQ.db"
)

index.fit(documents)