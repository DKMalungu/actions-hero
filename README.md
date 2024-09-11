# actions-hero
Certainly! If you want to replace the role segment with hypervisor details, you can modify the naming convention accordingly. Here is the updated server naming convention:

---

# Server Naming Convention

## Purpose
The purpose of this naming convention is to provide a standardized method for naming servers to ensure consistency, ease of management, and quick identification of server locations, environments, and hypervisor details.

## Naming Structure
The server name will be composed of several segments, each representing specific information about the server. The general format is:

```
[Location]-[Environment]-[Hypervisor]-[Sequence Number]
```

### Segments

1. **Location (LOC)**
   - A three-letter code representing the physical or logical location of the server.
   - Example: `NYC` for New York City, `LON` for London, `SFO` for San Francisco.

2. **Environment (ENV)**
   - A two-letter code representing the server environment.
   - Example: `PR` for Production, `ST` for Staging, `QA` for Quality Assurance, `DE` for Development.

3. **Hypervisor (HYP)**
   - A three-letter code representing the hypervisor type.
   - Example: `XEN` for XenServer, `VSP` for VMware vSphere, `HYP` for Microsoft Hyper-V, `KVM` for Kernel-based Virtual Machine.

4. **Sequence Number (SEQ)**
   - A two-digit sequence number to uniquely identify servers with the same location, environment, and hypervisor.
   - Example: `01`, `02`, `03`.

### Example Server Names
- `NYC-PR-XEN-01`: A production server running XenServer located in New York City.
- `LON-ST-VSP-02`: A staging server running VMware vSphere located in London.
- `SFO-QA-HYP-03`: A QA server running Microsoft Hyper-V located in San Francisco.

## Guidelines

1. **Consistency**
   - Always use the defined codes for location, environment, and hypervisor.
   - Ensure sequence numbers are unique within the same location, environment, and hypervisor.

2. **Readability**
   - Use hyphens (`-`) to separate different segments for better readability.
   - Avoid using special characters or spaces in server names.

3. **Documentation**
   - Maintain a centralized document or database that lists all server names along with their descriptions and purposes.
   - Update the documentation whenever a new server is added or an existing server is decommissioned.

4. **Flexibility**
   - Adapt the naming convention as needed to accommodate new locations, environments, or hypervisors.
   - Ensure any changes to the naming convention are communicated to all relevant personnel.

## Common Codes

### Location Codes
- `NYC`: New York City
- `LON`: London
- `SFO`: San Francisco
- `TOK`: Tokyo
- `SYD`: Sydney

### Environment Codes
- `PR`: Production
- `ST`: Staging
- `QA`: Quality Assurance
- `DE`: Development
- `DR`: Disaster Recovery

### Hypervisor Codes
- `XEN`: XenServer
- `VSP`: VMware vSphere
- `HYP`: Microsoft Hyper-V
- `KVM`: Kernel-based Virtual Machine

---

By following this server naming convention, your organization can achieve a more organized and manageable IT infrastructure, making it easier to identify and manage servers based on their location, environment, and hypervisor type.
