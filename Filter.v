// this is a moving average filter

module Filter (
    input wire clk,
    input wire [7:0] acc_data,
	 output reg [7: 0] filtered_data
	 );

reg [7: 0] buffer [255: 0];
reg [7: 0] i;
integer j;

reg [7: 0] temp;

initial begin
	i = 8'b0;
	for (j = 0; j <= 255;  j = j + 1) begin
		buffer[i] = 8'b0;
	end
end

always @(posedge clk) begin
	
	i <= i + 1;
	buffer[i] <= acc_data;
	

	for (j = 0; j <= 255; j = j + 1) begin
		temp <= temp + buffer[i];	
	end
	
	filtered_data <= temp / 256;
end

endmodule
