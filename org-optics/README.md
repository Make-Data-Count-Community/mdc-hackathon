## Org Optics

### Goal
Provide user-friendly insights into dataset citations by institution.

### Overview
A website with profile pages for every organization with dataset citations, listing all datasets with citations, papers that cite dataset from the org, and summary statistic insights

### Why
- Organizations can see insights about where data from their institution is being cited
- Potential applicants can look at the type of impactful data coming out of universities
- Researchers can look at the impact of their data publications (once we add researcher pages)

### Organization profile page details (_[Mock-up](https://docs.google.com/presentation/d/1Zxmi0uE597ADKV-C9dUEYbQCExrdAjOpOD8Bwkg4uLQ/edit#slide=id.p)_)
- Header at the top with organization information from ROR 
   - Institution name
   - Location 
   - Website 
   - ROR ID 
- Summary tab pulling Tableau visualizations filtered on that organization 
   - Citations by year 
   - Citations by subject 
   - Subject/Publication links 
- Datasets tab listing all datasets that are in the corpus
   - Title linking to dataset
     - Number of citations
       - Clicking brings up the list on the next tab
     - Subject area(s)
     - Repository 
     - Funder
  - Sort options on page (up and down if clicked)
    - Name 
    - Year 
    - Citation count 
  - Filter options on page 
    - Subject  
    - Repository 
    - Funder 
- Citing Papers tab listing all publications that cite a dataset from that org 
  - Link that brings you to that paper’s DOI 
    - Number of datasets they cite 
      - Clicking brings up the list of datasets on the previous page 
    - Subject area(s)
    - Publisher & Journal 
    - Funders 
  - Sort options on page (up and down if clicked)
    - Name 
    - Year 
    - Datasets cited 
  - Filter options on page
    - Subject 
    - Publisher 
    - Journal 
    - Funder


### Dependencies

- Complete and accurate affiliation and funder details for citation records
   - Missing ~98% currently 
- ROR ID for all affiliations 
- Complete and accurate DOI links for all datasets and citing publications 
- Dataset and publication titles for citation records 
- Embeddable Tableau/LookerStudio visualization filtered on organization by ROR ID 
   - Created by data-viz team 
- Search page built by data-retrievers team that links to org profile pages

### Future directions
- Funder and Researcher profile pages that may have slight differences
- Additional org information such as logo, header image for more customization

### Contributors

- Becky Grady
- Sean McIntyre
- Juliet Shin
- Jing Jiang
- Eric Lopatin
