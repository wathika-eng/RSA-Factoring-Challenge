// Factors.java
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class Factors {
    // Function to factorize a long number
    public static List<String> factorize(long number) {
        List<String> factors = new ArrayList<>();

        // Check if the number is less than or equal to 1
        if (number <= 1) {
            factors.add(number + "=1*" + number);
        } else {
            long i = 2;
            while (i <= number) {
                // Check if the number is divisible by i
                while (number % i == 0) {
                    // Add the factorization to the list
                    factors.add(number + "=" + i + "*" + (number / i));
                    // Update the number by dividing it by i
                    number /= i;
                }
                // Increment i
                i++;
            }
        }
        return factors;
    }

    public static void main(String[] args) {
        // Check for the correct command-line argument
        if (args.length != 1) {
            System.err.println("Usage: Factors <file>");
            System.exit(1);
        }

        String inputFileName = args[0];

        try (BufferedReader reader = new BufferedReader(new FileReader(inputFileName))) {
            String line;
            while ((line = reader.readLine()) != null) {
                // Parse the input as a long
                long number = Long.parseLong(line);

                // Call the factorize function and store the result
                List<String> factorizations = factorize(number);

                // Print each factorization result
                for (String factorization : factorizations) {
                    System.out.println(factorization);
                }
            }
        } catch (IOException e) {
            System.err.println("An unexpected error occurred: " + e.getMessage());
            System.exit(1);
        }
    }
}