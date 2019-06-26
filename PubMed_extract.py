import eutils
from metapub import PubMedFetcher
fetch = PubMedFetcher()

# get the first 1000 pmids matching "breast neoplasm" keyword search
pmids = fetch.pmids_for_query('breast neoplasm', retmax=1000)

# get abstract for each article:
abstracts = {}
for pmid in pmids:
    abstracts[pmid] = fetch.article_by_pmid(pmid).abstract