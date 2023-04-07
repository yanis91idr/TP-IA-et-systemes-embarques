`timescale 1ns / 1ps
module stimulus;
	// Inputs
	reg a;
	reg b;
    reg carry_in;
	// Outputs
	wire sum;
    wire carry_out;
	// Instantiate the Unit Under Test (UUT)
	adder_1_bit uut (
		a, 
		b, 
        carry_in, 
		sum,
        carry_out
	);
 
	initial begin
	$dumpfile("test.vcd");
    $dumpvars(0,stimulus);
		// Initialize Inputs
		a = 0;
		b = 0;
        carry_in = 0;
 
	#20 a = 1;
	#20 b = 1;
    #20 carry_in = 1;
	#20 b = 0;
    #20 carry_in = 0;	
	#20 a = 1;	  
	#40 ;
 
	end  
 
		initial begin
		 $monitor("t=%3d a=%d,b=%d,carry_in=%d,sum=%d,carry_out=%d \n",$time,a,b,carry_in,sum,carry_out, );
		 end
 
endmodule