`timescale 1ns / 1ps
module stimulus;
	// Inputs
	reg [7:0] a;
	reg [7:0] b;
    reg [7:0] carry_in;
	// Outputs
	wire [7:0] sum;
    wire carry_out;
	// Instantiate the Unit Under Test (UUT)
	adder_8_bit uut (
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
		a = 00000000;
		b = 00000000;
        carry_in = 00000000;
 
	#20 a = 11111111;
	#20 b = 00000001;
    #20 carry_in = 00000000;
	#20 b = 00001000;
    #20 carry_in = 00000000;	
	#20 a = 00010001;	  
	#40 ;
 
	end  
 
		initial begin
		 $monitor("t=%3d a=%d,b=%d,carry_in=%d,sum=%d,carry_out=%d \n",$time,a,b,carry_in,sum,carry_out, );
		 end
 
endmodule