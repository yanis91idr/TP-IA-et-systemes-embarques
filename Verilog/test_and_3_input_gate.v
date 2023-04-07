`timescale 1ns / 1ps
module stimulus;
	// Inputs
	reg x;
	reg y;
    reg w;
	// Outputs
	wire z;
	// Instantiate the Unit Under Test (UUT)
	and_3_input_gate uut (
		x, 
		y, 
        w, 
		z
	);
 
	initial begin
	$dumpfile("test.vcd");
    $dumpvars(0,stimulus);
		// Initialize Inputs
		x = 0;
		y = 0;
        w = 0;
 
	#20 x = 1;
	#20 y = 1;
    #20 w = 1;
	#20 y = 0;
    #20 w = 0;	
	#20 x = 1;	  
	#40 ;
 
	end  
 
		initial begin
		 $monitor("t=%3d x=%d,y=%d,w=%d,z=%d \n",$time,x,y,w,z, );
		 end
 
endmodule