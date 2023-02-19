`timescale 1ns/1ns

module data_converter_tb;

reg [7:0] data_in;
wire [7:0] data_out_1;
wire [7:0] data_out_2;
wire [3:0] hamming_sum;
reg clk;

data_converter dut (
    .data_in(data_in),
    .clk(clk),
    .data_out_1(data_out_1),
    .data_out_2(data_out_2),
    .hamming_sum(hamming_sum)
);

integer i;

initial begin
    $dumpfile("data_converter_tb.vcd");
    $dumpvars(0, data_converter_tb);
    clk = 0;
    data_in = 0;
    #5;
    for (i = 0; i < 256; i = i + 1) begin
        data_in = i;
        #5 clk = ~clk;
    end

    $finish;
end

endmodule


