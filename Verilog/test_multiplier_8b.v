`timescale 1ns / 1ps
module stimulus;
	// Inputs
	reg [7:0] a;
	reg [7:0] b;
   
	// Outputs
	wire [15:0] product;
    
	// Instantiate the Unit Under Test (UUT)
	multiplier_8b uut (
		a, 
		b, 
        product
	);
 
	initial begin
	$dumpfile("test.vcd");
    $dumpvars(0,stimulus);
		// Initialize Inputs
		a = 00000000;
		b = 00000000;
        
 
	#20 a = 11111111;
	#20 b = 00000001;
	#20 b = 00001000;	
	#20 a = 00010001;	  
	#40 ;
 
	end  
 
		initial begin
		 $monitor("t=%3d a=%d,b=%d,product=%d \n",$time,a,b,product, );
		 end
 
endmodule