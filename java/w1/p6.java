import java.util.Scanner;

public class w1p6 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter data usage:");

        float data = scanner.nextFloat();

        if (data <= 1) {
            System.out.println("Normal Usage");
        } else if (data <= 3) {
            System.out.println("Warning");
        } else if (data <= 5) {
            System.out.println("Alert");

        } else {
            System.out.println("Data limit exceeded");
        }
    }
}
