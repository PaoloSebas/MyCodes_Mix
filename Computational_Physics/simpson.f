program simpson
	implicit real(a-h,o-z) !i,j,k,l,m,n
	external func
	external ex_int
	
	
	open(10,file='error_simpson.dat')
	
	xa=0.e0
	xb=1.e0
	fexact=ex_int(xa,xb)
	
	
	do k=1,23
	
	np=2**k

	
	h=(1.e0/float(np-1))*(xb-xa)
	h3=h/3.e0

	
	x=xa	
	sum=func(x)

	
	fac=2.e0	
	do i=1,np-1
	
	
	 x=x+h	
	 if(fac.eq.2.e0)then
	 fac=4.e0
	 sum=sum+fac*func(x)
	 else 
	 fac=2.e0
	 sum=sum+fac*func(x)
	 end if
	
 	
        enddo
	
	sum=sum+func(xb)
	
	fnum=h3*sum
	
		
	err=abs(fnum-fexact)
	
	write(10,*)log10(float(np)),log10(err)
	
	enddo
	
	end program simpson
	

	
	function func(x)
	implicit real(a-h,o-z)
	func=exp(x)
	return
	end
	
	function ex_int(xa,xb)
	implicit real(a-h,o-z)	
	ex_int=func(xb)-func(xa)
	return
	end
