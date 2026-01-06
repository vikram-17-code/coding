import java.util.Scanner;

public class w1p3 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter amount");
        int amount = scanner.nextInt();
        if (amount<1000) {
            System.out.println("no discount");
            System.out.println("total"+amount);
        }
        else if(amount>=1000 && amount<5000){
            System.out.println("10% discount");
            System.out.println("total:"+(amount*.9));

        }
        else if(amount>=5000 && amount<10000){
            System.out.println("20% discount");
            System.out.println("total:"+(amount*.8));

        }
        else if(amount>10000 ){
            System.out.println("30% discount");
            System.out.println("total:"+(amount*.7));

        }
    }
}
