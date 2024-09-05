
### Project Summary: DOI Normalization, testing and repository identification in the Data Citation Corpus

Our project built upon prior work done by the springboks team, who identified problems in resolving and identifying DOIs for entries the Data Citation Corpus. We took as our objective to explore methods for programmatically normalizing and validating DOIs for publications and datasets, pulling metadata for valid entries to help complete them as well as detecting non-DOI publication identifiers. Using these techniques, we aimed to improve the overall quality and completeness of the corpus, as well as increase the total level of repositories identified.


#### 1. **DOI Normalization and Resolution**
   - **Process:** 
     - The core logic of our work involved taking each DOI, attempting to normalize and then resolve it, logging the normalized DOI and HTTP response code returned.
     - For each DOI that returned a successful response, we pulled in basic metadata (title, publisher) to assess its validity and usefulness in completing the entires.
   - **Results:** 
     - Testing with a sample of entries that lacked repository identification, we found a number of DOIs that failed to resolve, indicating potential quality issues for this set of citations.
     - For those DOIs that did resolve, we successfully retrieved the corresponding metadata, confirming the utility of this basic form of validation and extraction.

#### 2. **Detection of Non-DOI Identifiers**
   - **Process:** 
     - For cases where the publication identifier did not appear to conform to a DOI format (regex match), we developed logic to check the identifier against known regex patterns for accession numbers and similar identifier in the corpus.
   - **Results:** 
     - Testing with a sample containing these non-DOI values, we found that the regex matching logic was successful in identifying valid non-DOI identifiers, allowing for repository identification.
