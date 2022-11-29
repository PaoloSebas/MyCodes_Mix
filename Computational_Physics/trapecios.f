program trapecios
	implicit real(a-h,o-z) !i,j,k,l,m,n
	external func
	external ex_int
	
	
	open(10,file='error_trapecios_1.dat')
	
	xa=0.e0
	xb=1.e0
	fexact=ex_int(xa,xb)

        fac=2.e0
	
	
	do k=1,23
	
	np=2**k

	
	h=(1.e0/float(np-1))*(xb-xa)
	h2=0.5e0*h

	
	x=xa	
	sum=func(x)

	
		
	do i=1,np-1
	 x=x+h	
	 sum=sum+fac*func(x)	
        enddo
	
	sum=sum+func(xb)
	
	fnum=h2*sum
	
		
	err=abs(fnum-fexact)
	
	write(10,*)log10(float(np)),log10(err)
	
	enddo
	
	end program trapecios	
	
      


	
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
