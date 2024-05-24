# Secure File Transfer Protocol (SFTP)

A network protocol that provides file access, file transfer, and file management over any reliable data stream.
The SSH protocol supports encryption and other security methods to better protect file transfers.

!!! example

    Many financial institutions use SFTP to send customer transaction files for security reasons

## Fetch files from a local SFTP server

- You need to **connect to the local SFTP server**: initiate connection to the local SFTP, usually by executing these commands

```bash
sudo passwd <password>
sudo service ssh start
sftp <username>@<server IP>
```

- Enter the new password when prompted. You're connected to SFTP server.
- **Download a sample file**: Fetch a sample file from the server using the following command

```bash
get -r readme.txt
```

- **Disconnect**: When finished or download a sample file, exit the SFTP session by typing the `!` symbol.

- **Verify the downloaded file**: Confirm that the file has been successfully downloaded by using the following command

```bash
cat readme.txt
```
