This is a simple scanner to get the certificate data (serial number and CN). 
This scanner uses the underyling OS' openssl utility.
In the code a list is used rather than a dictionary because the dictionary will by default cannot hold duplicate keys (and if the same hostname appears more than once, only the last occurrence is kept, and previous ones are overwritten.)
Thus, for any entries where the FQDN is being probed for different ports, then it would not be considered and to overcome it, a list is used. 
Hope, this simple scanner will ease your work in some small way, enjoy !
