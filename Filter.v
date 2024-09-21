// this is a moving average filter

module Filter (
    input wire clk,
//	 input wire rst,
    input wire [7:0] acc_data,
	 output reg [7:0] filtered_data
	 );

reg [7: 0] buffer [255: 0];
reg [7: 0] i;
integer j;

reg [15: 0] temp;


always @(posedge clk) begin
//
//	if (rst) begin
//		i <= 0;
//		temp <= 16'b0;
//      for (j = 0; j <= 255; j = j + 1) begin
//          buffer[j] <= 8'b0;
//      end
//		filtered_data <= 0;
//	
//	end else begin
		
		i <= (i + 1);
		buffer[i] <= acc_data;
		
		temp <= 16'b0;
		for (j = 0; j <= 255; j = j + 1) begin
			temp <= temp + buffer[j];	
		end
		
//		filtered_data <= temp[15:8];
		filtered_data <= (temp / 256*256 > 8'd255) ? 8'd255 : temp[7:0];
//	end

end

endmodule
