




# Carname     	Color	   Age  	Speed	    AutoPass
# BMW	            red      	5	     99	           Y
# Volvo	        black	    7	     86	           Y
# VW          	gray	    8	     87         	N
# VW	            white	    7	     88         	Y
# Ford	        white	    2	     111	        Y
# VW          	white	    17	      86	        Y
# Tesla	        red     	2	     103	        Y
# BMW	           black	    9	      87	        Y
# Volvo       	gray	    4	     94         	N
# Ford        	white   	11	     78	            N
# Toyota      	gray	    12	     77	            N
# VW           	white	    9	     85         	N
# Toyota	        blue     	6	     86         	Y




# speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
# (99+86+87+88+111+86+103+87+94+78+77+85+86) / 13 = 89.77




import numpy

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = numpy.mean(speed)

print(x)