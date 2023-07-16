# California Power Outages Bot
- Toot about power outages in California.
  - Map of power outage.
  - Power Outage within current day and current hour.
  
Mastodon: https://mastodon.world/@california_power_outage
  
  <img width="556" alt="california_power_outage" src="https://user-images.githubusercontent.com/20311850/230490132-fbec7077-c027-49e1-bae7-72737b091766.png">

### Main flow
```
main.py
```

### Tests
```
python -m unittest discover
```

### Flowchart 
```mermaid

flowchart LR
    A1[Start] --> A2(Request API)
    style A1 fill:#333,stroke:#d4d3cf,color:#fff,stroke-width:2px
    style A2 fill:#faf1c5,stroke:#d4d3cf,color:#333,stroke-width:2px

    A2 --> A3("Create Power 
    Outage Object")
    style A3 fill:#faf1c5,stroke:#d4d3cf,color:#333,stroke-width:2px

    A3-->A31("Only Power Outage 
    during this hour")
    style A31 fill:#faf1c5,stroke:#d4d3cf,color:#333,stroke-width:2px

    A31 --> A4{"Any Power 
    Outage?"}
    style A4 fill:#f2c199,stroke:#d4d3cf,color:#333,stroke-width:2px

    A4 --> |Yes| A10("Draw Power 
    Outage map")
    style A10 fill:#faf1c5,stroke:#d4d3cf,color:#333,stroke-width:2px

    A10 --> A12("Create status")
    style A12 fill:#faf1c5,stroke:#d4d3cf,color:#333,stroke-width:2px

    A12 --> A13(Tooting)
    style A13 fill:#faf1c5,stroke:#d4d3cf,color:#333,stroke-width:2px

    A13 --> A14[Finished]
    style A14 fill:#333,stroke:#d4d3cf,color:#fff,stroke-width:2px

    A4 --> |No| A6("Print: no 
    Power Outage")
    style A6 fill:#f7c5fa,stroke:#d4d3cf,color:#333,stroke-width:2px

    A6 --> A66[Exit] 
    style A66 fill:#333,stroke:#d4d3cf,color:#fff,stroke-width:2px


```
