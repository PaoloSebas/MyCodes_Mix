program Poincare 

implicit none 

integer,parameter :: dp=kind(0.d0)

!*******Defino las variables******

Real (kind(1._dp)):: q1in, q2in, p1in, p2in, dt, t, ti, tf,dp1,dq1
Real (kind(1._dp)), allocatable, dimension(:) :: E, x, y     !vectores
Real (kind(1._dp)), allocatable, dimension(:) :: q1,q2,p1,p2 !vectores

integer ::i,j,n,k,m,nxi,idum,nxp1,nxq1

!********Abro files para grabar los datos ********

open(21,file='Energia_5.dat')
open(22,file='Energia_20.dat')
open(23,file='Energia_100.dat')
open(41,file='Energia_5_q2_cero.dat')
open(42,file='Energia_20_q2_cero.dat')
open(43,file='Energia_100_q2_cero.dat')

n=20000!****numero de pasos en un intervalo de 200 s en tiempo

allocate (E(1:3))
allocate (x(1:4))
allocate (y(1:4))

allocate (q1(1:20000))
allocate (p1(1:20000))
allocate (q2(1:20000))
allocate (p2(1:20000))

E=(/5.d0,20.d0,100.d0/)

do i=1,3

	ti=0._dp
	
	tf=1500._dp
	
	dt=(tf-ti)/float(n)
	
	!E=E(i)
	
	q1in=2._dp
	q2in=0._dp
	p1in=0._dp
	p2in=sqrt(2._dp*E(i)-(q1in**2._dp))
	
	nxq1=50
	nxp1=50
	
	dq1=((dsqrt(2*E(i))-(-(dsqrt(2*(E(i)))))))/nxq1
	dp1=((dsqrt(2*E(i))-(-(dsqrt(2*(E(i)))))))/nxp1
	
	
	t=ti
	
x=(/q1in,q2in,p1in,p2in/)

!******loop sobre las CI 

     
		do k=1,nxq1

           do m=1,nxp1
			!*****loop sobre los tiempos 
			
			
		   do j=1,n

				q1(j)=x(1)
				q2(j)=x(2)
				p1(j)=x(3)
				p2(j)=x(4)
			
				call RK4_Sub(dt,t,x,y,f)
		
					t=t+dt
		
					!write(20+i,*) t, y
		
					if ((q2(j)*q2(j-1)<0) .and. p2(j)>0) then  
		
					write (40+i,*) q1(j),q2(j),p1(j),p2(j)
		
					end if 
		
					x=y
					
					!print*,y
		
		     enddo
		
				x(1)=x(1)+dq1	 
				x(2)=0._dp
				x(4)=sqrt(2._dp*E(i)-(x(1)*x(1))-(x(3)*x(3)))
	  
	            if ( (((x(1)*x(1)))+(x(3)*x(3))) >= 2._dp*E(i)) cycle          	   
		  
		 
		      enddo  
		
		       
		
		     
		      
		        !if (abs(x(1))>=(dsqrt(2*E(i))) .or. (abs(x(3))>=(dsqrt(2*E(i))))) cycle   
	
	               
	
	            enddo 
	            
	             x(3)=x(3)+dp1
	                     
		        
	             
	             
	   enddo
	   



close(21)
close(22)
close(23)
close(40)

contains 

function f(t,x)
	Real(kind(1d0)) :: t
	Real (kind(1d0)), dimension(4) :: x,f
	f= (/x(3),x(4),-x(1)-0.1d0*x(1)*(x(2))**2,-x(2)-0.1d0*x(2)*(x(1))**2/) 
	! son 4 componentes desde 4 ecuaciones de primer grado (las 4 derivadas)
end function 	



subroutine RK4_Sub(dx,x,z,y,f)
Implicit none
real (kind(1d0)), intent(in) :: dx,x
real (kind(1d0)), dimension(4), intent(in)  ::z
real (kind(1d0)), dimension(4), intent(out) ::y
real (kind(1d0)), dimension(4)::k1, k2, k3, k4

	interface
		function f(t,x)
 		Real(kind(1d0)) ::t
 		Real(kind(1d0)), dimension(4) :: x,f
		end function
	end interface
	
	k1=dx*f(x,z)
	k2=dx*f(x+dx/2.d0,z+k1/2.d0)
	k3=dx*f(x+dx/2.d0,z+k2/2.d0)
	k4=dx*f(x+dx,z+k3)
	y=z+(k1/6.d0+k2/3.d0+k3/3.d0+k4/6.d0)
	
end subroutine


end program Poincare
