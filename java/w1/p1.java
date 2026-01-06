import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("enter the name of the user:");
        String name = scanner.nextLine();
        System.out.print("enter the units");
        int current = scanner.nextInt();
        int temp= current;

        int total = 0;

        if(current<=100){
            total+=(current*1.5);
        } else if (current>100 && current<=200) {
            total+=(100*1.5);
            current-=100;
            total +=(current*2.5);
        } else if (current>200) {
            total+=(100*1.5);
            total+=(100*2.5);
            current -=200;
            total+=(current*4);


        }
        total+=75;
        System.out.println("name of the customer:"+name);
        System.out.println("units:"+temp);
        System.out.println("total:"+total);

    }
}
