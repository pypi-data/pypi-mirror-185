# Rsalogy
rsalogy is an implementation of the 
RSA asymmetric cryptographic algorithm 
implemented by Codelogy for the Python language.
## Security
Because of how Python internally stores numbers, it is very hard (if not impossible) to make a pure-Python program secure against timing attacks. This library is no exception, so use it with care. See https://securitypitfalls.wordpress.com/2018/08/03/constant-time-compare-in-python/ for more info.
