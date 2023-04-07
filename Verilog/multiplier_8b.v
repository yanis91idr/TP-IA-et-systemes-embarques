module multiplier_8b(
    input [7:0] a,
    input [7:0] b,
    output reg [15:0] product
);

always @(*) begin
    product = a * b;
end

endmodule
