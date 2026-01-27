import java.util.Scanner;

public class w1p9 {
    public static void main(String []args){
        Scanner scanner = new Scanner(System.in);
        String name = scanner.nextLine();
        int salary =scanner.nextInt();

        int gross,net;
        gross = (int)((salary*0.2)+(salary*.1));
        int nets= (int)((gross+salary)*.95);
        int total = (int)((gross+salary));

        System.out.println("net salary:"+ nets);
        System.out.println("gross salary:"+total);

    }
}
