module regression_lineaire(
  input [7:0] taille,
  input [7:0] prix,
  output reg [15:0] y
);

  wire [15:0] resultat_mult;
  wire [15:0] constante;

  assign constante = 16'd10000;
  assign resultat_mult = prix * taille;

  always @ (prix or taille) begin
    y = constante + resultat_mult;
  end

endmodule
