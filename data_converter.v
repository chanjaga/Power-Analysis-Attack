module data_converter (
    input [7:0] data_in,
    output reg [7:0] data_out_1,
    output reg [7:0] data_out_2,
    output reg [3:0] hamming_sum
);

reg [7:0] prior_data;
reg [7:0] latter_data_1;
reg [7:0] latter_data_2;

always @ (data_in) begin
    prior_data = data_in;
    latter_data_1 = data_in ^ 8'b01010101;
    latter_data_2 = data_in ^ 8'b10101010;
    hamming_sum = $countones(latter_data_1 ^ prior_data) + $countones(latter_data_2 ^ prior_data);
end

assign data_out_1 = latter_data_1;
assign data_out_2 = latter_data_2;

endmodule