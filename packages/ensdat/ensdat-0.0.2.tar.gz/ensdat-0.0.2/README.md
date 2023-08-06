

Useful modules for encryption and file encryption and decryption (currently only string decryption)

## test

making key code :
```python
print(destr.make_key('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'))
# result : [97, 97, 97, 97, 
#           97, 97, 97, 97, 
#           97, 97, 97, 97, 
#           97, 97, 97, 97, 
#           97, 97, 97, 97, 
#           97, 97, 97, 97, 
#           97, 97, 97, 97, 
#           97, 97, 97, 97]
```
encrypting code
```python
print(destr.ens('this is test str.', destr.key)) 
# result : b'89k2hfSgnomKayxjTYPH4rxGGMSZORJJueh8x53OCaXq4+UFzTWeU2qjQQcqmtMV'
print(destr.ens('this is test str.', destr.key)) 
# result : b'qfEw+NuqhmIsq1DbXZh6glNEQSW3EUkZWxFEOdQwdSudTGWszjA17BNF27hSgBgs'
print(destr.ens('this is test str.', destr.key)) 
# result : b'xxMjhD7BbBTNKYDWM9W9F51n13VgxGtUqYbVGx5ErBvcWBVHG4umnaHPPsoobcj2'
print(destr.ens('this is test str.', destr.key)) 
# result : b'JdheT2cei4KTYHY3I8aMMi+9xYX#+ugySPBGLAuUpZE6VlSNWKmguyifgI5yxh8YG'
```

decrypting code
```python
print(destr.des(b'89k2hfSgnomKayxjTYPH4rxGGMSZORJJueh8x53OCaXq4+UFzTWeU2qjQQcqmtMV', destr.key))
# result : 'this is test str.'
```