module Filter (
    input wire clk,
    input wire [7:0] acc_data,
	 output reg [7: 0] filtered_data
	 );

always @(posedge clk) begin
	filtered_data <= acc_data;
end

endmodule
