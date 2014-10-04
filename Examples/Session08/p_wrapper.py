 @p_wrapper
   ...: def return_a_string(string):
   ...:     return string
   ...:

In [5]: return_a_string("this is a string")
Out[5]: '<p> this is a string </p>'

Extra credit:

@tag_wrapper('html')
   ...: def return_a_string(string):
   ...:     return string

return_a_string("this is a string")
<html> this is a string </html>

