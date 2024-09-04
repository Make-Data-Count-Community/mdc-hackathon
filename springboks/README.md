## The springboks

### Members

- nlisgo (Nathan Lisgo)
- Nimphal
- kaysiz

### Hackathon Focus

Our primary objective was to interact with the Crossref API to retrieve missing publication titles in cases where the title field was empty. We aimed to improve the quality and completeness of our dataset by filling in these gaps.

However, during our initial exploration, we found that out of 50 sample rows from `./assertion_without_title_and_journal.csv`, 17 returned a 404 error from Crossref, indicating that the DOIs associated with these entries could not be resolved. This inability to resolve the DOIs directly impacts the quality and reliability of our data, highlighting a key challenge in maintaining accurate metadata for publications.

### Parse

```bash
cat ./assertions_without_title_and_journal.csv | python parse.py > output.csv
```

### Investigative next steps

There are publications whose DOIs resolve but they do not exist in CrossRef. This makes is a bit more of a challenge to find out more information about them, but not impossible. From the provided example files, one such DOI is `10.22034/APJCP.2017.18.12.324`

We can use the Europe PMC API to get some more data

```bash
curl https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.22034/APJCP.2017.18.12.3245&format=json
```

This gives us the journal name and the journal ISSN. In this case there are two different journal ISSNs. We can query cross ref for each one:

```bash
curl -X 'GET' \
  'https://api.crossref.org/journals/1513-7368' \
  -H 'accept: application/json'
```
which gives us "Asian Pacific Organization for Cancer Prevention" as the publisher with publication dates range 2012-2016.

The other ISSN:
```bash
curl -X 'GET' \
  'https://api.crossref.org/journals/2476-762x' \
  -H 'accept: application/json'
```

which gives us "EpiSmart Science Vector Ltd" as the publisher with publication date ranges 2017-present.

This suggests that the journal changed publishers. The DOI above was published with the newer publisher.
