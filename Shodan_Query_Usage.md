
# Shodan Query Usage Guide

## Understanding Shodan Queries

Shodan is a specialized search engine that indexes information about devices connected to the internet. Instead of searching for website text like traditional search engines, Shodan lets you look up servers, routers, webcams, or other networked devices based on their banners, metadata, and various service responses.

A **Shodan query** is a keyword-based filter that tells Shodan what data you want to find. By leveraging specific keywords, filters, and Boolean logic, you can narrow results to a particular service, geographic location, device type, or vulnerability.

---

## Basic Queries

- **Single Keywords:**  
  *Example:* `JAWS/1.0`  
  This searches for any device banners that contain the keyword "JAWS/1.0", which often relates to certain embedded web servers.

- **Common Device Types:**  
  Searching for banners that reference specific device types or services can help you find devices of interest.  
  *Examples:*  
  - `apache` (Find servers running Apache)  
  - `nginx` (Find servers running Nginx)  
  - `ip camera` or `DVR` (Find IP cameras or Digital Video Recorders)  
  - `ftp` or `telnet` (Locate devices with FTP or Telnet services open)

---

## Advanced Filters and Modifiers

Shodan provides several filters (sometimes called "facets") that allow you to refine search results. Filters are applied using the syntax `filter:value`.

### Common Filters

1. **host:**  
   Restrict results to a particular hostname or domain.  
   *Example:* `host:example.com`
   
2. **port:**  
   Limit results to a specific port number. This is useful when you only want to see services running on known ports (e.g., `80` for HTTP, `443` for HTTPS, `22` for SSH).  
   *Example:* `apache port:443`
   
3. **country:**  
   Show results from a specific country using the two-letter country code.  
   *Example:* `nginx country:US`
   
4. **city:**  
   Narrow down results by city.  
   *Example:* `ftp city:"New York"`
   
5. **org:**  
   Filter results to a particular organization or ISP.  
   *Example:* `vnc org:"Comcast Cable Communications"`
   
6. **isp:**  
   Similar to `org`, but specifically matches the Internet Service Provider name.  
   *Example:* `ssh isp:"AT&T Services"`
   
7. **os:**  
   Show devices running a specific operating system. This can be helpful if you want to identify systems running outdated OS versions.  
   *Example:* `os:"Windows XP"`
   
8. **before:** and **after:**  
   Filter by time. These filters allow you to restrict results to devices that Shodan last saw before or after a certain date. Use YYYY-MM-DD format.  
   *Examples:*  
   - `apache before:2023-01-01`  
   - `nginx after:2024-06-15`
   
9. **geo:**  
   Specify a latitude/longitude pair with a radius (in kilometers) to find devices near a geographic point.  
   *Example:* `geo:"37.7749,-122.4194"` (Approx. San Francisco area)
   
10. **ssl:**  
    Filter for specific SSL-related metadata (e.g., by common name, issuer). For instance:  
    - `ssl:"Let's Encrypt"` to find certificates issued by Let’s Encrypt.

---

## Boolean Operators

Use logical operators to refine your queries:

- **AND** (default): All keywords must appear. (Shodan applies `AND` logic by default, so typing multiple terms is equivalent to `term1 AND term2`.)  
  *Example:* `apache ssl` finds devices whose banners contain both "apache" and "ssl".

- **OR**: Either keyword can appear.  
  *Example:* `apache OR nginx` finds devices running Apache or Nginx.

- **NOT** or `-`: Exclude results containing a certain keyword.  
  *Example:* `apache -nginx` finds devices running Apache but not those mentioning Nginx.

---

## Specific Use Cases and Specialized Queries

- **Finding Vulnerable Services or Weak Configurations:**  
  Using certain known strings or patterns in banners can help locate vulnerable services. For instance, known default credentials or certain outdated version strings can yield interesting results.  
  *Example:* `“default password” admin` might reveal devices that mention default login credentials in their banners.

- **IP Cameras with Weak Authentication:**  
  Shodan can index the favicon of a device's web interface. Finding a unique favicon hash associated with a default camera interface can lead you to IP cameras that still use default or weak authentication.  
  *Example:* `http.favicon.hash:-123456789` (Replace with actual hash from a known camera login page.)

- **Identifying Industrial Control Systems (ICS):**  
  Searching for ICS-related protocols or vendors can lead you to SCADA systems or other critical infrastructure devices. Always proceed with caution and legality in mind.  
  *Example:* `modbus` or `tag:"scada"` (if supported)

---

## Practical Tips

- **Start Broad, Then Narrow Down:**  
  Begin with a general keyword (e.g., `apache`) and then apply filters to reduce the noise:  
  `apache country:US port:443`

- **Use Quotation Marks for Phrases:**  
  If a keyword is made up of multiple words, put it in quotes. For example:  
  `"D-Link Camera"`

- **Check Shodan’s Documentation and Support:**  
  Shodan frequently updates its features and filters. Refer to the official documentation (https://help.shodan.io/) for the most up-to-date search parameters, or look up the `Explore` section on Shodan for popular community-provided queries.

---

## Ethical and Legal Considerations

When using Shodan, remember that the service indexes publicly available information. However, what you do with that information matters. Avoid:

- Attempting to gain unauthorized access to systems.
- Searching for content or devices in violation of local laws.
- Exploiting vulnerabilities found through Shodan.

Always adhere to Shodan’s terms of service and consult local laws before conducting security research.

---

## Conclusion

By combining keywords, advanced filters, and logical operators, you can create highly targeted Shodan queries. This precision helps you quickly find relevant devices, services, or vulnerabilities. Always use these capabilities ethically and responsibly.
