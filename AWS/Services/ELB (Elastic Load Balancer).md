Service on [[AWS (Amazon Web Services)]] that forward internet traffic to multiple servers downstream.

##### Why use Load Balancer?
1. Spread load across multiple instances
2. Expose single point DNS to app
3. Seamlessly handle failure of downstream instances
4. Regular health check for our instances
5. Provide SSL termination (HTTPS)
6. High availability accross zones
7. ELB -> Managed load balancer
	1. Guaranteed by aws 
8. Cost slightly higher instead of manual load balancer

##### AWS Load Balancer
1. Application Load Balancr (HTTP/HTTPS only) -> Layer 7
2. Network Load Balancer (ultra-high performance, TCP) -> Layer 4 (TCP and UDP)
3. Gateway Load Balancer -> Layer 3
4. Classic Load Balancer <mark style="background: #CACFD9A6;">retired in 2023</mark> -> Layer 4 & 7

| Application Load Balancer | Network Load Balancer                 | Gateway Load Balancer                                     |
| ------------------------- | ------------------------------------- | --------------------------------------------------------- |
| HTTP / HTTPS / [[gRPC]]   | TCP / UDP protocols                   | GENEVE Protocol on IP Packets                             |
| HTTP Routing Features     | High performance: millions of request | Route Traffic to Firewalls                                |
| Static DNS (URL)          | Static IP through Elastic IP          | Intrusion detection                                       |
|                           |                                       | Redirect traffic to 3rd party security virtual appliances |
Gateway load balancer need to give traffic to inspect packets on security appliances and traffic send back to GWLB and sent to Application EC2