## Project setup

To connect DBeaver (running on Windows) to a PostgreSQL database running inside WSL2 (Windows Subsystem for Linux 2), follow these steps:



### **Step 1: Find the WSL2 IP Address**

1. Open your WSL2 terminal.
2. Run the following command to get the IP address of your WSL2 instance:

   ```bash
   ip addr | grep inet
   ```

   Look for an IP address under `eth0` or similar (usually something like `172.20.x.x`).

**Note:** This IP changes every time you restart WSL2. For a persistent setup, consider binding Postgres to `0.0.0.0` and using Windows localhost.



### **Step 2: Configure PostgreSQL in WSL2 to Accept External Connections**

1. Edit the PostgreSQL configuration file (typically in `/etc/postgresql/14/main/postgresql.conf`, version may vary):

   ```bash
   sudo nano /etc/postgresql/*/main/postgresql.conf
   ```

2. Find the line:

   ```conf
   listen_addresses = 'localhost'
   ```

   And change it to:

   ```conf
   listen_addresses = '*'
   ```

3. Then edit the `pg_hba.conf` file:

   ```bash
   sudo nano /etc/postgresql/*/main/pg_hba.conf
   ```

4. Add the following line at the bottom:

   ```conf
   host    all             all             0.0.0.0/0            trust
   ```

   Note that for some reason, the password authenticaiton for WSL postgres is not working when connecting from Windows.
   So the `trust` (instead of `md5`) means anyone can access it without password. Also change the line 

   ```conf
   local    all             postgres                          md5
   ```

   to 

   ```conf
   local    all             postgres                          trust
   ```



### **Step 3: Restart PostgreSQL in WSL2**

```bash
sudo service postgresql restart
```



### **Step 4: Allow Windows to Connect**

Windows firewall may block the connection. Either:

* Temporarily disable it (not recommended), or
* Allow port 5432 through firewall settings.

Open powershell in administrator mode and forward the port to localhost using `netsh` (optional):

```powershell
netsh interface portproxy add v4tov4 listenport=5432 listenaddress=127.0.0.1 connectport=5432 connectaddress=<WSL_IP>
```

Replace `<WSL_IP>` with the one you found earlier.



### **Step 5: Connect in DBeaver**

1. Open DBeaver.
2. Create a new PostgreSQL connection.
3. Enter:

   * **Host**: WSL2 IP (or `127.0.0.1` if using `portproxy`)
   * **Port**: 5432 (or your configured port)
   * **Database**: your database name
   * **Username** and **Password**: as configured in PostgreSQL

Click **Test Connection** and connect.


## Notes

https://community.qlik.com/t5/Connectivity-Data-Prep/PostgreSQL-Password-forgot/td-p/2160246