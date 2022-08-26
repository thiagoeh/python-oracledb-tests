Oracle Cloud free tier don't allow Autonomous Database connections over public Internet without mTLS enable.

Test code was adjusted to use the authentication wallet, with client certificate.


## References
* https://python-oracledb.readthedocs.io/en/latest/user_guide/installation.html#quickstart
* https://python-oracledb.readthedocs.io/en/latest/user_guide/connection_handling.html#mutual-tls-mtls-connection-to-oracle-autonomous-database
* https://docs.oracle.com/en/cloud/paas/autonomous-data-warehouse-cloud/cswgs/autonomous-connect-download-credentials.html
