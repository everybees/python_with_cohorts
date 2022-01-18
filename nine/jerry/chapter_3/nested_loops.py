# 3.17 (Nested Loops) Write a script that displays the following triangle patterns separately, one below the other.
# Separate each pattern from the next by one blank line. Use for loops to generate the patterns.
# Display all asterisks (*) with a single statement of the form print('*', end='')
# which causes the asterisks to display side by side. [Hint: For the last two patterns, begin
# each line with zero or more space characters.]


for i in range(1, 11):
    for j in range(i):
        print("*", end=" ")
    print("\n")


        # for(int a = 1; a <= 10; a++){
        #     for(int b = 10; b >= a; b--){
        #         System.out.print(symbol);
        #     }
        #     System.out.println();
        # }
        # System.out.println();
        #
        # for(int p = 1; p <= 10; p++){
        #     for(int q = 2; q <= p; q++) {
        #         System.out.print(" ");
        #     }
        #     for(int r = p; r <= 10; r++){
        #         System.out.print(symbol);
        #     }
        #     System.out.println();
        # }
        # System.out.println();
        #
        # for(int x = 1; x <= 10; x++){
        #     for(int y = x; y < 10; y++){
        #         System.out.print(" ");
        #     }
        #     for (int z = 1; z <= x; z++){
        #         System.out.print(symbol);
        #     }
        #     System.out.println();
        # }