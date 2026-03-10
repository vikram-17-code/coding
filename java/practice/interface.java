interface Pay{
    static final int fee = 100;
    public void proPay(double amount);
    public void pReceit();
}
class Creditcard implements Pay{
    double paid=0;
    public void proPay(double amount){
        paid = fee+amount;
    }
    @Override
    public void pReceit(){
        System.out.println("paid amount is "+paid);
    }
}
class UPI implements Pay{
    double paid=0;
    public void proPay(double amount){
        paid = fee+amount;
    }
    @Override
    public void pReceit(){
        System.out.println("paid amount is "+paid);
    }
}
public class payment {
    public static void main(String [] args){
        UPI a = new UPI();
        Creditcard b = new Creditcard();
        a.proPay(20000);
        a.pReceit();
        b.proPay(1000);
        b.pReceit();
    }
}
