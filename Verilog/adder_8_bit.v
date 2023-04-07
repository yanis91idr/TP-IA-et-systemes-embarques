module adder_8_bit(
    input [7:0] a,
    input [7:0] b,
    input [7:0] carry_in,
    output reg [7:0]  sum,
    output reg carry_out
);

reg [7:0] carry;   
integer i;  

always @(*) begin
    sum = 8'b0;  
    carry = carry_in;  
    for (i = 0; i < 8; i = i + 1) begin
        
        sum[i] = a[i] ^ b[i] ^ carry;

        carry = (a[i] & b[i]) | (carry & (a[i] ^ b[i]));
    end
    carry_out = carry;
end

endmodule

