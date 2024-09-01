module uart(input wire [7:0] data_in, //input data
				input wire wr_en,
				input wire clk_50m,
				output wire Tx,
				output wire Tx_busy
				);		

wire Txclk_en;
		 

baudrate uart_baud(	.clk_50m(clk_50m),
							.Txclk_en(Txclk_en)
							);
							
transmitter uart_Tx(	.data_in(data_in),
							.wr_en(wr_en),
							.clk_50m(clk_50m),
							.clken(Txclk_en), //We assign Tx clock to enable clock 
							.Tx(Tx),
							.Tx_busy(Tx_busy)
							);
							

endmodule
