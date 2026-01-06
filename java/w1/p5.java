import java.util.Scanner;

public class w1p5 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter marks:");

        int m1 = scanner.nextInt();
        int m2 = scanner.nextInt();
        int m3 = scanner.nextInt();
        if(m1>39 && m2>39 && m3>39){
            int avg = (m1+m2+m3)/3;
            if (avg>75) {
                System.out.println("distinction");

            }
            else if(avg >60){
                System.out.println("first class");

            }
            else if(avg >50){
                System.out.println("second class");

            }
            else{
                System.out.println("pass");

            }
        }
        else{
            System.out.println("fail");
        }
    }
}
