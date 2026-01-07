import java.util.Scanner;

public class w1p7 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter NO burger:");
        int i1 = scanner.nextInt();
        System.out.print("Enter NO pizza:");
        int i2 = scanner.nextInt();
        System.out.print("Enter NO pasta:");
        int i3 = scanner.nextInt();
        float total = 0;
        total+=(i1*12)+(i2*15)+(i3*18);
        total+=(total*.05);

        if (total>1000) total = (float)(total * .9);
        System.out.println("total price:"+total);
    }
}
