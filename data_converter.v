module data_converter (
    input wire clk,
    input [7:0] data_in,
    output wire [7:0] data_out_1,
    output wire [7:0] data_out_2,
    output reg [3:0] hamming_sum
);

reg [7:0] prior_data;
reg [7:0] input_data;
reg [7:0] output_data_1;
reg [7:0] output_data_2;
reg [3:0] ham_count_out_1;
reg [3:0] ham_count_out_2;
integer i;

always @(posedge clk) begin
    prior_data <= input_data;
    input_data <= data_in;
end

always @* begin
    output_data_1 = input_data;
    ham_count_out_1 = 0;
    for (i = 0; i < 8; i = i + 1) begin
        if (prior_data[i] ^ output_data_1[i]) begin
            ham_count_out_1 = ham_count_out_1 + 1;
        end
        
    output_data_2 = prior_data;
    for (i = 0; i < 8 - ham_count_out_1; i = i + 1) begin
        output_data_2[i] = ~prior_data[i];
        end
        
    ham_count_out_2 = 0;
    for (i = 0; i < 8; i = i + 1) begin
        if (prior_data[i] ^ output_data_2[i]) begin
            ham_count_out_2 = ham_count_out_2 + 1;
        end
    end

    hamming_sum = ham_count_out_1 + ham_count_out_2; 
end
end

assign data_out_1 = output_data_1;
assign data_out_2 = output_data_2;

endmodule


