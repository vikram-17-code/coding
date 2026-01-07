import java.util.Scanner;

public class w1p8 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter color:");
        String color = scanner.nextLine();
        if (color.equals("red")){
            System.out.println("stop");
        } else if (color.equals("yellow")) {
            System.out.println("wait");
        } else if (color.equals("green")) {
            System.out.println("go");
        }
    }
}
