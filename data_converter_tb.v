`timescale 1ns / 1ns

module data_converter_tb;

reg [7:0] data_in;
wire [7:0] data_out_1;
wire [7:0] data_out_2;
wire [3:0] hamming_sum;

data_converter dut (
    .data_in(data_in),
    .data_out_1(data_out_1),
    .data_out_2(data_out_2),
    .hamming_sum(hamming_sum)
);

initial begin
    $dumpfile("data_converter_tb.vcd");
    $dumpvars(0, data_converter_tb);

    for (int i = 0; i < 256; i++) begin
        data_in = i;
        #10;
        $display("data_in = %d, data_out_1 = %b, data_out_2 = %b, hamming_sum = %d",
                 data_in, data_out_1, data_out_2, hamming_sum);
    end

    $finish;
end

endmodule