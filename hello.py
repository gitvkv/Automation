Management Architecture for GNC Light
In the standard GNC deployment, management services such as CVA (CloudVision Analytics) and CVP (CloudVision Portal) are hosted locally within each data center. These components manage the GNC switches deployed in that specific location.

However, this model is not scalable or cost-effective for smaller server rooms, which are the target of the GNC Light solution. Hosting a local CVA/CVP for every server room would result in:

Increased hardware and licensing costs

Operational complexity due to numerous distributed management systems

Difficulties in global support, maintenance, and compliance

Centralized Management Approach in GNC Light
To address these challenges, GNC Light adopts a centralized management model:

CVA and CVP services will not be hosted locally in server rooms.

Instead, GNC Light switches will be managed remotely by centralized CVPs deployed in strategic data centers.

This architecture reduces the hardware footprint and simplifies global management by consolidating control infrastructure.

Resiliency Design – CVP Clusters in Asia Pacific
To ensure high availability and geographic redundancy, two centralized CVP clusters will be deployed in the Asia Pacific region:

Primary Cluster: Singapore

Secondary Cluster: Japan

This dual-cluster design supports failover and continuity in case the primary site becomes unavailable.

Deployment Models for CVP Resiliency
Two deployment strategies are available to support dual-cluster resiliency:

1. Gold Standby
The secondary cluster remains powered off during normal operation.

In case of failure at the primary site:

The secondary cluster is activated manually.

Configuration and device data are restored from backup.

Pros: Lower resource usage during standby

Cons: Recovery time is longer due to manual activation

2. Warm Standby
Both clusters are active and receive real-time telemetry from the switches.

Switches are dual-registered to both clusters:

Primary cluster handles provisioning and operations

Secondary cluster acts as a live standby

Ensures seamless monitoring and provisioning continuity if the primary cluster fails

Pros: Faster failover and zero data loss

Cons: Requires more resources and ongoing synchronization

Network Communication Architecture
The communication between GNC Light switches and centralized CVPs will traverse the Control Network (DAN).

CVP subnets will be:

Advertised to local IC firewalls

Firewalls will then advertise these routes to core DAN switches

Core DAN will route this traffic over the global control network

This design ensures secure, reliable, and scalable connectivity between remote server rooms and centralized management infrastructure.
