# Automating Data Quality in Dev Environments

## Roadmap

* Data as a product instead of Data as a service
* Apply QA to high priority projects
* Know where you stand - do data audit
* Audit benchmarks
    - compliance to laws
    - context of current architecture
    - Quality of data

* Create current process map for the high priority project you chose

* Data quality
    - Metrics mean nothing without context

* Areas to Have Clear Quality Standards
    - Domain
    - Component
    - Freshness
    - Schema
    - Success conditions
    - Failed conditions

* Data observability
    - tracking and triaging data incidents to prevent downtime with data products

* Write a roadmap - ingredients
    - Data product vision
    - Key tasks and milestones
    - Essential data assets
    - Roles and responsibilities
    - Risks and mitigations
    - Data governance

* Roadmap
    - Shows all the people, processes, technology needed to build data product
    - Communicates long-term strategic view
    - Changes as business and user needs evolve

## Governance-Driven Development

* Data Requirements - include
    - User roles
    - Trigger points
    - Data points
    - Preconditions

* Confirm data source systems - contextual inquiry

* Establish right data system integrations - example
    - Security tokens
    - Cloud env
    - Data integration tool
    - Data storage platform
    - Real-time data stream
    - Staging area
    - Interactive computing platform
    - Business analytics platform

* Most data problems start with source systems

* Minimum acceptance criteria for data
    - Domain
    - Component name
    - Goal
    - Success conditions
    - Failed conditions

* Data Lineage tracking
    - Who using the data
    - What info that data contains
    - Where originated
    - When created and transformed throught product lifecycle
    - Why this data is most relevant for the product at hand

* Stages (ELT)
    1. Extraction
    2. Staging
    3. Transformation

* Levels of access per user (Data Governance) - example
    * Level 1, Sub-domain Marketing Leads
        - SEO, content
        - pull data within respective subdomains
        - view data in other subdomains
    * Level 2, Superuser
        - Heads of marketing, >= director-level
        - pull data from all subdomains
        - approve access to subdomains

    * Level 3, Admin
        - Data architects, colleagues in CISO
        - Maintain system
        - Uphold governance standards

* Future process map

* Define areas of data transformation (think of DBT)

* Choose super users to validate product

* Give data team room to fail (think of own schema for transformations)

## Monitor Data in Production
* Think of the github actions



