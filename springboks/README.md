## The springboks

### Members

- nlisgo
- Nimphal
- kaysiz

### Hackathon Focus

Our primary objective was to interact with the Crossref API to retrieve missing publication titles in cases where the title field was empty. We aimed to improve the quality and completeness of our dataset by filling in these gaps.

However, during our initial exploration, we found that out of 50 sample rows from `./assertion_without_title_and_journal.csv`, 17 returned a 404 error from Crossref, indicating that the DOIs associated with these entries could not be resolved. This inability to resolve the DOIs directly impacts the quality and reliability of our data, highlighting a key challenge in maintaining accurate metadata for publications.

### Parse

```bash
cat ./assertions_without_title_and_journal.csv | python parse.py > output.csv
```
