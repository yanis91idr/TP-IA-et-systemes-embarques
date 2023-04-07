module adder_1_bit(
    input a,
    input b,
    input carry_in,
    output sum,
    output carry_out
);

assign sum = a ^ b ^ carry_in;
assign carry_out = (a & b) | (carry_in & (a ^ b));

endmodule
