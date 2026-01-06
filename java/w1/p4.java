import java.util.Scanner;

public class w1p4 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter age:");
        int amount = 500;
        int age = scanner.nextInt();
        if (age<5) {
            System.out.println("free");
            System.out.println("total:"+0);
        }
        else if(age>=5 && age<13){
            System.out.println("50% discount");
            System.out.println("total:"+(amount*.5));

        }
        else if(age>=13 && age<60){
            System.out.println("no discount");
            System.out.println("total:"+ amount);

        }
        else if(age>59 ){
            System.out.println("40% discount");
            System.out.println("total:"+(amount*.6));

        }
    }
}
