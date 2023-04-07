`timescale 1ns / 1ps
module stimulus;
	// Inputs
	reg [7:0] taille;
	reg [7:0] prix;
   
	// Outputs
	wire [15:0] y;
    
	// Instantiate the Unit Under Test (UUT)
	regression_lineaire uut (
		taille, 
		prix, 
        y
	);
 
	initial begin
	$dumpfile("test.vcd");
    $dumpvars(0,stimulus);
		// Initialize Inputs
		taille = 00000000;
		prix = 00000000;
        
 
	#20 taille = 11111111;
	#20 prix = 00000001;
	#20 prix = 00001000;	
	#20 taille = 00010001;	  
	#40 ;
 
	end  
 
		initial begin
		 $monitor("t=%3d taille=%d,prix=%d,y=%d \n",$time,taille,prix,y, );
		 end
 
endmodule