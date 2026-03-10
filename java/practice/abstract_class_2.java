abstract class Employee1{
    String name;
    int id;
    final String companyname="abc";
    abstract double calSal();
    void displayemployee(int salary){
        System.out.println("name" + name);
        System.out.println("id" + id);
        System.out.println("salary" + salary);
    }
}
class Fulltime extends Employee1{
    int salary;
    Fulltime(String name,int id,int salary){
        super.name = name;
        super.id = id;
        this.salary = salary;
    }
    double calSal(){
        return salary;
    }

}
class Parttime extends Employee1{
    int hours,rate;
    Parttime(String name,int id,int hours,int rate){
        super.name = name;
        super.id = id;
        this.hours = hours;
        this.rate = rate;
    }
    double calSal(){
        return hours*rate;
    }

}
public class employee {
    public static void main(String [] args){
        Fulltime a = new Fulltime("alex",1,20000);
        Parttime b = new Parttime("beth",2,50,200);
        double s1 = a.calSal(),s2 = b.calSal();
        a.displayemployee((int)s1);
        a.displayemployee((int)s2);
    }

}
